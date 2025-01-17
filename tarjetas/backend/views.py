from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from backend.modelos import prediccion

@api_view(['POST'])
def predecir_fraude(request):
    # Recibir datos del POST
    data = {
        'category': request.data.get('category'),
        'amt': request.data.get('amt'),
        'city': request.data.get('city'),
        'state': request.data.get('state'),
        'age': request.data.get('age'),
        'transaction_hour': request.data.get('transaction_hour'),
        'transaction_day_of_month': request.data.get('transaction_day_of_month'),
        'transaction_day_of_week': request.data.get('transaction_day_of_week'),
        'profession_group': request.data.get('profession_group'),
        'fraud_category_merchant': request.data.get('fraud_category_merchant'),
    }
    
    
    pred_dt,pred_rf,pred_gb=prediccion(data)
    fraude_dt=pred_dt[0]
    fraude_rf=pred_rf[0]
    fraude_gb=pred_gb[0]

    # Retornar los resultados de los tres modelos
    return Response({'decision_tree': fraude_dt, 'random_forest': fraude_rf, 'gradient_boosting': fraude_gb})
