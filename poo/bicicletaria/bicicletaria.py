class Bicicleta:
    def __init__(self,cor,modelo,ano,valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzina(self):
        print("Biiibiip")
    
    def correr(self):
        print("começando a correerr....")
        print("vruuuummmm")

    def parar(self):
        print("vruuuummmmm")
        print("parannnndo.....parada")

b1 = Bicicleta("branca","caloi",2023,1500)
print(b1.parar())