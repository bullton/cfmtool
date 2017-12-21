from flask import render_template
from flask_pymongo import PyMongo
from app import app
from app.form import BaseLogin
from flask import url_for

app.config.update(
    MONGO_HOST='127.0.0.1',
    MONGO_PORT=27017,
    MONGO_USERNAME='dba',
    MONGO_PASSWORD='dba',
    MONGO_DBNAME='mydb'
)
mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' } # fake user
    posts = [ # fake array of posts
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        }
    ]
    books = mongo.db.books.find_one({'lang': 'python'})
    return render_template("index.html",
        title = 'Customer Fault Mamagement Tool',
        user = user,
        posts = posts,
        name = books['author'])

@app.route("/test",methods=['GET','POST'])
def TTest():
    form = BaseLogin()
    if form.validate_on_submit():
        flash(form.name.data+'|'+form.password.data)
        return redirect(url_for('success'))
    else:
        return render_template('index.html',form=form)