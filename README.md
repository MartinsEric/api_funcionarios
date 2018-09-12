# api_funcionarios

A API foi criada usando o framework django e o django-rest-framework. 

Por isso, precisam ser feitas algumas configurações para rodar o projeto localmente.

## Como rodar o projeto localmente:
**1.** Abra o prompt de comando.

**2.** Entre na pasta do projeto (...\api_funcionarios-master\).

**3.** Agora precisamos criar uma VirtualEnv com o comando `python -m venv venv`.

**4.** Faça `cd venv/Scripts` para entrar na pasta Scripts da venv e use o comando `activate`.

**5.** Use o comando `cd ..` 2 vezes para voltar pra pasta do projeto.

**6.** Instale o django usando o comando `pip install django`.

**7.** Agora instale o django rest framework usando `pip install djangorestframework`.

**8.** Execute `pip install django-rest-swagger`.

**9.** Por fim, execute `python manage.py runserver` para rodar o servidor.

**OBS: Esses são os passos a serem seguidos quando baixarem o projeto pela primeira vez.
Quando forem utilizá-lo de novo, só será necessário seguir os passos 1, 2, 4, 5 e 9.**


## Consumindo a API localmente:

**GET.** http://localhost:8000/funcionarios/

**GET.** http://localhost:8000/funcionarios/{id}/

**POST.** http://localhost:8000/funcionarios/

**PUT.** http://localhost:8000/funcionarios/{id}/

**DELETE.** http://localhost:8000/funcionarios/{id}/

**Quando qualquer ação é realizada, logs são registrados num arquivo dentro da pasta projeto no caminho ...\api_funcionarios-master\api_funcionarios\static\logging**

**OBS: O django-rest-framework fornece uma interface no browser para testar a API. Caso não queiram usa-la, 
qualquer programa usado para testar API's pode ser usado.**

