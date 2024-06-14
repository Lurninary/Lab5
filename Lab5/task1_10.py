from data.users import User
from data import db_session

db_session.global_init("db/mars_explorer.db")

db_sess = db_session.create_session()

db_sess.query(User).filter(User.address == "module_1", User.age < 21).update({User.address: "module_3"})

db_sess.commit()

for user in db_sess.query(User).all():
    print(f"{user} - {user.address}")

db_sess.close()
