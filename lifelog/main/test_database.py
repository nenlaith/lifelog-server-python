import time


def test():
    from lifelog.models.drink import Drink
    from lifelog.main.database import get_session

    sess = get_session()

    drink_001 = Drink()
    drink_001.quantity = 100.0
    drink_001.drink_type = 'tea'

    sess.add(drink_001)
    sess.commit()

    time.sleep(10)

    drink_001.added_fat = 10.0

    sess.commit()
