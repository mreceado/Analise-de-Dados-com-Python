# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!



def soma(n1,n2): 
    print("Resultado: %s" %(n1+n2)) 

def subtracao(n1,n2):
    print("Resultado: %s" %(n1-n2))

def multiplicacao(n1,n2):
    print("Resultado: %s" %(n1*n2))

def divisao(n1,n2):
    if n2 != 0:
        print("Resultado: %s" %(n1/n2))
    else:
        print("Não tem solução!")

def potencia(n1,n2):
    print("Resultado: %s" %(n1**n2))
    


print("------------- CALCULADORA ------------")
print("\n")
print("Operações a escolher")
print("'+' para somar")
print("'-' para subtrair")
print("'*' para multiplicar")
print("'/' para dividir")
print("'**' para potência")
print("\n")

num1 = int(input("Insira o 1º Número: "))
num2 = int(input("Insira o 2º Número: "))

op = input("Escolha a operação: ")

if op == '+':
    soma(num1,num2)
elif op == '-':
    subtracao(num1,num2)
elif op == '*':
    multiplicacao(num1,num2)
elif op == '/':
    divisao(num1,num2)
elif op == '**':
    potencia(num1,num2)
else:
    print("Operador inválido!!!")          
    
