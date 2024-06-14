from data.jobs import Jobs
from data import db_session

db_session.global_init("db/mars_explorer.db")

db_sess = db_session.create_session()

jobs = db_sess.query(Jobs).filter(Jobs.work_size < 20, ~Jobs.is_finished).all()

for job in jobs:
    print(job)

db_sess.close()
