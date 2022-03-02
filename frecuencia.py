from distutils.log import debug
from flask import Flask
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/Megahertz/<string:frecuencia>")
def get_datosD(frecuencia):
    velocidadLuz = 300000000
    frecuencia = float(frecuencia)
    longitudOnda = velocidadLuz/frecuencia
    return jsonify({ "longitud de onda" : longitudOnda})


@app.route("/masa/<string:densidad>/<string:volumen>")
def get_datosM(volumen,densidad):
    volumen = float(volumen)
    densidad = float(densidad)
    masa = volumen*densidad
    return jsonify({ "masa" : masa})

@app.route("/volumen/<string:densidad>/<string:masa>")
def get_datosV(masa,densidad):
    masa = float(masa)
    densidad = float(densidad)
    volumen = masa/densidad
    return jsonify({ "volumen" : volumen})


if __name__ == '_main_':
    app.run(debug=True, port=4000)