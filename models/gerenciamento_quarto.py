class Quarto:
    def __init__(self, n_quarto: int, preco_diaria: float, status: bool = True):
        """
        Cria o quarto no sistema
        status: True = disponível, False = ocupado
        """
        self.n_quarto = int(n_quarto)
        self.preco_diaria = float(preco_diaria)
        self.status = bool(status)

    def reserva_quarto(self):
        self.status = False

    def libera_quarto(self):
        self.status = True

    def to_dict(self):
        return {
            "n_quarto": self.n_quarto,
            "preco_diaria": self.preco_diaria,
            "status": "Disponível" if self.status else "Ocupado",
        }

    def __repr__(self):
        st = "Disp" if self.status else "Ocup"
        return f"Quarto({self.n_quarto}, R${self.preco_diaria:.2f}, {st})"
