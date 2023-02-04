from flask import Blueprint

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return "<h1>Test<h1>"

@views.route('/test')
def test():
    return "<h1>test<h1>"