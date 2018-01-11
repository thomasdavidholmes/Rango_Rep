from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse("""<html><head><title>About</title><head><body>
            <h1>What does Rango say </h1>
        Rango says some shite <a href="/rango/">Index</a>
        </body>
    </html>
    """)