from django.http import HttpResponse
from django.template import loader
from .models import TestExample

def test(request):
    fields = TestExample.objects.all().values()
    template = loader.get_template('all_fields.html')
    context = {
        'fields': fields,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    field = TestExample.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'field': field,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
