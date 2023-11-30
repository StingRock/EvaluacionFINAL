from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None

    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros_pintura = int(request.form['tarros_pintura'])

        total_sin_descuento = tarros_pintura * 9000

        descuento = 0
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25

        total_con_descuento = total_sin_descuento - (total_sin_descuento * descuento)

        resultado = {
            'nombre': nombre,
            'total_sin_descuento': total_sin_descuento,
            'descuento': descuento * 100,
            'total_con_descuento': total_con_descuento
        }
    return render_template('ejercicio1.html', resultado=resultado)

##################################################################################################################

usuarios = {
    "juan": "admin",
    "pepe": "user"
}

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None

    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        if usuario in usuarios and usuarios[usuario] == contrasena:
            if usuario == "juan":
                mensaje = "Bienvenido administrador juan"
            elif usuario == "pepe":
                mensaje = "Bienvenido usuario pepe"
        else:
            mensaje = "Usuario o contreña incorrectos"

    return render_template('ejercicio2.html', mensaje=mensaje)

##################################################################################################################

if __name__ == '__main__':
    app.run(debug=True)