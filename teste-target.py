# PERGUNTA 1

indice = 13 
soma = 0
k = 0

while k < indice:
    k=k+1
    soma = soma+ k
    
print(soma)
# RESULTADO = 91

###########################

#PERGUNTA 2

v1 = int(0)
v2 = int(1)
v3 = int(0)
valorIn = int(input('Digite um número: '))
while valorIn > v3:
    v3 = v1 + v2
    v1 = v2
    v2 = v3
if valorIn == 0 or valorIn == 1:
    print ('O número faz parte da sequência de Fibonacci.')
elif valorIn == v3:
    print ('O número faz parte da sequência de Fibonacci.')
else:
    print ('O número digitado não faz parte da sequência de Fibonacci.')


###########################

#PERGUNTA 3

#RESULTADO a = 2
#RESULTADO b = 128
#RESULTADO c = 49
#RESULTADO d = 100
#RESULTADO e = 13
#RESULTADO f = 200

###########################

#PERGUNTA 4 

#RESULTADO = ambos estarão á mesma distância de Ribeirão Preto, pois se eles estão se encontrando no mesmo 
           # ponto do caminho portando a distância é a mesma

##########################

#PERGUNTA 5

string = "amor"[::-1]
print(string)
#RESULTADO = roma
