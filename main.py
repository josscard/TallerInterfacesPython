from abc import ABC, abstractmethod

# creamos las interfaces a implementar
class Volarable(ABC):
    @abstractmethod
    def volar(self):
        pass
class Olfatearable(ABC):
    @abstractmethod
    def olfatear(self):
        pass

class Nadarable(ABC):
    @abstractmethod
    def nadar(self):
        pass

class Terrestreable(ABC):
    @abstractmethod
    def desplazar(self):
        pass

class Respirable(ABC):
    @abstractmethod
    def respirar(self):
        pass


#creamos las clases que van a implementar las interfaces

class Pato(Volarable, Respirable, Nadarable):
    def volar(self):
        print('El Pato esta volando')

    def nadar(self):
        print('El Pato esta nadando')

    def respirar(self):
        print('El Pato esta respirando')

class Elefante(Terrestreable, Nadarable, Respirable):
    def desplazar(self):
        print('El Elefante se esta desplazando')

    def respirar(self):
        print('El Elefante esta respirando')

    def nadar(self):
        print('El Elefante esta nadando')

class Culebra(Terrestreable, Nadarable, Respirable):
    def desplazar(self):
        print('La Culebra se esta desplazando')

    def respirar(self):
        print('La Culebra esta respirando')

    def nadar(self):
        print('La Culebra esta nadando')


class Perro(Terrestreable, Nadarable, Respirable, Olfatearable):
    def desplazar(self):
        print('El Perro se esta desplazando')

    def olfatear(self):
        print('El Perro esta olfateando')

    def nadar(self):
        print('El Perro esta nadando')

    def respirar(self):
        print('El Perro esta respirando')

class Pez(Nadarable, Respirable, Terrestreable):
    def desplazar(self):
        print('El Pez se esta desplazando')

    def respirar(self):
        print('El Pez esta respirando')

    def nadar(self):
        print('El Pez esta nadando')



#instanciamos las clases para ejecutar cada accion que le corresponde

douglas = Perro()

print(douglas.desplazar())
print(douglas.olfatear())
print(douglas.respirar())
print(douglas.nadar())


donald = Pato()

print(donald.nadar())
print(donald.respirar())
print(donald.nadar())


dumbo=Elefante()

print(dumbo.desplazar())
print(dumbo.nadar())
print(dumbo.respirar())


nemo= Pez()

print(nemo.desplazar())
print(nemo.nadar())
print(nemo.respirar())


piton=Culebra()

print(piton.desplazar())
print(piton.nadar())
print(piton.respirar())

