demo_list=[1,'hello',1.34,True,[1,2,3]]
colors=['red','blue','green']


numbers_list=list((1,2,3,4))
#print(numbers_list)

#r=list(range(1,100))
#print(r)

#print(len(colors))

#print(colors[-2])

#print('green' in colors)

#colors.append('violet')
#colors.append(['yellow, gray'])
#colors.extend(['violet','yellow'])

colors.insert(len(colors),'violet')

print(colors)
#Elimina segun un indice, si no se ingresa
#indice elimina el ultimo elemento
#colors.pop()#Elimina el ultimo elemento
#colors.remove('green')
#para quitar todos
#colors.clear()

#para ordenarlos alfabeticamente

#colors.sort()
#inversa

colors.sort(reverse=True)
#imprimir el indice de cierto color
print(colors.index('green'))

#

print(colors)
 