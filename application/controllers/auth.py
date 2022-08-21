from flask import Blueprint, render_template, request
from application.forms.login_form import LoginForm
from application.forms.register_form import RegisterForm
from application.helpers.general_helper import form_errors, is_ajax

controller = Blueprint('auth', __name__, url_prefix='/auth')


@controller.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and is_ajax(request):
        if form.validate_on_submit():
            pass
        else:
            return {
                'error': True,
                'form': True,
                'messages': form_errors(form)
            }
    return render_template('pages/auth/login.jinja2', form=form)


@controller.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and is_ajax(request):
        if form.validate_on_submit():
            pass
        else:
            return {
                'error': True,
                'form': True,
                'messages': form_errors(form)
            }
    return render_template("pages/auth/register.jinja2", form=form)

