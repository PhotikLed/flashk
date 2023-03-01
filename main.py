import datetime

from flask import Flask, render_template, redirect, make_response, jsonify
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from data import db_session
from data.users import User
from data.jobs import Jobs
from forms.jobs import JobForm
from wtf_cal import LoginForm
from jobs_api import blueprint as jobs_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/works_log')
@app.route('/')
def works_log():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    return render_template('index.html', jobs=jobs)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/add_job', methods=['GET', 'POST'])
@login_required
def add_job():
    form = JobForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        news = Jobs()
        news.job = form.job.data
        news.work_size = form.work_size.data
        news.collaborators = form.collaborators.data
        news.start_date = form.start_date.data
        news.end_date = form.end_date.data
        news.is_finished = form.is_finished.data
        current_user.news.append(news)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/')
    return render_template('news.html', title='Добавление новости',
                           form=form)


def main():
    db_session.global_init('db/mars_explorer.db')
    app.register_blueprint(jobs_blueprint)

    session = db_session.create_session()
    user = session.query(User).get(5)
    user.set_password('11111111')
    session.commit()
    app.run()


if __name__ == '__main__':
    main()
