# Importa a Função render da biblioteca django.shortcuts 
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Retorna a pagina template index.html e renderiza
def index(request):
    return render(request,'estrutura/mainContent.html')

def cad(request):
    return render(request,'acesso/cadastro.html')

def ciee(request):
    return render(request,'bancas/ciee.html')

def fuvest(request):
    return render(request,'bancas/fuvest.html')

def cebraspe(request):
    return render(request,'bancas/cebraspe.html')

def fgv(request):
    return render(request,'bancas/fgv.html')

def contato(request):
    return render(request,'info/contato.html')

def sobre(request):
    return render(request,'info/sobre.html')

def telaLogin(request):
    return render(request, 'acesso/telaLogin.html')

# Esta Função verifica no banco de as senhas digitadas são iguais no caso password e password-conf
def store(request):
    # Data é um dicionario.
    data = {}
    # Condição que faz a validação se a senha é gual ou não, se a condição aceita for o if significa que as senhas são diferentes senão as informações são gravadas na variavel user para serem enviadas para o banco de dados e é exibido a mensagen de usuario cadastrado
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'As senhas não são iguais!'
        data['class'] = 'alert-danger'
    else: 
        # A variavel user armazena as informações dos posts 
        
        #TODO - Validar informações que ja existem no banco para que não possa ocorrer dulicidade, está ocorendo erro na criação de usuarios identicos e exibe informações sensiveis do framework.
        
        user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        # Salva no banco de dados.
        user.save()
        # Define permições para os usuarios no sistema.
        ## user.user_permissions.add((ex: 27,53,1,5,9))
        data['msg'] = 'Usuário cadastrado com sucesso!'
        data['class'] = 'alert-success'
    return render(request,'cadastro.html',data)

# Autenticação de credenciais para validação de login.
def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    
    # Condição que valida se o usuário está logado out não.
    if user is not None:
        login(request, user)
        return redirect(index)
    else:
        # Se a condição de logado não for atendido é exibido uma mensagem para realizar o login novamente e é renderizada a pagina de login novamente.
        data['msg'] = 'Nome de Usuário ou senha inválidos!'
        data['class'] = 'alert-danger'
        return render(request, 'telaLogin.html', data)

# Chama o arquivo telaLogin.html para renderizar na tela indicando que a seção foi encerrada.
def logouts(request):

    # Função para elinimar a seção, remove as informações de login.
    logout(request)
    # Retorna o usuario para a tela de login
    return redirect('/telaLogin/')

# Define a criação de uma rota para a redefinicção de senha.
def changePassword(request):
    # Variavel que recebe as informações do usuario para redefinir a senha.
    user = User.objects.get(email=request.user.email)
    ############ Criar formulario de troca de senha
    user.set_password(request.POST['resetPpassword'])
    user.save()
    logout(request)
    return redirect('/painel/')


