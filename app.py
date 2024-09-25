from flask import Flask, render_template

# Inicializar la aplicación Flask
app = Flask(__name__)

# Ruta para la raíz, va a index.html
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para el index en español
@app.route('/ES')
def index_es():
    return render_template('index.html')

# Ruta para el index en inglés
@app.route('/EN')
def index_en():
    return render_template('en-index.html')

@app.route('/ES/route_to')
def long_es():
    return render_template('long.html')

@app.route('/EN/route_to')
def long_en():
    return render_template('en_long.html')

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
