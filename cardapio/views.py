from django.shortcuts import render

# Create your views here.

def index(request):

	return render(request, 'cardapio/cardapio.html', {'dados': [1,2,3,4,5,6,7,8,9,0]})
