from xmlrpc.server import SimpleXMLRPCServer
import datetime

server = SimpleXMLRPCServer( ("0.0.0.0", 8891) )

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

server.register_function(perintah_file, "file4")

server.serve_forever()
