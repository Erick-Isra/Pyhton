import random

def candado(lista1,lista2,lista3,lista4):
    final_list = []
    contador = 0
    combinacion = ""
    while(contador<10000):
        combinacion = lista1[random.randint(0,9)] + lista2[random.randint(0,9)] + lista3[random.randint(0,9)] + lista4[random.randint(0,9)]
        if contador == 0:
            final_list.append(combinacion)
            contador += 1
        elif combinacion not in final_list: 
            final_list.append(combinacion) 
            contador += 1      
    return final_list

print(candado(["B","D","M","J","P","R","S","T","L","N"],["O","U","Y","R","T","L","H","A","E","I"],["A","C","D","E","O","R","S","T","L","N"],["Y","R","S","T","L","N","E","D","H","K"]))
        