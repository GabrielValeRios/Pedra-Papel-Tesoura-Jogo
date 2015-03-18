print('''
      Bem vindo ao jogo de pedra papel tesoura spock e lagarto!
      Quem fizer 3 pontos vence!
      
      ''')

j=0
c=0
while (j<3 and c<3):
  import random
  print('jogador=%d' % j)
  print('computador=%d' % c)

  jg=int(input('Escolha: 1-pedra 2-papel 3-tesoura 4-spock 5-lagarto. Eu ja escolhi!'))
  cpu=random.randint(1,5)
  if(jg==1):
    if(cpu==1):
      print('Empate')
    elif(cpu==2):
      print('voce perdeu!')
      c+=1
    elif(cpu==3):
      print('voce ganhou!')
      j+=1
    elif(cpu==4):
      print('voce perdeu!')
      c+=1
    elif(cpu==5):
      print('voce ganhou!')
      j+=1
  elif(jg==2):
    if(cpu==1):
      print('voce ganhou!')
      j+=1
    elif(cpu==2):
      print('empate')
    elif(cpu==3):
      print('voce perdeu!')
      c+=1
    elif(cpu==4):
      print('voce ganhou!')
      j+=1
    elif(cpu==5):
      print('voce perdeu!')
      c+=1
  elif(jg==3):
    if(cpu==1):
      print('voce perdeu!')
      c+=1
    elif(cpu==2):
      print('voce ganhou!')
      j+=1
    elif(cpu==3):
      print('empate')
    elif(cpu==4):
      print('voce perdeu!')
      c+=1
    elif(cpu==5):
      print('voce ganhou!')
      j+=1
  elif(jg==4):
      if(cpu==1):
        print('voce ganhou!')
        j+=1
      elif(cpu==2):
        print('voce perdeu!')
        c+=1
      elif(cpu==3):
        print('voce ganhou!')
        j+=1
      elif(cpu==4):
        print('empate')
      elif(cpu==5):
        print('voce perdeu!')
        c+=1
  elif(jg==5):
    if(cpu==1):
      print('voce perdeu!')
      c+=1
    elif(cpu==2):
      print('voce ganhou!')
      j+=1
    elif(cpu==3):
      print('voce ganhou!')
      c+=1
    elif(cpu==4):
      print('voce ganhou!')
      j+=1
    elif(cpu==5):
      print('empate')
if(j==3):
    print('parabens, voce venceu o jogo!!')
elif(c==3):
    print('Nao foi dessa vez...')
        
         
  
