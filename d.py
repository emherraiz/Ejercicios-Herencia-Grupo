class Pared:
    
  def __init__(self, orientacion):
    self.orientacion = orientacion



class Ventana:

  def __init__(self, objeto_pared, superficie, proteccion):
    self.orientacion = objeto_pared.orientacion
    self.superficie = superficie
    
    self.proteccion = proteccion
    
    if(proteccion!="Persiana" and proteccion!="Estor"):
      raise Exception("Protección obligatoria ")

class Casa:

  def __init__(self, norte, oeste, sur, este):
    self.norte = norte.superficie
    self.oeste = oeste.superficie
    self.sur = sur.superficie
    self.este = este.superficie


  def superficie_acristalada(self):
    return (self.norte + self.oeste + self.sur + self.este)
    





pared_norte = Pared("NORTE") 
pared_oeste = Pared("OESTE") 
pared_sur = Pared("SUR") 
pared_este = Pared("ESTE") 


ventana_norte = Ventana(pared_norte, 0.5,"Persiana") 
ventana_oeste = Ventana(pared_oeste, 1, "Persiana") 
ventana_sur = Ventana(pared_sur, 2, "Persiana") 
ventana_este = Ventana(pared_este, 1, "Persiana") 


casa = Casa(ventana_norte, ventana_oeste, ventana_sur, ventana_este) 

print(casa.superficie_acristalada()) 




