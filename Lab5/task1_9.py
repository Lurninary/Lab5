from data.jobs import Jobs
from data.users import User
from data import db_session
from sqlalchemy import func

db_session.global_init("db/mars_explorer.db")

db_sess = db_session.create_session()

team_sizes = db_sess.query(Jobs.team_leader, func.count()).group_by(Jobs.team_leader).all()

max_team_size = max(team_sizes, key=lambda x: x[1])[1]

team_leaders = [team_leader[0] for team_leader in team_sizes if team_leader[1] == max_team_size]

team_leaders_info = db_sess.query(User.surname, User.name).filter(User.id.in_(team_leaders)).all()

for leader in team_leaders_info:
    print(f"{leader.surname} {leader.name}")

db_sess.close()
