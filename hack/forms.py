from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,IntegerField, DateField
from wtforms.validators import DataRequired,Email,EqualTo, ValidationError,Length

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField("Log in")

class RawForm(FlaskForm):
    milk = IntegerField('Milk')
    sugar = IntegerField('Sugar')
    beans = IntegerField('Beans')
    submit = SubmitField("Enter")

class ManufactureForm(FlaskForm):
    milk = IntegerField('Milk',validators=[DataRequired()])
    sugar = IntegerField('Sugar',validators=[DataRequired()])
    beans = IntegerField('Beans',validators=[DataRequired()])
    defected = IntegerField('Defected',validators=[DataRequired()])
    perfect = IntegerField('Perfect',validators=[DataRequired()])
    submit = SubmitField("Enter")

class SellForm(FlaskForm):
    offline = IntegerField('Offline (D2C)',validators=[DataRequired()])
    online = IntegerField('Online (D2C)',validators=[DataRequired()])
    buisness = IntegerField('Buisness (B2B)',validators=[DataRequired()])
    submit = SubmitField("Enter")
