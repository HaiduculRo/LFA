fin = open("2test2.txt")
n =  int(fin.readline())
final = [False for x in range(n)]
mat = []
for i in range(n):
    mat.append([])
    for j in range(n):
        mat[i].append("*")
final = []
for i in range(n):
    final.append(False)

for i in range(n):
    posibilitati = int(fin.readline())
    for j in range(posibilitati):
        linie = fin.readline()
        linie = linie.split()
        next_nod = int(linie[0])
        cpas = linie[1]
        try:
            mat[i][next_nod].append(cpas)
        except:
            mat[i][next_nod] = [cpas]
    stare = fin.readline()
    if stare == "False" or stare == "False\n":
        final[i] = bool(0)
    else:
        final[i] = bool(1)


rez = []
ok = True
cuvant = input("Cuvant de verificat : ")
poz = 0
for caracter in cuvant:
    for i in range(n):
        if mat[poz][i] != '*':
            if caracter in mat[poz][i]:
                poz = i
                rez.append(i) # am gasit rezultatul
                break
    else:
        print("Cuvantul ales nu este acceptat")
        ok = False
        break

if final[poz] == True:
    print(f"Cuvantul ales  este acceptat si traseul este : ")
    print(*rez)
elif ok == True:
    print("Cuvantul ales nu este acceptat")







