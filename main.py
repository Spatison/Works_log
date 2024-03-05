from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def works_log():
    db_sess = db_session.create_session()
    work = db_sess.query(Jobs).all()
    user = db_sess.query(User).all()
    return render_template('works_log.html', work=work, user=user)


def main():
    db_session.global_init("db/blogs.db")
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()