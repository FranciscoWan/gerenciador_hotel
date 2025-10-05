
class Funcionario:
    '''
    Cria um funcionario dentro do sistema
    '''
    def __init__(self, nome: str, funcao: str, salario: float):
        self.nome = nome
        self.funcao = funcao
        self.salario = float(salario)

    def to_dict(self):
        return {"nome": self.nome, "funcao": self.funcao, "salario": self.salario}

    def __repr__(self):
        return f"Funcionario({self.nome!r}, {self.funcao!r}, {self.salario:.2f})"
