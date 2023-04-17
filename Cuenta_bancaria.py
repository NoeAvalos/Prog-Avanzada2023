class Persona():
  def __init__(self, nombre,apellido,dni):
    self.nombre = nombre
    self.apellido = apellido
    self.dni=dni

class Cuentabancaria():
  def __init__(self, persona,tipo_cuenta):
    self.persona = persona
    self.saldo = 0
    self.movimientos = []
    self.tipo_cuenta = tipo_cuenta
    
    
persona = Persona("Juan","Gomez", "11111")
cb1 = Cuentabancaria(persona, "CA")
