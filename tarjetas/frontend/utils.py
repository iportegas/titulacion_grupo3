import requests

class APIClient:
    @staticmethod
    def call_api(data):
        # URL de tu API
        api_url = "http://localhost/api/predecir_fraude/"
        print(data)
        
        try:
            # Realizar la solicitud POST
            response = requests.post(api_url, json=data)
            
            # Verificar el estado de la respuesta
            if response.status_code == 200:
                return response.json()  # Retorna los datos en formato JSON
            else:
                return {"error": f"Error en la API: {response.status_code}"}
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}