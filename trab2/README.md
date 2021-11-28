# Programação para Web: Trabalho 2 – Implementando um Website em Django
Desenvolvido pelos alunos **Mark Ribeiro (1612043)** e **Pedro Chamberlain Matos (1710883)** para a matéria INF1407 – Programação para Web.

Domínio oficial do site: https://inf1407-moviedatabase.herokuapp.com/

## Sobre o site

O website a ser implementado nesta disciplina é o **Movie Database**. O Movie Database é um portal voltado para usuários que desejam cadastrar/logar filmes que eles já assistiram, podendo conferir uma lista pessoal de filmes, assim como valores relacionados a eles, como por exemplo:
- Título
- Ano de lançamento
- Diretor
- Gênero
- País de Origem
- Duração (em min)

Os usuários poderão, também, conferir os filmes que outras pessoas cadastraram no portal, numa página que exibe a lista completa de filmes da base de dados do site.

Os usuários possuirão acesso a quatro páginas:
1. Uma página para cadastrar novos filmes
2. Uma página para editar filmes anteriormente cadastrados
3. Uma página para conferir seus filmes cadastrados
4. Uma página para conferir todos filmes cadastrados no site, podendo conferir o que cada usuário cadastrou.

## Manual de usuário: Como usar o site
1. Para acessar o site, acesse o [domínio principal da página](https://inf1407-moviedatabase.herokuapp.com/).
2. Antes de cadastrar filmes, registre sua conta na página principal.
3. Após registrar-se, faça login na sua conta na página principal.
4. Acesse a [página de cadastro de novo filme](https://inf1407-moviedatabase.herokuapp.com/movies/create/) para adicionar um filme a sua lista.
5. Após cadastrar um novo filme, você poderá encontrá-lo na [lista dos seus filmes](https://inf1407-moviedatabase.herokuapp.com/movies/list/).
6. Caso você deseje editar um filme já cadastrado, acesse a [sua lista de filmes](https://inf1407-moviedatabase.herokuapp.com/movies/list/) e clique o botão `Editar` ao lado do filme desejado. 
7. Caso você queira deletar um filme cadastrado, acesse [sua lista de filmes](https://inf1407-moviedatabase.herokuapp.com/movies/list/) e clique o botão `Deletar` ao lado do filme desejado.
8. Para ver a lista com todos os filmes cadastrados do site, confira a [página listando todos filmes do site](https://inf1407-moviedatabase.herokuapp.com/movies/list_all/). Cada filme terá suas características listados e o respectivo usuário que o cadastrou.

## Arquivos do repositório
- `moviedatabase/`: Pasta principal do projeto Django.

  - `moviedatabase/`: Pasta para configuração do acesso de contas do site, templates, views e a configuração de diretórios do domínio principal.
  
    - `templates/`: Pasta com os templates HTML utilizadas na página inicial, de cadastro e login do site. 
      - `index.html`: Página inicial do site.
      - `login.html`: Página de login do site.
      - `register.html`: Página de cadastro de conta do site.
    - `static/`: Pasta com a configuração completa do CSS do site. 
    - `settings.py`: Configurações técnicas gerais do projeto, como a configuração do database.
    - `urls.py`:  Configuração dos diretórios dos domínio do site relacionados ao acesso de conta.
    - `views.py`:  Configuração das funções do site que recebem requisições HTTP e retornam respostas.
    - `wsgi.py`: Especificação para deploy do site.
    
  - `movies/`: Pasta para configuração do modelo `Filme` e operações CRUD relacionadas a ele, assim como templates, views e a configuração de subdiretórios `/movies/*` do domínio.
  
    - `templates/`: Pasta com os templates HTML utilizadas na adição, atualização e listagem individual e completa dos filmes da database do site. 
    
      - `add_movie.html`: Página de cadastro de um filme.
      - `edit_movie.html`: Página de edição das características de um filme. Só pode ser editado pelo usuário que o cadastrou.
      - `list_movies.html`: Página que lista todos os filmes da database do site cadastrados pelo usuário logado.
      - `list_all_movies.html`: Página que lista todos os filmes da database do site.
    - `models.py`: Configuração do modelo `Filme`.
    - `form.py`: Form do modelo `Filme`.
    - `urls.py`:  Configuração dos diretórios dos domínio do site vinculados às operações de filmes.
    - `views.py`:  Configuração das funções do site que recebem requisições HTTP e operações CRUD para os filmes.
    - `apps.py`:  Configuração da aplicação `movies` do site (Não foi configurada).
    
  - `manage.py`: Um utilitário de linha de comando que permite a interação com o projeto Django.
  - `Pipfile`: Arquivo que especifica os requerimentos de biblioteca do projeto.
  - `Procfile`: Configuração de deploy do Heroku.
  - `requirements.txt`: Arquivo que especifica os requerimentos de biblioteca do projeto.
  - `runtime.txt`: Configuração de linguagem utilizada para o deploy do Heroku. Foi utilizada para criar o arquivo `Pipfile`.

## O que foi feito
- Foi elaborado um site em Python + Django, HTML e CSS.
- - O site contém operações de login, acesso e ações selecionadas por usuário. Cada usuário possui uma visão diferente da página de listagem de filmes pessoalmente cadastrados.
- O site contém as quatro operações básicas em banco de dados (CRUD) com o modelo de `Filme`.
- O site foi publicado em um provedor de serviço Web (Heroku).
- O git foi utilizado para o controle de versão do site, sendo armazenado neste repositório público.
- Commits foram publicados semanalmente durante o desenvolvimento do projeto.
- Javascript e requisições AJAX não foram desenvolvidas para o projeto.
