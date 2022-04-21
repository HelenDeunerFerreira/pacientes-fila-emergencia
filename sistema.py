import maxHeap

fila = maxHeap.MaxHeap()

pacientesChamados = []

aparecerMenu = True

ordem = 999


class Paciente:

    def cadastrarPaciente():
        global fichaPaciente

        print("\n--> Escreva os dados a seguir para cadastrar um novo paciente e colocá-lo na fila de espera")

        nome = input("Nome: ")
        tipoSanguineo = input("Tipo sanguíneo: ")
        data = input("Data de nascimento: ")

        fichaPaciente = [nome, tipoSanguineo, data]

    def inserirNaFila():
        global ordem

        prioridade = int(input("Prioridade de atendimento: "))
        pacienteNaFila = (prioridade, ordem, fichaPaciente)
        fila.put(pacienteNaFila)

        ordem -= 1

        print("\nPaciente cadastrado e adicionado à fila")

    def chamarPaciente():
        chamado = fila.get()
        print(chamado)
        pacientesChamados.append(chamado)

    def listarProximoPaciente():
        try:
            print(fila.peek())
        except:
            print("Não há um próximo paciente para listar")

    def listarUltimosCinco():
        for index in range(5):
            print(pacientesChamados[index])


def menu():
    global aparecerMenu

    print("\n\n***MENU***\n")
    opcao = input("Bem-vindo ao sistema. \n Digite 1 para cadastrar um paciente \n Digite 2 para chamar o próximo paciente \n Digite 3 para apenas mostrar o próximo paciente \n Digite 4 para listar os últimos 5 pacientes chamados \n Digite 5 para fechar o menu \n * Sua opção: ")

    if opcao == '1':
        Paciente.cadastrarPaciente()
        Paciente.inserirNaFila()

    elif opcao == '2':
        Paciente.chamarPaciente()

    elif opcao == '3':
        Paciente.listarProximoPaciente()

    elif opcao == '4':
        Paciente.listarUltimosCinco()

    elif opcao == '5':
        aparecerMenu = False

    else:
        print("ATENÇÃO: opção inválida! Tente novamente")
        menu()


while aparecerMenu == True:
    menu()
