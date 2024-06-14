from data.users import User
from data import db_session

db_session.global_init("db/mars_explorer.db")

db_sess = db_session.create_session()

colonists = db_sess.query(User).filter(User.position.like('%chief%') | User.position.like('%middle%')).all()

for colonist in colonists:
    print(colonist)

db_sess.close()
