from django.shortcuts import render,redirect
from .forms import *
from .models import Professor
from django.contrib.auth.decorators import login_required


def home(request):
#    horario = Atendimento_Aluno.objects.all()
    return render(request, 'home.html')


#manda informações pro template professor
@login_required
def professor(request):
    hora = Professor.objects.all()
    return render(request, 'professor.html',{'hora': hora})

@login_required
def cadastrar_horario(request):
    Mhora = Horariodisponivel(request.POST or None)
    if Mhora.is_valid():
        Mhora.save()
        return redirect(home)

    return render(request, 'cadastrar_horario.html', {'Mhora': Mhora})

@login_required
def alterar(request, id):
    marcar = Professor.objects.get(id=id)
    Mhora = Horariodisponivel(request.POST or None,instance=marcar)
    if Mhora.is_valid():
        Mhora.save()
        return redirect(home)

    return render(request, 'cadastrar_horario.html', {'Mhora': Mhora, 'marcar':marcar})

@login_required
def deletar(request, id):
    cadastrado = Professor.objects.get(id=id)
    if request.method == 'POST':
        cadastrado.delete()
        return redirect(home)

    return render(request, 'deletar.html', {'cadastrado': cadastrado})

######################################################################

#@login_required
#def horario(request):
#    horaM = Marcarhorario(request.POST or None)
#    if horaM.is_valid():
#        horaM.save()
#        return redirect(home)
#
#    return render(request, 'horario.html', {'horaM': horaM})


#@login_required
#def marcar_horario(request):
#    Mhras = Atendimento_Aluno.objects.all()
#    return render(request, 'horarios_marc.html', {'Mhras': Mhras})
#
#
#@login_required
#def deletarH(request, id):
#    cadastrado = Atendimento_Aluno.objects.get(id=id)
#    if request.method == 'POST':
#        cadastrado.delete()
#        return redirect(home)
#
#    return render(request, 'deletarH.html', {'cadastrado': cadastrado})


######################################################################################################3

##manda informações pro template aluno
#def aluno(request):
#    hora = Professor.objects.all()
#    return render(request, 'aluno.html',{'hora': hora})
#
##comentario
#def agenda_hora(request):
#    agendaH = Agendarhorario(request.POST or None)
#    if agendaH.is_valid():
#        agendaH.save()
#        return redirect(home)
#
#    return render(request, 'agenda_hora.html', {'agendaH': agendaH})
#
#
#def deletar_comentario(request, id):
#    cadastrado = Aluno.objects.get(id=id)
#    if request.method == 'POST':
#        cadastrado.delete()
#        return redirect(home)
#
#    return render(request, 'deletarC.html', {'cadastrado': cadastrado})
#
#
#def alterar_comentario(request, id):
#    agenda = Aluno.objects.get(id=id)
#    agendaH = Agendarhorario(request.POST or None, instance=agenda)
#    if agendaH.is_valid():
#        agendaH.save()
#        return redirect(home)
#    return render(request, 'agenda_hora.html', {'agendaH': agendaH, 'agenda': agenda})
#
#
#def comentarios(request):
#    hora = Aluno.objects.all()
#    return render(request, 'comentarios.html', {'hora': hora})
#
########################################################################################
#
#
#
## colocar um bUtao so para o professor clica e ir o atendimento marcado e ir para a home
## o aluno so tem que clicar para ter o atendimento
#
#
#
#
#