# Programação para Web: Trabalho 1 – Implementando um Servidor Web
Desenvolvido pelos alunos **Mark Ribeiro (1612043)** e **Pedro Chamberlain Matos (1710883)** para a matéria INF1407 – Programação para Web.

## Arquivos 
- `server.py`: Arquivo escrito em Python com a implementação do Servidor Web.
- `config.py`: Arquivo escrito em Python com as configurações do servidor.
- `index.html`: Página inicial do servidor.
- `notfound.html`: Página que o servidor retorna ao ter erro 404.
- `favicon.ico`: Ícone que aparece na aba das páginas criadas para o projeto.
- `README.md`: O relatório do projeto.

## Como usar o servidor Web

1. [Baixe o projeto.](https://github.com/pedrochamberlain/INF1407/archive/refs/heads/main.zip)
2. Acesse a pasta `trab1/` pela linha de comando.
3. Rode o seguinte comando para inicializar o servidor:
```zsh
python3 server.py
```
4. Acesse a [página inicial do servidor](http://localhost:8080/) no seu navegador.

Com o servidor inicializado, você pode fazer requisições para todos os arquivos (HTML, JS, JPEG, PNG e GIF) inclusos dentro da pasta `trab1/`.

## O que foi feito

- Foi implementado um servidor Web no arquivo `server.py`.
- As configurações do servidor Web foram definidas no arquivo `config.py`.
- O servidor Web implementado escuta a porta 8080.
- O método GET foi implementado e retorna arquivos HTML, JS, JPEG (JPG), PNG e GIF que estejam presentes dentro da pasta do servidor. (Ex.: `http://localhost:8080/favicon.ico`) 
- Em caso de um erro 404 numa requisição com método GET, a página `notfound.html` será exibida.
- Caso o servidor receba uma requisição com um método que não seja GET, ele retornará um erro.
- O código foi comentado para que o professor tenha entendimento de como ele funciona.
- O servidor permite conexões simultâneas, permitindo o uso dele por mais de um usuário ao mesmo tempo.

## O que não foi feito

- Nós não conseguimos testar as classes de erro `OSError` e `UnicodeDecodeError` com o servidor.
- A parte de segurança não foi implementada.
- A parte de interpretação de scripts não foi implementada.
