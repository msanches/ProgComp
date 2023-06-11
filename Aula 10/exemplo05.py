import os
os.system("cls")

lugares_vagos=[10,2,3,4,0]
print("Bem vindos ao CINEMARKO")

for i, vagas in enumerate(lugares_vagos):
  print(f"Sala {i+1}: {vagas} lugares vagos")
  
while True:
  sala = int(input("Escolha uma sala (0 para sair): "))
  if sala==0:
    print("Até logo")
    break
  elif sala > len(lugares_vagos):
    print("Sala inválida!!\n")  
  elif lugares_vagos[sala-1] == 0:
    print("Desculpe! Sala lotada!\n")
  else:
    compra = int(input(f"Quantos ingressos você deseja ({lugares_vagos[sala-1]} vagos) :"))
    if compra > lugares_vagos[sala-1]:
      print("Desculpe! Número de ingressos indisponível\n!!")
    elif compra <= 0:
      print("Número inválido\n!!")
    else:
      lugares_vagos[sala-1] -= compra
      print(f"{compra} ingressos vendidos! Bom filme")
    
  input("Enter para continuar...")
  os.system("cls")
  print("Utilização das salas:")
  for i, vagas in enumerate(lugares_vagos):
    print(f"Sala {i+1}: {vagas} lugares vagos")