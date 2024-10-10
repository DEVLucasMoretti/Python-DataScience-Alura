sum=0
weight=0
numbers= [5,12,20,15] 
for i in range(4):
    weight = weight + (i+1)
    print(weight)
    sum= sum + numbers[i]*(i+1)
    
print(f'A média ponderada é {sum/weight}')
