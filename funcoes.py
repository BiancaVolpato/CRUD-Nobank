

#função que mostra cabeçalho
def cabecalho():
    print('-'*36)
    print('----------FACULDADE CESUSC----------')
    print('NOME: Bianca Volpato')
    print('CURSO: Análise e Desenvolvimento de Sistemas')
    print('DISCIPLINA: Lógica de programação e algoritmos ')
    print('PROFESSOR: Roberto Fabiano Fernandes ')
    print('TURMA: ADS11')
    print('AVALIAÇÃO: N2/N3')
    print('-'*36)


#função cadastrar dados
def cadastrar_dados():

    #tentativa de criar arquivo e salvar dados nele mesmo
    try:

        #abrir arquivo 
        with open('dados_clientes.txt', 'a') as arquivo:

            #solicitar informações do cliente
            nome = input("Nome: ")
            cpf = int(input("CPF: "))
            dataNasc = input("Data de Nascimento: ")
            endereco = input("Endereço: ")
            cep = int(input("CEP: "))
            cidade = input("Cidade: ")
            estado = input("estado: ")
            telefone = int(input("telefone: "))
            obs = input("Observações: ")
            print("-"*36)

            #Formatar os dados do cliente
            #variavel tipo lista
            cliente = f"{nome};{cpf};{dataNasc};{endereco};{cep};{cidade};{estado};{telefone};{obs}, \n"

            #onde os dados sao gravados no arquivo
            arquivo.write(cliente)

            #Exibi mensagem de conclusão
            print("Dados do cliente cadastrados com sucesso!")

    except ValueError: 
        #Capturar erros caso valores fora do formato esperado sejam inseridos
        print("Valor inválido")
    except Exception as e:
        print("Dados não cadastrados", str(e))

#Função listar dados
def listar_dados ():

    #Tentativa ler e listar dados
    try:

        #Abrir Dados_Clientes
        with open ('dados_clientes.txt','r') as arquivo:
            linhas = arquivo.readlines()

            #Verificar se há dados no arqiuvo
            if not linhas:
                print("Nenhum dado de cliente cadastrado")

            #Exibir um cabeçalho com os dados
            else:
                print("-"*30)
                print("Dados cadastrados: ")
                
                #repetir sobre cada linha do arquivo
                for linha in linhas:
                    #Dividir linhas por vírgulas e remover os espaços em branco
                    dados = linha.strip().split(';')

                    #Extrair os valores de cada dado
                    nome_cliente = dados[0]
                    cpf = dados[1]
                    dataNasc = dados [2]
                    endereco = dados [3]
                    cep = dados [4]
                    cidade = dados [5]
                    estado = dados [6]
                    telefone = dados [7]
                    obs = dados [8]

                    #Exibir os dados dos clientes na tela
                    print("Nome: ", nome_cliente)
                    print("CPF: ", cpf)
                    print("Data de Nascimento: ", dataNasc)
                    print("Endereço: ", endereco)
                    print("CEP: ", cep)
                    print("Cidade: ", cidade)
                    print("Estado: ", estado)
                    print("Telefone: ", telefone)
                    print("obs: ", obs)
                    print("-"*30)

    except FileNotFoundError:
        #Capturar erros caso o arquivo não seja encontrado
        print("Arquivo de dados não encontrado")
    except Exception as e:
        #Capturar erros durante o listar dados
        print("Ocorreu um erro ao listar os dados:", str(e))


#fazer a função de alterar dados
def alterar_dados():
     #Solicitar CPF do cliente a ser atualizado
    cpf = input("Digite o CPF do cliente a ser atualizado: ")

    #Variavel booleana para indicar se o cliente foi encontrado
    encontrado = False

    #Lista para armazenar os dados atualizados
    dados_atualizados = []

    #Tentativa de atualizar dados
    try:

        #Abrir arquivo de dados
        with open ('dados_clientes.txt','r') as arquivo:

            #ler as linhas do arquivo
            linhas =  arquivo.readlines()
            
            #Repetir sobre cada linha do arquivo
            for linha in linhas:
                #Separa os dados da linha em uma lista usando a virgula como separador
                dados = linha.strip().split(';')
                #Armazena o cpf do cliente
                cpf_cliente = dados[1]

                #Verficia se o CPF fornecido é igual ao CPF do cliente
                if cpf == cpf_cliente:
                    #Marca como encontrado
                    encontrado = True
                    # Mostra na tela os dados do cliente
                    print("-"*30)
                    print("Dados atuais do cliente:")
                    print("Nome:", dados[0])
                    print("CPF:", dados[1])
                    print("Data Nascimento:", dados[2])
                    print("Endereço:", dados[3])
                    print("CEP: ",dados [4])
                    print("Cidade:", dados[5])
                    print("Estado: ", dados [6])
                    print("Telefone: ", dados [7])
                    print("Observação: ", dados [8])
                    print()

                    #Obter novos dados
                    novos_dados = {}
                    novos_dados['nome_cliente'] = input("Digite o novo nome do cliente: ")
                    novos_dados['cpf_cliente'] = input("Digite o novo cpf do cliente: ")
                    novos_dados['data_nascimento'] = input("Digite a nova data de nascimento do cliente: ")
                    novos_dados['endereco'] = input ("Digite o novo endereço do cliente: ")
                    novos_dados['cep'] = input("Digite o novo CEP do cliente: ")
                    novos_dados['cidade'] = input("Digite a nova cidade do cliente: ")
                    novos_dados['estado'] = input("Digite o novo estado do cliente: ")
                    novos_dados['telefone'] = input("Digite o novo telefone do cliente: ")
                    novos_dados['obs'] = input("Digite uma nova observação sobre o cliente: ")
                    print()

                    # Atualizar os dados do cliente
                    dados[0] = novos_dados['nome_cliente']
                    dados[1] = novos_dados['cpf_cliente']
                    dados[2] = novos_dados['data_nascimento']
                    dados[3] = novos_dados['endereco']
                    dados[4] = novos_dados['cep']
                    dados[5] = novos_dados['cidade']
                    dados[6] = novos_dados['estado']
                    dados[7] = novos_dados['telefone']
                    dados[8] = novos_dados['obs']

                #Converte a lista de dados de volta para uma string separada por vírgulas
                #converte a lista de dados de um cliente de volta em uma string formatada para ser escrita no arquivo.
                linha_atualizada = ','.join(dados) + '\n'
                #Adiciona a linha atualizada à lista de dados atualizados

                dados_atualizados.append(linha_atualizada)

        #Se o cliente foi encontrado        
        if encontrado:
            #Abrir arquivo
            with open('dados_clientes.txt', 'w') as arquivo:
                #Escrever dados atualizados de volta no arquivo
                arquivo.writelines(dados_atualizados)
                print("Dados atualizados com sucesso!")

        #Se o cliente não foi encontrado
        else:
            print("Cliente não encontrado")
    
    except FileNotFoundError:
        #Capturar erros caso o Arquivo não seja encontrado
        print("Arquivo de dados não encontrado")
    except Exception as e:
        print("Houve um erro ao alterar o dado",str(e))
   


