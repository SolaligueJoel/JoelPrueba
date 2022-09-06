from django.shortcuts import render
from ejemplo.models import Familiar

def familiar(request):
	familiar_uno = Familiar(nombre='Carolina',edad=49)
	familiar_dos = Familiar(nombre='Victor',edad=49)
	familiar_tres = Familiar(nombre='Dulcinea',edad=20)

	familiar_uno.save()
	familiar_dos.save()
	familiar_tres.save()

	context = Familiar.objects.all()

	return render(request, 'ejemplo/mostrar_familia.html', {'context':context})
