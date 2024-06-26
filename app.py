from flask import Flask, request, render_template, jsonify
import joblib
import pandas as pd
import logging



app = Flask(__name__)

# Configurar el registro
logging.basicConfig(level=logging.DEBUG)

# Cargar el modelo entrenado
model = joblib.load('modeloRf93.pkl')
scaler = joblib.load('dataFrameScalado.pkl')
app.logger.debug('Modelo cargado correctamente.')

@app.route('/')
def home():
    return render_template('formulario.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obtener los datos enviados en el request
        calificacion = float(request.form['calificacion'])
        precioMedio= float(request.form['precioMedio'])
        precioProducto =float(request.form['precioProducto'])
        puntuacion =float(request.form['puntuacion'])

        data = pd.DataFrame({
            'Number of clicks on similar products': [0],
            'Number of similar products purchased so far': [0],
            'Average rating given to similar products': [calificacion],
            'Median purchasing price (in rupees)': [precioMedio],
            'Rating of the product': [0],
            'Brand of the product': [0],
            'Customer review sentiment score (overall)': [puntuacion],
            'Price of the product': [precioProducto],
            'Season': [0],
            'Geographical locations': [0],
            'Holiday_No': [0],
            'Holiday_Yes': [0],
            'Gender_female': [0],
            'Gender_male':[0]
        })


        scaled_data = scaler.transform(data)
        scaled_data_for_prediction = scaled_data[:, [2,3,6,7]]

        prediccion = model.predict(scaled_data_for_prediction)

        resultado = round(float(prediccion[0]), 2)

        return jsonify({'prediction': resultado})
     
    except Exception as e:
        app.logger.error(f'Error en la predicción: {str(e)}')
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

