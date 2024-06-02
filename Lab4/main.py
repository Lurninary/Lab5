import json
import random

from flask import Flask, render_template, request
from flask_mail import Mail, Message
from werkzeug.utils import secure_filename, redirect
from loginForm import AstronautSelectionForm
import os

app = Flask(__name__, static_folder="./members/photo", template_folder="./templates")
app.config['SECRET_KEY'] = 'my_secret_key'
app.config['MAIL_SERVER'] = 'smtp.mail.ru'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'plisko.ivan@mail.ru'
app.config['MAIL_PASSWORD'] = 'zqvFdb7wirsp5AZMECw5'
app.config['MAIL_USE_TLS'] = True
app.config['UPLOAD_FOLDER'] = 'static/uploads'

mail = Mail(app)


@app.route('/')
@app.route('/index', methods=['GET'])
def mission():
    return render_template("index.html", title="Добро пожаловать")


@app.route('/list_prof/<list>')
def show_list(list):
    professions = ["Инженер-механик", "Биолог", "Пилот", "Врач", "Астроном", "Гид по Марсу", "Строитель", "Эколог",
                   "Финансист", "Юрист"]

    if list == "ol":
        return render_template('list_prof.html', title='Список профессий', type='ol', professions=professions)
    elif list == "ul":
        return render_template('list_prof.html', title='Список профессий', type='ul', professions=professions)
    else:
        return "Неверный параметр"


@app.route('/distribution')
def distribution():
    with open('members/crew_members.json', 'r', encoding='utf-8') as file:
        crew_data = json.load(file)
    return render_template('distribution.html', title='Размещение', crew_data=crew_data)


@app.route('/member/<int:number>')
def member_by_number(number):
    with open('members/crew_members.json', 'r', encoding='utf-8') as file:
        crew_data = json.load(file)
    return render_template('member.html', title='Член экипажа', member=crew_data[number])


@app.route('/member/random')
def member_random():
    with open('members/crew_members.json', 'r', encoding='utf-8') as file:
        crew_data = json.load(file)
    return render_template('member.html', title='Член экипажа', member=random.choice(crew_data))


@app.route('/room/<sex>/<int:age>')
def room(sex, age):
    return render_template('room.html', title='Оформление каюты', sex=sex, age=age)


@app.route('/astronaut_selection', methods=['GET', 'POST'])
def astronaut_selection():
    form = AstronautSelectionForm()
    if form.validate_on_submit():
        filename = secure_filename(form.photo.data.filename)
        form.photo.data.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        msg = Message("Запись добровольцем", sender="plisko.ivan@mail.ru",
                      recipients=["plisko.ivan@mail.ru"])
        msg.body = f"""
                        Фамилия: {form.surname.data}
                        Имя: {form.name.data}
                        Email: {form.email.data}
                        Образование: {form.education.data}
                        Основная профессия: {form.main_profession.data}
                        Пол: {form.gender.data}
                        Мотивация: {form.motivation.data}
                        Готовы ли остаться на Марсе?: {form.stay_on_mars.data}
                        Прикреплено фото: {filename}"""
        with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), "rb") as image_file:
            image_content = image_file.read()
        msg.attach(filename, "image/png", image_content)
        mail.send(msg)
        return redirect('/success')
    return render_template('astronaut_selection.html', title="Запись добровольцем", form=form)


@app.route('/success')
def success():
    return '''<h1 style="text-align: center; color: #d22e3a;">Форма отправлена</h1>'''


@app.route('/galery', methods=['GET', 'POST'])
def galery():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join("static/img/Mars", filename))
        return "Изображение успешно загружено!"

    images = os.listdir("static/img/Mars")

    return render_template('galery.html', title="Галерея", images=images)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
