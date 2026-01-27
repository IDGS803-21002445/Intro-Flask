from flask import Flask, render_template, request
from flask import flash #Para
from flask_wtf.csrf import CSRFProtect #Para los tokens
import forms
#jinja jinja2 es el motor de parámetros
app = Flask(__name__)#Nombre del archivo 

app.secret_key='clave secreta' #Se le envía al formulario para verificar que es quien dice ser o sea tú o tu app
csrf=CSRFProtect()
@app.route('/')
def index():
    titulo = "IDGS803-FLASK"
    lista = ['pedro', 'mario','juan']
    return render_template('index.html', titulo=titulo,lista=lista)

@app.route("/usuarios", methods=['GET','POST'])
def usuario():
    mat = 0
    nom=''
    apa=''
    ama=''
    correo=''

    usuario_class=forms.UserForm(request.form)
    print(usuario_class.data)
    if request.method=='POST' and usuario_class.validate():
        mat = usuario_class.matricula.data
        nom = usuario_class.nombre.data
        apa = usuario_class.apaterno.data
        ama = usuario_class.apaterno.data
        correo = usuario_class.correo.data
    return render_template('usuarios.html', form=usuario_class, mat = mat, nom=nom, apa = apa, ama= ama, correo=correo )

# @app.route('/usuarios')
# def usuarios():
#     titulo = "IDGS803-FLASK USUARIOS"
#     lista = ['usuario 1', 'usuario 2','usuario 3']
#     return render_template('usuarios.html', titulo=titulo,lista=lista)

@app.route('/alumnos')
def alumnos():
    titulo = "IDGS803-FLASK ALUMNOS"
    lista = ['alumno 1', 'alumno 2','alumno 3']
    return render_template('alumnos.html', titulo=titulo,lista=lista)

@app.route("/operasbas", methods=['GET','POST'])
def operas():
    res = 0
    if request.method == 'POST':
        n1 = request.form.get('n1')
        n2 = request.form.get('n2')
        
        if request.form.get('operacion')=='sumar':
            res = float(n1) + float(n2)
        elif request.form.get('operacion')=='mutiplicar':
            res = float(n1) * float(n2)
        elif request.form.get('operacion')=='restar':
            res = float(n1) - float(n2)
        elif request.form.get('operacion')=='dividir':
            res = float(n1) / float(n2)

    return render_template('operasBas.html',resultado=res)

# @app.route("/resultado", methods=['GET','POST'])
# def resultado():
#     operas()
#     return render_template('operasBas.html')
    

@app.route('/hola')
def hola():
    return "Hello, hola!"

@app.route("/user/<string:user>")
def user(user):
    return f"Hello, {user}"

@app.route("/numero/<int:n>")
def numero(n):
    return f"El número es:,{n}"

@app.route("/username/<int:id>/<string:Username>")
def nombrenumero(id,Username):
    return f"<h1> El número es:,{Username}, Tu ID es: {id}</h1>"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return f"La suma es: {n1+n2}"

@app.route("/default/")
@app.route("/default/<string:param>")
def default(param="Juan"):
    return f"<h1> Hola,{param}, </h1>"

# @app.route("/operas")
# def operas():
#     return '''
#                 <form>
#                     <label for="name">Name:</label> 
#                     <input type="text" id="name" name="name" required>

#                     <label for="name">Apaterno:</label> 
#                     <input type="text" id="name" name="name" required>       
#                 </form>
#             '''

if __name__ == '__main__':
    app.run(debug=True) #Aquí corremos todo el archivo y con el debug es para o tener que estar bajando y levantando el servidor 
    csrf.init_app(app)
