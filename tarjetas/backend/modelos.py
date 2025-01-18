import os
import pickle
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
encoders_path = os.path.join(BASE_DIR, 'encoders_4.pkl')
dt_path = os.path.join(BASE_DIR, 'modelo_dt.pkl')
rf_path = os.path.join(BASE_DIR, 'modelo_rf.pkl')
gb_path = os.path.join(BASE_DIR, 'modelo_gb.pkl')

# Cargar los encoders
with open(encoders_path, 'rb') as f:
    encoders = pickle.load(f)


# Verificar las columnas y clases de los encoders
#print("Columnas con encoders y sus clases:")
#for column, encoder in encoders.items():
    #if hasattr(encoder, 'classes_'):  # Verificar si el encoder tiene clases
        #print(f"Columna: {column}, Número de clases: {len(encoder.classes_)}, Clases: {encoder.classes_}")
    #else:
        #print(f"Columna: {column}, El encoder no tiene clases")

# Cargar los modelos
with open(dt_path, 'rb') as f:
    modelo_dt = pickle.load(f)
with open(rf_path, 'rb') as f:
    modelo_rf = pickle.load(f)
with open(gb_path, 'rb') as f:
    modelo_gb = pickle.load(f)




def prediccion(data):
    for column, encoder in encoders.items():
        if hasattr(encoder, 'classes_'):  
            print(f"Columna: {column}, Longitud: {len(encoder.classes_)}")
        else:
            print(f"Columna: {column}, Longitud: No disponible (El encoder no tiene 'classes_')")

    data = {key: [value] for key, value in data.items()}  # Convertir valores escalares en listas
    data = pd.DataFrame(data)
    print(data)
    
# Transformar las columnas categóricas
    for column in ['category', 'city', 'state', 'profession_group']:
        if column in encoders:
            encoder = encoders[column]
            try:
                data[column] = encoder.transform(data[column])
            except ValueError as e:
                print(f"Error al transformar la columna '{column}': {e}")
                print(f"Valores no reconocidos en '{column}': {set(data[column]) - set(encoder.classes_)}")



    # Seleccionar las columnas relevantes para los modelos
    columnas_modelo = [
        'category', 'amt', 'city', 'state', 'age', 'transaction_hour',
        'transaction_day_of_month', 'transaction_day_of_week', 
        'profession_group', 'fraud_category_merchant'
    ]
    #X_prueba = data_prueba[columnas_modelo]
    X_prueba = data[columnas_modelo]
    print(X_prueba)

    # Realizar predicciones con cada modelo
    pred_dt = modelo_dt.predict(X_prueba)
    pred_rf = modelo_rf.predict(X_prueba)
    pred_gb = modelo_gb.predict(X_prueba)

    # Mostrar resultados
    print("Predicción Decision Tree:", pred_dt)
    print("Predicción Random Forest:", pred_rf)
    print("Predicción Gradient Boosting:", pred_gb)
    return pred_dt,pred_rf,pred_gb