import maxHeap

fila = []

chamados = []

ordem = 0

contador = 999


class Paciente:
    # duvida se faço por parametro ou por input
    def cadastrarPaciente(self, nome_completo, tipo_sanguineo, data_nascimento):
        print("Escreva os dados a seguir para cadastrar um novo paciente e colocá-lo na fila de espera: ")

        nome = input("Nome: ")
        tipoSanguineo = input("Tipo sanguíneo: ")
        data = input("Data de nascimento: ")

        # talvez colocar todos os pacientes em um dicionário com o ome como chave pra acessar eles??

        pass

    def inserirNaFila(self, prioridade, ordem, paciente):
        prioridade = int(input("Prioridade de atendimento: "))
        prioridade = int(input("Ordem de chegada na emergência: "))
        prioridade = input("Nome do paciente: ")

        # insere tudo na tupla e a tula é inserida na fila
        pass

    def chamarPaciente():
        contador -= 1

        # pega o próximo paciente da fila e joga pra lista dos já chamados
        pass

    def listarProximoPaciente():

        # pega opróximo em ordem de prioridade
        # colocar na chave do dicionário nome ou prioridade (prob prioridade, ai pega o nome pelo index)
        pass

    def listarUltimosCinco():

        # n sei ainda
        pass


def menu():
    opcao = int(input("Bem-vindo ao sistema. Digite 1 para cadastrar um paciente, digite 2 para chamar o próximo paciente, digite 3 para apenas mostrar o próximo paciente e digite 4 para listar os últimos 5 pacientes chamados: "))

    if opcao == 1:
        Paciente.cadastrarPaciente()
        Paciente.inserirNaFila()
        pass
    elif opcao == 2:
        Paciente.chamarPaciente()
        pass
    elif opcao == 3:
        Paciente.listarProximoPaciente()
        pass
    elif opcao == 4:
        Paciente.listarUltimosCinco()
        pass
    else:
        print("Opção inválida!")

# Cada item dentro da fila deverá ser representado por uma tupla com o padrão:
# (prioridade [int], ordem [int], paciente [classe Paciente])

# - Prioridade: (MAIS URGENTE: 10 | MENOS URGENTE: 1)
# - Ordem: Quem chegou primeiro terá um valor maior
# - Paciente: objeto da classe Paciente que deverá guardar nome completo, tipo sanguíneo e data de nascimento.

# Por padrão, a linguagem Python ao comparar tupla, caso haja empate entre o primeiro parâmetro, o segundo é usado para desempate.

# IMPORTANTE:
# Manter os pacientes chamados (removidos da fila) em uma lista auxiliar
