from django.shortcuts import render,redirect
from django.http import JsonResponse
# from .main import ProcessQuery
from .scrap import WebScraper
# from .build import vectorBuilder
import requests



# Create your views here.

def index(request):
    return render(request, 'index.html')



def process_form(request):


    if request.method == 'POST':
        form_data = request.POST.get('name')
        obj = ProcessQuery()
        get_answer = obj.start_processing(form_data)
        print(get_answer)
        return JsonResponse({'data': get_answer})
    else:
        return JsonResponse({'error': 'Invalid request method'})


def scrap_view(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        response = requests.get(url)
        scraper = WebScraper(url)
        scraper.save_to_json('data.txt')
        vector_builder = vectorBuilder()
        vector_builder.build()
        return JsonResponse({'status': 'success'})

    return JsonResponse({'error': 'Invalid request method'})










