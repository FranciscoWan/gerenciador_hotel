from typing import List, Optional
from models.funcionario import Funcionario
from models.gerenciamento_quarto import Quarto
from models.reserva import Reserva

class Hotel:
    def __init__(self, nome_hotel: str = "Meu Hotel"):
        '''Cria o sistema o hotel que permite gerenciar os funcionários, quartos e reservas.'''
        self.nome_hotel = nome_hotel
        self.funcionarios: List[Funcionario] = []
        self.quartos: List[Quarto] = []
        self.reservas: List[Reserva] = []

    # ---------- Funcionários ----------
    def adicionar_funcionario(self, funcionario: Funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self) -> List[dict]:
        return [f.to_dict() for f in self.funcionarios]

    # ---------- Quartos ----------
    def adicionar_quarto(self, quarto: Quarto):
        # evita duplicar número de quarto
        if any(q.n_quarto == quarto.n_quarto for q in self.quartos):
            raise ValueError(f"Quarto {quarto.n_quarto} já existe.")
        self.quartos.append(quarto)

    def listar_quartos(self) -> List[dict]:
        return [q.to_dict() for q in sorted(self.quartos, key=lambda x: x.n_quarto)]

    def buscar_quarto_por_numero(self, n_quarto: int) -> Optional[Quarto]:
        for q in self.quartos:
            if q.n_quarto == int(n_quarto):
                return q
        return None

    def quartos_disponiveis(self) -> List[Quarto]:
        return [q for q in self.quartos if q.status]

    # ---------- Reservas ----------
    def reservar_quarto(self, nome_hospede: str, dias: int, n_quarto: Optional[int] = None) -> Reserva:
        """
        Se n_quarto for None, escolhe o primeiro quarto disponível.
        Retorna a Reserva criada.
        """
        if n_quarto is None:
            disponiveis = self.quartos_disponiveis()
            if not disponiveis:
                raise RuntimeError("Nenhum quarto disponível para reserva.")
            quarto = disponiveis[0]
        else:
            quarto = self.buscar_quarto_por_numero(n_quarto)
            if quarto is None:
                raise ValueError(f"Quarto {n_quarto} não encontrado.")
            if not quarto.status:
                raise RuntimeError(f"Quarto {n_quarto} está ocupado.")

        quarto.reserva_quarto()
        reserva = Reserva(nome_hospede, dias, quarto)
        self.reservas.append(reserva)
        return reserva

    def listar_reservas_ativas(self) -> List[dict]:
        return [r.to_dict() for r in self.reservas if not r._finalizada]

    def listar_todas_reservas(self) -> List[dict]:
        return [r.to_dict() for r in self.reservas]

    def checkout(self, nome_hospede: str) -> float:
        """
        Procura a reserva do hóspede (não finalizada) e faz checkout.
        Retorna o valor a pagar.
        """
        for r in self.reservas:
            if r.nome_hospede == nome_hospede and not r._finalizada:
                valor = r.checkout()
                return valor
        raise LookupError(f"Nenhuma reserva ativa encontrada para {nome_hospede}.")

    def resumo_hotel(self) -> dict:
        return {
            "nome": self.nome_hotel,
            "n_funcionarios": len(self.funcionarios),
            "n_quartos": len(self.quartos),
            "n_quartos_disponiveis": len(self.quartos_disponiveis()),
            "n_reservas_ativas": len(self.listar_reservas_ativas()),
            "n_reservas_totais": len(self.reservas),
        }

    def __repr__(self):
        return f"<Hotel {self.nome_hotel}: {len(self.quartos)} quartos, {len(self.funcionarios)} funcionários>"
