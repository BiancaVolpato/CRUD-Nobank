#função cadastrar dados
def cadastrar_dados():

    #tentativa de criar arquivo e salvar dados nele mesmo
    try:

        #abrir arquivo 
        with open('dados_clientes.txt', 'a') as arquivo:

            #solicitar informações do cliente
            nome = input("Nome: ")
            cpf = input("CPF: ")
            dataNasc = input("Data de Nascimento: ")
            endereco = input("Endereço: ")
            cep = input("CEP: ")
            cidade = input("Cidade: ")
            estado = input("estado: ")
            telefone = input("telefone: ")
            obs = input("Observações: ")
            print("-"*36)

            #Formatar os dados do cliente
            cliente = f"{nome},{cpf},{dataNasc},{endereco}, {cep}, {cidade}, {estado}, {telefone}, {obs}, \n"

            #Escrever os dados no arquivo
            arquivo.write(cliente)

            #Exibir mensagem de conclusão
            print("Dados do cliente cadastrados com sucesso!")

    except ValueError: 
        #Capturar erros caso valores fora do formato esperado sejam inseridos
        print("Valor inválido")
    
    except Exception as e:
        #Captura erros durante o cadastro dos dados
        print("Ocorreu um erro ao cadastrar os dados:", str(e))




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
                    dados = linha.strip().split(',')

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
                print("Dados atualizados com sucesso!")

    
    except FileNotFoundError:
         #Capturar erros caso o Arquivo não seja encontrado
        print("Arquivo de dados não encontrado")
    except Exception as e:
        #Capturar erros durante a atualização dos dados
        print("Ocorreu um erro ao atualizar os dados: ", str(e))

#fazer a função de atualizar dados



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
                dados = linha.strip().split(',')
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
        #Capturar erros durante a exclusão dos dados
        print("Ocorreu um erro ao excluir os dados: ", str(e))




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
        print("Ocorreu um erro ao realizar o backup de dados: ", str(e))



#Exibir MENU
def exibir_menu():
    #Exibir opções da nela
    print("--------------- MENU ---------------")
    print("1. Cadastrar novo cliente")
    print("2. Listar dados dos clientes")
    print("3. Atualizar dados de um cliente")
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
        #elif opcao == "3":
            #Chamar função para atualizar os dados
            #atualizar_dados()
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
