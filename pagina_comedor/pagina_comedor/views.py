from django.http import HttpResponse
from django.template import Template,context
from django.template.loader import get_template
def saludo(request):
    doc_externo=get_template('index.html')
    documento=doc_externo.render()
    return HttpResponse(documento)

