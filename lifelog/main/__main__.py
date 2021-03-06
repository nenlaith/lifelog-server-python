from lifelog.main.flask_application import create_app
from lifelog.main.test_database import test

app = create_app()
test()
# app.run(port=8080)
