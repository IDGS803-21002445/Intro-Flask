from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField, Label
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    matricula = IntegerField('Matricula',[
                            validators.DataRequired(message="El campo es requerido"),
                            validators.NumberRange(min=2,max=100, message="Ingresa un valor valido")])
    nombre = StringField('nombre',[
                            validators.DataRequired(message="El campo es requerido"),
                            validators.Length(min=4,max=10, message="Ingresa un valor valido")])    
    apaterno = StringField('apaterno',[
                            validators.DataRequired(message="El campo es requerido"),
                            validators.Length(min=2,max=100, message="Ingresa un valor valido")])
    amaterno = StringField('amaterno',[
                            validators.DataRequired(message="El campo es requerido"),
                            validators.Length(min=2,max=100, message="Ingresa un valor valido")])
    correo = EmailField('correo',[
                            validators.Email(message="Ingrese un correo valido")])

