from flask import render_template, request, redirect

from users_app.models.user_model import User

from users_app import app

@app.route('/')
def index():

    user_list = User.get_all()

    return render_template('index.html', user_list = user_list)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    User.create(request.form)
    return redirect('/')

@app.route('/edit/<int:id>')
def edit(id):
    User.get_one(id)
    return render_template('edit.html', user = User.get_one(id))\

@app.route('/update_user', methods=['POST'])
def update_user():
    User.update(request.form)
    return redirect('/')

@app.route('/delete_user/<int:id>')
def delete_user(id):
    User.delete(id)
    return redirect('/')
