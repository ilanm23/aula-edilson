# Desafios da Semana 01 - Python
# Prática Independente

# 1. Calculadora de troco
valor_compra = float(input("Digite o valor da compra: R$ "))
valor_pago = float(input("Digite o valor pago: R$ "))

troco = valor_pago - valor_compra

print(f"Troco: R$ {troco:.2f}")


# 2. Média de notas
nota_1 = float(input("\nDigite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))

media = (nota_1 + nota_2 + nota_3) / 3

print(f"Média: {media:.2f}")


# 3. Conversor de tempo
total_segundos = int(input("\nDigite o tempo em segundos: "))

horas = total_segundos // 3600
minutos = (total_segundos % 3600) // 60
segundos = total_segundos % 60

print(f"Tempo convertido: {horas}h {minutos}min {segundos}s")


# 4. Calculadora de desconto
preco = float(input("\nDigite o preço do produto: R$ "))
percentual_desconto = float(input("Digite o percentual de desconto: "))

desconto = preco * (percentual_desconto / 100)
preco_final = preco - desconto

print(f"Preço final: R$ {preco_final:.2f}")


# 5. Par ou ímpar
numero = int(input("\nDigite um número inteiro: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")


# 6. Inversor de nome
nome = input("\nDigite seu nome: ")

nome_invertido = nome[::-1]

print(f"Nome invertido: {nome_invertido}")

##