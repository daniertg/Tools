import socket

socket.setdefaulttimeout(1)

addr = "142.251.31.139"
daftar_port = [20, 21, 22, 23, 25, 53, 79, 80, 110, 137, 138, 139, 443, 3306]

for port in daftar_port:
    socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = socket_obj.connect_ex((addr, port))
    if result == 0:
        print("Port terbuka: " + str(port))
    else:
        print("Port tertutup: " + str(port))
    socket_obj.close()
