from django.http import HttpResponse

# create your view here
def home_page_view(request):
    return HttpResponse('My name is Asogwa Chika Godson, i built my first django project on 24/04/2021; hellow world app in django, I will continue to improve until the whole world get to here about me.')