from application.models.user import User
from wtforms.validators import ValidationError


class UsernameExists:

    def __init__(self, model=User, exclude=None, message=None):
        self.model = model
        self.exclude = exclude
        if not message:
            message = "Username is already taken"
        self.message = message

    def __call__(self, form, field):
        user = self.model.query.filter_by(username=field.data)
        if not self.exclude:
            user.filter_by(id=self.exclude)
        if user.first():
            raise ValidationError(self.message)
