vot =[]
vot_all =[1,1,1,1,2,3,2,3,4,4,5,5,5,5,6,6,2,1,2,3]
a=0;b=0;c=0;d=0;e=0;f=0
for i in range(len(vot_all)):
    if(vot_all[i] == 1):
        a = a +1
    elif(vot_all[i] == 2):
        b = b + 1
    elif(vot_all[i] == 3):
        c = c + 1
    elif(vot_all[i] == 4):
        d = d + 1
    elif(vot_all[i] == 5):
        e = e + 1
    elif(vot_all[i] == 6):
        f = f + 1

vot.append(a)
vot.append(b)
vot.append(c)
vot.append(d)
vot.append(e)
vot.append(f)

print(f' Candidato 1 teve {vot[0]} votos.')
print(f' Candidato 2 teve {vot[1]} votos.')
print(f' Candidato 3 teve {vot[2]} votos.')
print(f' Candidato 4 teve {vot[3]} votos.')
print(f' Em Nulo teve {vot[4]} votos({vot[4]*100/20}%).')
print(f' Em branco teve {vot[5]} votos({vot[5]*100/20}%).')





