class Avtomabil:
    def __init__(self, brend, model, yil):
        self.brend = brend
        self.model = model
        self.yil = yil
        self.km = 0

    def yurish(self, masofa):
        self.km += masofa
        return f"{self.brend} {masofa} km yuradi"

    def holat(self):
        return f"{self.brend} {self.model}, {self.yil}-yil, {self.km} km yurgan"


avto1 = Avtomabil("Tayota", "Camry", 2020)
print(avto1.holat())
print(avto1.yurish(100))
print(avto1.holat())

class ElektroAvto(Avtomabil):
    def __init__(self, brend, model, yil, batareya):
        super().__init__(brend, model, yil)
        self.batareya = batareya

    def zaryad(self):
        return f"{self.brend} {self.model} zaryad qilinmoqda ... "

elektro1 = ElektroAvto("Telsa", "Model S", 2022, 45)
print(elektro1.holat())
print(elektro1.zaryad())
