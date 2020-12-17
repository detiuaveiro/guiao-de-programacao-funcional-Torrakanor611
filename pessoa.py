
class Pessoa:
    def __init__(self, nome, data_nasc, cc):
        self.nome = nome
        self.data_nasc = data_nasc
        self.cc = cc

    def __str__(self):
        return f'name is {self.nome}, birthdate: {self.data_nasc}, cc: {self.cc}'

p1 = Pessoa('tó mané', '12-2-2098', 98547924)

print('->' + p1.nome)
print(p1)