import random
import time

class nomina:
          
        
    def __init__(self, compania, nombre, salario):
        self.__compania = compania
        self.__nombre = nombre
        self.__salario = salario
        
        
    @property
    def compania(self):
        return self.__compania
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def salario(self):
        return self.__salario
    
    @compania.setter
    def compania(self, compania):
        self.__compania = compania
        
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre 
    
    @salario.setter
    def salario(self, salario):
        self.__salario = salario

            
    def __str__(self):
        return f'Nomina: compania = {self.__compania}, nombre = {self.__nombre}, salario = {self.__salario}'
    
class empleados:
    
    __lista_empleados = []
    
    def __init__(self, num_empl, nuevo_salario, puesto):
      self.__num_empl = num_empl
      self.__nuevo_salario = nuevo_salario
      self.__puesto = puesto
      empleados.__lista_empleados.append(self)

    
    @property
    def num_empl(self):
        return self.__num_empl
        
    
    @property
    def nuevo_salario(self):
      return self.__nuevo_salario  

    @nuevo_salario.setter
    def nuevo_salario(self, nuevo_salario):
        self.__nuevo_salario = nuevo_salario
    
    @property
    def puesto(self):
        return self.__puesto
        
    def __str__(self):
        return f'Nomina: Nombre del empleado = {self.__num_empl}, Nuevo salario = {self.__nuevo_salario}, Puesto del empleado = {self.__puesto}]'
    
    def nomina_num_empl(self):
        a = []
        for nomina in self.__num_empl:
            a.append(nomina.num_empl)
        return ','.join(a)
        
    @classmethod
    def lista_empleados(cls):
        return cls.__lista_empleados

class Airplane:
    
    __vuelos = []

    def __init__(self, destino, aerolinea, dia, mes, año, hora, puerta):
        Airplane.__vuelos.append(self)
        self.__destino = destino
        self.__aerolinea = aerolinea
        self.__dia = dia
        self.__mes = mes
        self.__año = año
        self.__hora = hora
        self.__puerta = puerta
        

    def __repr__(self):
        return f'Airplane[destino={self.__destino}, aerolinea={self.__aerolinea}, {self.__dia}/{self.__mes}/' \
               f'{self.__año} at {self.__hora}, puerta={self.__puerta}]'

    @classmethod
    def vuelos(cls):
        return cls.__vuelos

    @property
    def destino(self):
        return self.__destino

    @property
    def aerolinea(self):
        return self.__aerolinea

    @property
    def dia(self):
        return self.__dia

    @property
    def mes(self):
        return self.__mes

    @property
    def año(self):
        return self.__año

    @property
    def hora(self):
        return self.__hora

    @property
    def puerta(self):
        return self.__puerta
    



class Gate:
    __door = []

    def __init__(self, name):
        Gate.__door.append(self)
        self.__name = name

    def __repr__(self):
        return f'Gate[name={self.__name}]'

    @property
    def name(self):
        return self.__name

    @classmethod
    def door(cls):
        return cls.__door
    
def read_files():
    # leyendo
    airplane = open('airplane.txt', 'r')
    for j in airplane.readlines():
        old_airplane = []
        for i in j.split(','):
            old_airplane.append(i)
        if len(old_airplane) > 1:
            last_word = old_airplane[-1]

            Airplane(old_airplane[0], old_airplane[1], old_airplane[2], old_airplane[3], old_airplane[4],
                     old_airplane[5], last_word[:-1])  
    airplane.close()
    # leyendo
    gate = open('gates.txt', 'r')
    for g in gate.readlines():
        Gate(g[:-1])


read_files()

while True:
    flights = open('airplane.txt', 'a')
    print('¡Bienvenido! Aqui puedes crear tus vuelos,' 
    ' registrar tu nomina o modificar tu salario')
    
    print('1. Crear vuelo')
    print('2. Registrar mi nomina')
    print('3. Modificar mi salario ')
    print('4. Salir')
    ask = int(input('¿Qué acción deseas realizar?'))
    if ask == 1:

      dest = input('¿A donde se dirige tu vuelo? ')
      airl = input('¿Cual es tu aerolinea? ')
      d = input('¿En qué día saldra tu vuelo? ')
      m = input('¿En qúe mes saldra tu vuelo? ')
      y = input('¿En qúe año saldra tu vuelo? ')
      h = input('¿A qué hora saldra tu vuelo? ')
      gat = random.choice(Gate.door())

      new_airplane = Airplane(dest, airl, d, m, y, h, gat)
      flights.write(f'{dest},{airl},{d},{m},{y},{h},{gat}\n')
      print('Vuelo creado exitosamente.')

      print('Estos son todos los vuelos que tenemos creados:')
      for a in range(len(Airplane.vuelos())):
          print(f'{a}) {Airplane.vuelos()[a]}\n')

      end = input('Quieres registrar otro vuelo? ')

      if end.lower() == 'no':
          
          time.sleep(3)
    elif ask == 2:
      a1 = nomina('Aeromexico', 'José Carlos', 10000)
      a2 = nomina('Mexicana', 'Diana Paola', 9000)
      a3 = nomina('Air France', 'Fersita', 1000)

      print('1:',a1)
      print('2:',a2)
      print('3:',a3)
      time.sleep(3)
      
    elif ask == 3:
      a1 = nomina('Aeromexico', 'José Carlos', 10000)
      a = a1.nuevo_salario = 100000
      b1 = empleados('Bad Bunny', 15000, 'Director General')

      print('5:',b1)
      time.sleep(3)

    elif ask == 4:
      break

    else:
      print("Lo sentimos, esta no es una opción valida")
      break