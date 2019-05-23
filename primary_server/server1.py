from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client, datetime

server = SimpleXMLRPCServer( ("0.0.0.0", 8888) )
clientServer2 = xmlrpc.client.ServerProxy("http://127.0.0.1:8889")
clientServer3 = xmlrpc.client.ServerProxy("http://127.0.0.1:8890")
clientServer4 = xmlrpc.client.ServerProxy("http://127.0.0.1:8891")

today = datetime.datetime.now()

def perintah_file(a,b):
    # perintah
    if a == "read":
        f = open("log.txt", 'r')
        return f.read()
        f.close()
    elif a == "unduh":
        f = open("log.txt", 'a')
        f.write("\n[" + str(today.strftime("%d/%m/%y - %H:%M")) + "] " + "Gambar " + b + " telah diunduh.")
        f.close()

        clientServer3.file3(a, b)
        clientServer4.file4(a, b)

        return "OK"
    elif a == "reset":
        f = open("log.txt", 'w+')
        f.write("=== File aktivitas log server ===\n")
        f.close()

        clientServer3.file3(a, b)
        clientServer4.file4(a, b)

        return "OK"
    else:
        return "Input salah"

server.register_function(perintah_file, "file")

server.serve_forever()
