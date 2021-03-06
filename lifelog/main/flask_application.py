import connexion

from lifelog.main.database import get_session

app = None


def create_app():
    global app

    if app:
        return app
    app = connexion.App(__name__, specification_dir='../openapi/')
    app.session = get_session()

    # app.app.json_encoder = encoder.JSONEncoder
    # app.add_api('openapi.yaml', arguments={'title': 'LifeLog'}, pythonic_params=True)
    return app
