from models.gerenciamento_quarto import Quarto

class Reserva:
    def __init__(self, nome_hospede: str, dias: int, quarto: Quarto):
        '''Cria a reserva no hotel'''
        self.nome_hospede = nome_hospede
        self.dias = int(dias)
        self.quarto = quarto
        self._finalizada = False

    def valor_total(self) -> float:
        return round(self.dias * self.quarto.preco_diaria, 2)

    def checkout(self) -> float:
        """Finaliza a reserva, libera o quarto e retorna o valor total."""
        if not self._finalizada:
            self.quarto.libera_quarto()
            self._finalizada = True
        return self.valor_total()

    def to_dict(self):
        return {
            "nome_hospede": self.nome_hospede,
            "dias": self.dias,
            "n_quarto": self.quarto.n_quarto,
            "preco_diaria": self.quarto.preco_diaria,
            "valor_total": self.valor_total(),
            "finalizada": self._finalizada,
        }

    def __repr__(self):
        return f"Reserva({self.nome_hospede!r}, dias={self.dias}, quarto={self.quarto.n_quarto})"