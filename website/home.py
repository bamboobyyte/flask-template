from flask import Blueprint, request, render_template

home = Blueprint('home', __name__)

@home.route('/', methods=['GET', 'POST'])
def root():
    title = 'home'
    return render_template('home.html', title=title)