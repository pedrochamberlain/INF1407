# Programação para Web: Trabalho 2 – Implementando um Website em Django
Desenvolvido pelos alunos **Mark Ribeiro (1612043)** e **Pedro Chamberlain Matos (1710883)** para a matéria INF1407 – Programação para Web.

Domínio oficial do site: https://inf1407-moviedatabase.herokuapp.com/

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

## Arquivos 
- `moviedatabase/`: ...
- `movies/`: ...
- `manage.py`: ...
- `Pipfile`: ...
- `Procfile`: ...
- `requirements.txt`: ...
- `runtime.txt`: ...

## Como usar o site
1. Para acessar o site, acesse o [domínio principal da página](https://inf1407-moviedatabase.herokuapp.com/).
2. Antes de cadastrar filmes, registre sua conta na página principal.
3. Após registrar-se, faça login na sua conta na página principal.
4. Acesse a [página de cadastro de novo filme](https://inf1407-moviedatabase.herokuapp.com/movies/create/) para adicionar um filme a sua lista.
5. Após cadastrar um novo filme, você poderá encontrá-lo na [lista dos seus filmes](https://inf1407-moviedatabase.herokuapp.com/movies/list/).
6. Para ver a lista com todos os cadastros do site, confira a [página listando todos filmes do site](https://inf1407-moviedatabase.herokuapp.com/movies/list_all/)
