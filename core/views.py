from django.shortcuts import render, redirect, get_object_or_404

from core.models import Contato


def add_contato(request):
   return render(request, 'core/add_contato.html')
def editarContato(request, id):
    contato = get_object_or_404(Contato,id=id)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        contato.nome = nome
        contato.sobrenome = sobrenome
        contato.email = email
        contato.telefone = telefone
        contato.save()
        return redirect('list_contato')
    context = {
        'contato': contato
    }
    return render(request, 'core/editarContato.html', context)