import xmlrpc.client, os

client = xmlrpc.client.ServerProxy("http://127.0.0.1:8889")

a = input("Masukkan perintah : ")

if a == "unduh":
    print("Daftar gambar :\n1. NS2\n2. ICMP\n3. RIP")
    b = input("Masukkan nama file : ")
    client.unduhALL(a,b)
    method = client.file2(a,b)

    if os.path.exists("/home/rezaainur/PycharmProjects/SKT2/ProjekAkhir/primary_server/" + b + ".png"):
        f1 = open("/home/rezaainur/PycharmProjects/SKT2/ProjekAkhir/primary_server/" + b + ".png", 'rb')
        f1_baca = f1.read()
        f1.close()
        f2 = open("/home/rezaainur/PycharmProjects/SKT2/ProjekAkhir/" + b + "_unduh.png", 'w+b')
        f2.write(f1_baca)
        print("Gambar disimpan dgn nama " + b + "_unduh.png")
        f2.close()
    else:
        data1 = "File tidak tersedia"

elif a == "read":
    b = ""
    method = client.file2(a, b)
    print(method)

elif a == "reset":
    b=""
    client.resetALL(a,b)
    method = client.file2(a,b)
    print(method)

else:
    print("INPUT SALAH")

