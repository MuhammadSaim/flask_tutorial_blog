from flask import Blueprint, render_template

controller = Blueprint('home', __name__)

@controller.route('/', methods=['GET'])
def index():
    return "Home Controller"