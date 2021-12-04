import socket
import ssl
import pyperclip
import winsound

server = 'irc.chat.twitch.tv'
port = 6697
username = '{USERNAME IN ALL LOWERCASE}'
token = 'oauth:{OAUTH TOKEN}'
channel = '#summit1g'
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS)
sock = socket.socket()
s_sock = ctx.wrap_socket(sock, server_hostname=server)
s_sock.connect((server, port))


s_sock.send(f"PASS {token}\n".encode('utf-8'))
s_sock.send(f"NICK {username}\n".encode('utf-8'))
s_sock.send(f"JOIN {channel}\n".encode('utf-8'))

while True:
    data = s_sock.recv(2048).decode('ascii', 'ignore')
    if ( len(data) < 1 ) :
        break
    if username in data: 
        print(data)
    elif data.startswith(':gamepasshaspcgames'):
        print(data)
        sstr = data.split(" ")
        if len(sstr[-2]) == 29:
            winsound.Beep(2000, 500)
            print(f'New code!: {sstr[-2]}')
            pyperclip.copy(sstr[-2])
    
s_sock.close()
