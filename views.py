from urllib import request
from django.shortcuts import render
import csv
from django.http import HttpResponse

# Create your views here.

def first(request):
    return render(request, 'page1.html')

def two(request):
    return render(request, 'page2.html')


def some_view(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="data.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(['1', 'A', '10'])
    writer.writerow(['2','B', '20'])

    return response
