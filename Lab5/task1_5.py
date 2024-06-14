from data.users import User
from data import db_session

db_session.global_init("db/mars_explorer.db")

db_sess = db_session.create_session()

colonist_ids = db_sess.query(User.id).filter(~User.speciality.like('%engineer%'))\
    .filter(~User.position.like('%engineer%')).all()

for colonist_id in colonist_ids:
    print(colonist_id[0])

db_sess.close()
