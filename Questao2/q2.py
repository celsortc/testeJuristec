# ### Questão 2
# Construa uma classe em Python que represente uma televisão. Deve ser possível:
# - Alterar os canais
# - Alterar o volume
# - Alternar a função 'mudo'



##### Resposta

#Quando for criada, começa no canal 1, volume 10 e não está no mudo
class Televisao:
  def __init__(self):
    self.canal = 1
    self.volume = 10
    self.mudo = False
  
  #Functions pra aumentar/diminuir volume
  def aumentarVolume(self):
    if self.volume > 0:
      self.volume += 1
  def diminuirVolume(self):
    if self.volume <= 100:
      self.volume -= 1

  #Troca de canal
  def trocarCanal(self, novoCanal):
    if novoCanal > 0:
      self.canal = novoCanal
  
  #boolean para alternar entre mudo e não mudo
  def alternarMudo(self):
    self.mudo = not self.mudo

