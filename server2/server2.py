from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client, datetime

server = SimpleXMLRPCServer( ("0.0.0.0", 8889) )
clientServer1 = xmlrpc.client.ServerProxy("http://127.0.0.1:8888")

today = datetime.datetime.now()

def perintah_file(a,b):
    # perintah
    if a == "read":
        f = open("log.txt", 'r')
        return f.read()
        f.close()
    elif a == "unduh":
        f = open("log.txt", 'a')
        global counter
        f.write("\n[" + str(today.strftime("%d/%m/%y - %H:%M")) + "] " + "Gambar " + b + " telah diunduh.")
        f.close()
        return "OK"
    elif a == "reset":
        f = open("log.txt", 'w+')
        f.write("=== File aktivitas log server ===\n")
        f.close()
        return "OK"
    else:
        return "Input salah"

def unduhALL(a,b):
    clientServer1.file(a,b)
    return ""

def resetALL(a,b):
    clientServer1.file(a,b)
    return ""

server.register_function(perintah_file, "file2")
server.register_function(unduhALL, "unduhALL")
server.register_function(resetALL, "resetALL")


server.serve_forever()
