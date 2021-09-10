import threading

from sys import argv, exit
from socket import socket, AF_INET, SOCK_STREAM

def client_request(connection, client):
    # Recebe mensagem recebida do socket

    message = connection.recv(32768)
    message = message.decode('iso-8859-1')
    
    if not message:
        # Nenhuma mensagem foi recebida do socket, fechando requisição
   
        connection.close()
        return

    print(message)

    # Request recebe a primeira linha da requisição
   
    request = message.splitlines()[0]

    # Separa método, caminho do arquivo e protocolo HTTP
   
    method, archive_path, protocol = request.split(' ')

    if (method != 'GET'):
        # Se o método não for GET, avisa ao usuário que o método não é suportado pelo servidor
        
        body=''
        status_code='501'
        status_text='METHOD NOT SUPORTED'

    else:
        print(f'Tentando abrir {archive_path}...\n')
        try:
            if archive_path == '/':
                # Se não receber requisição de arquivo, envia arquivo padrão
             
                with open('./index.html','rb') as f:
                    body=f.read()
            else:
                # Se receber requisição de arquivo e encontrá-lo, envia arquivo selecionado
               
                with open(archive_path[1:],'rb') as f:
                    body=f.read()
            status_code='200'
            status_text='OK'

        except FileNotFoundError:
            # Se o arquivo não for encontrado, envia página 404
            
            with open('notfound.html','rb') as f:
                    body=f.read()
            status_code='404'
            status_text='FILE NOT FOUND'

        except OSError:
            # Avisa erro de sistema operacional
            
            body=''
            status_code='500'
            status_text='FAILED OPENING FILE'

        except UnicodeDecodeError:
            # Avisa erro de decodificação
            
            body=''
            status_code='500'
            status_text='FAILED OPENING FILE'

    response_header = [
        f'Content-Length: {len(body)}',
        f'Connection: close'
    ]

    connection.send((f'HTTP/1.1 {status_code} {status_text}').encode('iso-8859-1'))
    connection.send(''.join(response_header).encode('iso-8859-1'))
    connection.send('\n\n'.encode('iso-8859-1'))
    connection.send(body)

    print(f'{status_text}\n')

    connection.close()

if __name__ == '__main__':
    # Escolhe uma porta do servidor

    if len(argv) >= 2:
        server_port = argv[1]
    else:
        server_port = 8080

    # Cria um socket do servidor sem cliente
    
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.bind(('', int(server_port)))
    tcp_socket.listen(0)

    print(f'Acesse o servidor no endereço localhost:{server_port}')

    while True:
        # Programa aguarda por uma conexão
        # Ao receber uma conexão, retorna um socket com cliente, servidor e o endereço do cliente

        connection, client = tcp_socket.accept()
        new_thread = threading.Thread(group=None, target=client_request, args=(connection, client))
        new_thread.start()