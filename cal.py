from flask import Flask, render_template, redirect

from wtf_cal import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Заготовка')


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<list>')
def list_prof(list):
    prof = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог',
            'врач', 'инженер по терраформированию', 'климатолог',
            'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
            'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода',
            'киберинженер', 'штурман', 'пилот дронов']
    return render_template('parasha.html', prof=prof, list=list)


@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    params = {
        'title': 'Анкета',
        'surname': 'Масло',
        'name': 'Сергей',
        'education': 'МиМК',
        'profession': 'мастер по автомобильным маслам',
        'sex': 'м',
        'motivation': 'всегда мечтал менять масло в транспорте на Марсе',
        'ready': 'всегда'

    }
    return render_template('maslo.html', **params)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/success')
def success():
    return 'SUCCESS'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
