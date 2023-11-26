from django.http import HttpResponse

def home(Request):
        return HttpResponse("this is home")
def contact(Request):
        return HttpResponse("This is contact page")