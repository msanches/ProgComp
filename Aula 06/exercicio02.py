segundos = int(input("Digite a quantidade de segundos: "))
horas = segundos//3600
minutos = segundos%3600//60
segundos = segundos%60

print("%d hora(s), %d minuto(s) %d e segundo(s)"%(horas,minutos,segundos))