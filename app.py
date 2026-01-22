from flask import Flask, render_template

app = Flask(__name__)#Nombre del archivo 

@app.route('/index')
def index():
    return render_template('index.html')

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

@app.route("/operas")
def operas():
    return '''
                <form>
                    <label for="name">Name:</label> 
                    <input type="text" id="name" name="name" required>

                    <label for="name">Apaterno:</label> 
                    <input type="text" id="name" name="name" required>       
                </form>
            '''

if __name__ == '__main__':
    app.run(debug=True) #Aquí corremos todo el archivo y con el debug es para o tener que estar bajando y levantando el servidor 