#Função Deletar Dado
def deletar_dado():

    #Solicitar CPF do cliente a ser deletado
    cpf = input("Digite o CPF do cliente a ser deletado: ")

    #Tentativa de apagar dados
    try:

        #Abrir arquivo de dados em modo de leitura
        with open ('dados_clientes.txt', 'r') as arquivo:

            #Ler as linhas do arquivo
            linhas = arquivo.readlines()
        
        #Abrir arquivo de dados em modo de escrita
        with open ('dados_clientes.txt', 'w') as arquivo:

            #Variavel booleana para indicar se o cliente foi encontrado
            encontrado = False

            #Repetir sobre cada linha do arquivo
            for linha in linhas:
                #Separar os dados da linha em uma lista usando virgula como separador
                dados = linha.strip().split(';')
                #Armazena o cpf do cliente
                cpf_cliente = dados [1]

                #Verificar se o CPF fornecido é giual ao cpf do cliente
                if cpf == cpf_cliente:
                    #Marca como encontrado
                    encontrado = True 

                #Se o CPF não corresponder ao CPF do cliente, reescrever o mesmo novamente
                else: 
                    arquivo.write(linha)
            
            #Se o cliente foi encontrado
            if encontrado:
                print("Cliente excluido com sucesso!")
            
            #Se o cliente não foi encontrado
            else:
                print("Cliente não encontrado. Nenhum dado foi excluido.")

    
    except FileNotFoundError:
        #Capturar erros caso o arquivo não seja encontrado
        print("Arquivo de dados não encontrado")
    except Exception as e:
        print("Houve um erro ao deletar o dado", str(e))


#Função Backup
def backup_dados():

    #Tentativa de criar um backup dos dados
    try:

        #Abrir dados clientes 
        with open ('dados_clientes.txt','r') as origem:
            dados = origem.read()

            #Criar uma copia dos dados clientes
            with open ('dados_clientes_backup.txt','w') as destino:
                destino.write(dados)

        #Alerta de sucesso
        print("Backup realizado com sucesso!")
    
    #Exceção de erro arquivo não encontrado
    except FileNotFoundError:
        print("Arquivo de origem não encontrado")
     #Exceção de erro backup não realizado
    except Exception as e:
        print("Houve um erro ao fazer o backup")


#Exibir MENU
def exibir_menu():
    #Exibir opções da nela
    print("--------------- MENU ---------------")
    print("1. Cadastrar novo cliente")
    print("2. Listar dados dos clientes")
    print("3. Alterar dados de um cliente")
    print("4. Deletar dados de um cliente")
    print("5. Realizar backup dos dados")
    print("0. Sair do sistema")
    print("-"*36)


#Função principal para rodar o menu
def main():
    #Executa um loop infinito até que encontre a instrução 'break'
    while True:
        #Exibe o menu
        exibir_menu()
        #Pedir ao usuario que digite o numero da opção desejada
        opcao = input("Digite o numero da opção desejada: ")
        #Imprime uma linha de separação
        print("-"*36)

        #Verificar qual opção foi selecionada
        if opcao == "1":
            #Charmar função apra cadastrar dados
            cadastrar_dados()
        elif opcao == "2":
            #Chamar função para listar os dados
            listar_dados()
        elif opcao == "3":
            #Chamar função para alterar os dados
            alterar_dados()
        elif opcao == "4":
            #Chamar função para deletar os dados
            deletar_dado()
        elif opcao == "5":
            #Chamar função para fazer backup dos dados
            backup_dados()
        elif opcao == "0":
            #Imprime uma mensagem dizendo que esta saindo do sistema
            print("Saindo do sistema...")
            #Saia do loop
            break
        
        else: 
            #Se nenhuma opção valida for selecionada, mostre uma mensagem de erro
            print("Opção inválida.Por favor, escolha uma opção válida")
