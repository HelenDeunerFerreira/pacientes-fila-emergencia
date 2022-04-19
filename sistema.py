import maxHeap

fila = []

chamados = []

ordem = 0

contador = 999


class Paciente:
    def cadastrarPaciente(self, nome_completo, tipo_sanguineo, data_nascimento):
        pass

    def inserirNaFila(self, paciente):
        pass

    def listaChamados():
        pass

    def chamarPaciente():
        contador -= 1
        pass

    def listarProximoPaciente():
        pass

    def listarUltimosCinco():
        pass


def menu():
    opcao = int(input("Bem-vindo ao sistema. Digite 1 para cadastrar um paciente, digite 2 para chamar o próximo paciente, digite 3 para apenas listar o próximo paciente e digite 4 para listar os últimos 5 pacientes chamados: "))

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

#    Deve ter interação com o usuário e as opções em um Menu:
# Adicionar novo paciente
# Chamar próximo paciente
# Mostrar próximo paciente (sem chamar)
# Listar os 5 últimos chamados
