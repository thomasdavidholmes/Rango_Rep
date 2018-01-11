from django.http import HttpResponse


def index(request):
    return HttpResponse("Rango says hey there partner! <br/><a href='/rango/about/'>About</a>")

def about(request):
    return HttpResponse("""<html><head><title>About</title><head><body>
            <h1>What does Rango say </h1>
        Rango says some shite <a href="/rango/">Index</a>
        </body>
    </html>
    """)