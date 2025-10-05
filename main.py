from models.imports import *

def main():
    hotel = Hotel("Hotel Pythonista")

    hotel.adicionar_quarto(Quarto(101, 150.0, True))
    hotel.adicionar_quarto(Quarto(102, 200.0, True))
    hotel.adicionar_quarto(Quarto(201, 300.0, True))

    hotel.adicionar_funcionario(Funcionario("Ana", "Gerente", 4500.00))
    hotel.adicionar_funcionario(Funcionario("Bruno", "Recepcionista", 2200.00))

    while True:
        print("\n--- Menu Hotel ---")
        print("1. Listar quartos")
        print("2. Listar quartos disponíveis")
        print("3. Fazer reserva")
        print("4. Listar reservas ativas")
        print("5. Checkout (fazer pagamento)")
        print("6. Listar funcionários")
        print("7. Resumo do hotel")
        print("0. Sair")
        escolha = input("Escolha: ").strip()

        if escolha == "1":
            for q in hotel.listar_quartos():
                print(q)
        elif escolha == "2":
            for q in hotel.quartos_disponiveis():
                print(q)
        elif escolha == "3":
            nome = input("Nome do hóspede: ").strip()
            dias = int(input("Número de diárias: "))
            num = input("Número do quarto (enter para auto-atribuir): ").strip()
            try:
                n_quarto = int(num) if num else None
                reserva = hotel.reservar_quarto(nome, dias, n_quarto)
                print("Reserva criada:", reserva.to_dict())
            except Exception as e:
                print("Erro ao reservar:", e)
        elif escolha == "4":
            for r in hotel.listar_reservas_ativas():
                print(r)
        elif escolha == "5":
            nome = input("Nome do hóspede para checkout: ").strip()
            try:
                valor = hotel.checkout(nome)
                print(f"Checkout realizado. Valor a pagar: R${valor:.2f}")
            except Exception as e:
                print("Erro no checkout:", e)
        elif escolha == "6":
            for f in hotel.listar_funcionarios():
                print(f)
        elif escolha == "7":
            print(hotel.resumo_hotel())
        elif escolha == "0":
            print("Encerrando.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()