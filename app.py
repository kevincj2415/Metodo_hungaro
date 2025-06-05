from flask import Flask, render_template, request
from hungaro import algoritmo_hungaro

app = Flask(__name__)

status = {}

# Rutas de Flask
@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/datos_1')
def Datos1():
    return render_template('datos_1.html')

@app.route('/datos_2', methods=['POST'])
def Datos2():
    global status
    status['trabajadores'] = int(request.form['trabajadores'])
    status['tareas'] = int(request.form['tareas'])
    return render_template('datos_3.html', trabajadores=status['trabajadores'], tareas=status['tareas'])

@app.route('/datos_3', methods=['POST'])
def Datos3():
    global status
    return render_template('datos_3.html', puntos=status['trabajadores'], almacenes=status['tareas'])

@app.route('/datos_4', methods=['POST'])
def Datos4():
    global status
    status['costes'] = [] 
    for i in range(status['trabajadores']):
        ayuda = [] 
        for o in range(status['tareas']):
            precio = int(request.form[f'coste_{i+1}_{o+1}'])
            ayuda.append(precio)
        status['costes'].append(ayuda)
    return render_template('tabla.html', status=status)

@app.route('/solucionar', methods=['POST'])
def solucionar():
    global status
    
    asignaciones, costo_total = algoritmo_hungaro(status['costes'])

    
    return render_template(
        'resultado.html',
        status=status,
        asignaciones=asignaciones,
        costo_total=costo_total
    )

if __name__ == '__main__':
    app.run(debug=True)