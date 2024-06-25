from flask import Flask, request, render_template, jsonify
import joblib
import pandas as pd
import logging


app = Flask(__name__)

# Configurar el registro
logging.basicConfig(level=logging.DEBUG)

# Cargar el modelo entrenado
model = joblib.load('modeloDGMental.pkl')
app.logger.debug('Modelo cargado correctamente.')

@app.route('/')
def home():
    return render_template('formulario.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obtener los datos enviados en el request
        euforia = float(request.form['Euphoric'])
        activida= float(request.form['Sexual'])
        optimismo =float(request.form['Optimisim'])
        humor= float(request.form['Mood'])
        pensamientos= float(request.form['Suicidal'])
        comportamiento= float(request.form['Ignore'])
        crisis= float(request.form['Nervous'])
        sobrepiensa= float(request.form['Overthinking'])

        
        # Crear un DataFrame con los datos
        data_df = pd.DataFrame([[euforia, activida,optimismo,humor,pensamientos,comportamiento,crisis,sobrepiensa]], columns=['Euphoric','Sexual Activity','Optimisim','Mood Swing_YES','Suicidal thoughts_YES','Ignore & Move-On_YES','Nervous Break-down_YES','Overthinking_YES'])
        app.logger.debug(f'DataFrame creado: {data_df}')
        
        # Realizar predicciones
        prediction = model.predict(data_df)
        app.logger.debug(f'Predicción: {prediction[0]}')
        
        # Devolver las predicciones como respuesta JSON
        return jsonify({'categoria': prediction[0]})
    
    except Exception as e:
        app.logger.error(f'Error en la predicción: {str(e)}')
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

