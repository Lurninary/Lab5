from flask import Flask, render_template, redirect
from forms.user import RegisterForm
from data.jobs import Jobs
from data.users import User
from data import db_session

app = Flask(__name__)

app.config['SECRET_KEY'] = 'my_secret_key'


@app.route('/')
def index():
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs)
    return render_template('main_page.html', title="Works log", jobs=jobs)


@app.route('/register', methods=['GET', 'POST'])
def register_form():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_session.global_init("db/mars_explorer.db")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            email=form.email.data,
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/success')
    return render_template('register.html', title="Register form", form=form)


@app.route('/success')
def success():
    return '''<h1 style="text-align: center; color: #d22e3a;">Пользователь сохранен</h1>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
