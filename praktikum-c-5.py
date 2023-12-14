import os
os.system("clear")

a = True
limit = 5
i = 0

while a:
    print(f"Menjalankan Program {limit + 1 - i}")
    if i == limit:
        a = True
        print("Program Berhasil Dijalankan")
    else:
        a = False