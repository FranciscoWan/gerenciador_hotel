# 🏨 Sistema de Gerenciamento de Hotel

Este projeto foi desenvolvido em **Python** utilizando os princípios de **Programação Orientada a Objetos (POO)** para simular o funcionamento básico de um sistema de gerenciamento de hotel.  

O sistema permite o **cadastro e gerenciamento de funcionários**, **controle de quartos**, **realização de reservas** e **cálculo automático do valor total da estadia**.  

---

## 📋 Funcionalidades

### 👩‍💼 Gerenciamento de Funcionários
- Cadastra funcionários com nome, função e salário.  
- Armazena os dados em uma lista interna no sistema.  

### 🛏️ Gerenciamento de Quartos
- Cria quartos com número, preço da diária e status (disponível/ocupado).  
- Permite marcar quartos como ocupados ou liberá-los após o checkout.  
- Impede que um mesmo número de quarto seja cadastrado duas vezes.

### 🧾 Gerenciamento de Reservas
- Registra reservas com nome do hóspede, número de dias e número do quarto.  
- Calcula o valor total da estadia com base nas diárias.  
- Faz o checkout, liberando automaticamente o quarto e exibindo o valor a pagar.  

### 🧮 Cálculo da Conta Final
- Valor total = número de dias × preço da diária do quarto.  
- Exibição automática no checkout.

## 📂 Estrutura de Pastas do Projeto

```
gerenciador_hotel/
│
├── main.py
│
└── models/
    ├── __init__.py
    ├── funcionario.py
    ├── gerenciamento_quarto.py
    ├── hotel.py
    └── imports.py
```

---

## 📘 Descrição dos Arquivos

- **main.py** → Arquivo principal para execução do sistema.
- **models/** → Diretório que contém todas as classes e módulos do sistema.
- **__init__.py** → Torna o diretório `models` um pacote Python.
- **funcionario.py** → Define a classe `Funcionario`, responsável pelos dados dos funcionários.
- **gerenciamento_quarto.py** → Define a classe `Quarto`, responsável pela gestão dos quartos.
- **hotel.py** → Define a classe `Hotel`, que gerencia funcionários, quartos e reservas.
- **imports.py** → Centraliza as importações entre os módulos, evitando redundância.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos:
- Python 3.8 ou superior instalado
- Nenhuma biblioteca externa é necessária (somente módulos padrão do Python)

### Passos:

```bash
# 1️⃣ Clone o repositório
git clone https://github.com/seu-usuario/sistema-gerenciamento-hotel.git

# 2️⃣ Acesse o diretório do projeto
cd sistema-gerenciamento-hotel

# 3️⃣ Execute o programa
python main.py
## 🧠 Estrutura do Projeto

