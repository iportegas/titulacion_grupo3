from django.shortcuts import render
from django.http import JsonResponse
from .utils import APIClient
from .listas import *
from statistics import mode

def predecir(request):
    if request.method == "POST":
        # Obtener los datos del formulario
        data = {
            'category': request.POST.get('category'),
            'amt': request.POST.get('amt'),
            'city': request.POST.get('city'),
            'state': request.POST.get('state'),
            'age': request.POST.get('age'),
            'transaction_hour': request.POST.get('transaction_hour'),
            'transaction_day_of_month': request.POST.get('transaction_day_of_month'),
            'transaction_day_of_week': request.POST.get('transaction_day_of_week'),
            'profession_group': request.POST.get('profession_group'),
            'fraud_category_merchant': request.POST.get('fraud_category_merchant'),
        }
        
        # Llamar a la API utilizando la clase APIClient
        api_response = APIClient.call_api(data)

        fraude_dt=api_response['decision_tree']
        fraude_rf=api_response['random_forest']
        fraude_gb=api_response['gradient_boosting']

        fraudes=[fraude_dt,fraude_rf,fraude_gb]
        moda = mode(fraudes)
        fraude_total=moda         

        # Redirigir al template resultado.html con un mensaje
        return render(request, 'resultado.html', {'mensaje': 'Formulario enviado correctamente', 'data': data,'fraude_dt':fraude_dt,
                                                  'fraude_rf':fraude_rf,'fraude_gb':fraude_gb,'fraude_total':fraude_total
                                                  })
        
    else:
        # Si no es POST, muestra un formulario vacío
        
        return render(request, 'predecir_form.html',{'category_lista':category_lista,'city_lista':city_lista,
                                                  'state_lista':state_lista,'profession_lista':profession_lista, 'state_city_dict': state_city_dict} )