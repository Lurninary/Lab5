from data.users import User
from data import db_session

db_session.global_init("db/mars_explorer.db")

db_sess = db_session.create_session()

underage_colonists = db_sess.query(User).filter(User.age < 18).all()

for colonist in underage_colonists:
    print(f"{colonist.surname} {colonist.name}: {colonist.age} лет")

db_sess.close()
