import random
from datetime import datetime, timedelta
from flask import Flask
from generator import ColonistGenerator
from data import db_session
from data.users import User
from data.jobs import Jobs
from data.departments import Departments


app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()

    db_sess.add(User(**{
            "surname": 'Scott',
            "name": 'Ridley',
            "age": 21,
            "position": 'captain',
            "speciality": 'research engineer',
            "address": 'module_1',
            "email": 'scott_chief@mars.org',
            "hashed_password": 'cap_pass123',
            "created_date": datetime.now()
        }))
    colonist_generator = ColonistGenerator()
    colonist_generator.generate_all_colonists()
    for colonist_data in colonist_generator.crew_members:
        db_sess.add(User(**colonist_data))

    db_sess.add(Jobs(**{
        "team_leader": 1,
        "job": 'deployment of residential modules 1 and 2',
        "work_size": 15,
        "collaborators": '2, 3',
        "start_date": datetime.now(),
        "end_date": None,
        "is_finished": False
    }))

    jobs_list = [
        {
            "team_leader": random.randint(1, 6),
            "job": 'Cooking',
            "work_size": random.randint(10, 20),
            "collaborators": ', '.join([str(random.randint(1, 6)) for _ in range(random.randint(1, 3))]),
            "start_date": datetime.now(),
            "end_date": None,
            "is_finished": False
        },
        {
            "team_leader": random.randint(1, 6),
            "job": 'Construction of the central park',
            "work_size": random.randint(25, 35),
            "collaborators": ', '.join([str(random.randint(1, 6)) for _ in range(random.randint(1, 3))]),
            "start_date": datetime.now() - timedelta(days=random.randint(30, 90)),
            "end_date": None,
            "is_finished": True
        },
        {
            "team_leader": random.randint(1, 6),
            "job": 'Installation of solar panels on the roof',
            "work_size": random.randint(18, 28),
            "collaborators": ', '.join([str(random.randint(1, 6)) for _ in range(random.randint(1, 3))]),
            "start_date": datetime.now() + timedelta(days=random.randint(120, 180)),
            "end_date": None,
            "is_finished": False
        }
    ]

    for job_data in jobs_list:
        db_sess.add(Jobs(**job_data))

    db_sess.add(Departments(**{
        "title": 'department_1',
        "chief": 2,
        "members": '2, 3',
        "email": 'email@mail.ru'
    }))

    db_sess.commit()
    app.run()


if __name__ == '__main__':
    main()