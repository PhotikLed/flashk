from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    data_list = [
        {
            'surname': 'Scott',
            'name': 'Ridley',
            'age': 21,
            'position': 'captain',
            'speciality': 'research engineer',
            'address': 'module_1',
            'email': 'scott_chief@mars.org',

        },
        {
            'surname': 'Maslo',
            'name': 'Sergey',
            'age': 25,
            'position': 'maslozamenitel',
            'speciality': 'specialist po masla',
            'address': 'butyl s maslom',
            'email': 'siboil@mars.org',

        },
        {
            'surname': 'Misha',
            'name': 'Antifreeze',
            'age': 20,
            'position': 'reqg',
            'speciality': 'specialist po cal',
            'address': 'butyl s aytifrizom',
            'email': 'antifriz@mars.org',

        },
        {
            'surname': 'petr',
            'name': 'patron',
            'age': 60,
            'position': 'pulemetchik',
            'speciality': 'specialist po patron',
            'address': 'otcek s patron',
            'email': 'patron@mars.org',

        }
    ]
    session = db_session.create_session()
    for user_data in data_list:
        user = User(**user_data)
        session.add(user)
    session.commit()
    # app.run()


if __name__ == '__main__':
    main()
