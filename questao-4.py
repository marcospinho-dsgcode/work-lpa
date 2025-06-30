# Sistema de Gerenciamento de Funcionários
# Desenvolvido por: Marcos Pinho da Silva

# Mensagem de boas-vindas
print("Bem-vindo ao Sistema de Gerenciamento de Funcionários!")
print("Desenvolvido por: Marcos Pinho da Silva")
print("=" * 50)

# Lista para armazenar os funcionários (lista de dicionários)
lista_funcionarios = []

# Variável global para controlar o ID dos funcionários
id_global = 5118842

def cadastrar_funcionario(id):
    """
    Função para cadastrar um novo funcionário
    Parâmetro: id - ID único do funcionário
    """
    print("\n=== CADASTRAR FUNCIONÁRIO ===")
    
    # Perguntar os dados do funcionário
    nome = input("Digite o nome do funcionário: ")
    setor = input("Digite o setor do funcionário: ")
    salario = input("Digite o salário do funcionário: ")
    
    # Criar um dicionário com os dados do funcionário
    funcionario = {
        "id": id,
        "nome": nome,
        "setor": setor,
        "salario": salario
    }
    
    # Copiar o dicionário para a lista de funcionários
    lista_funcionarios.append(funcionario.copy())
    
    print(f"Funcionário {nome} cadastrado com sucesso!")
    print(f"ID do funcionário: {id}")

def consultar_funcionarios():
    """
    Função para consultar funcionários com submenu
    """
    while True:
        print("\n=== CONSULTAR FUNCIONÁRIOS ===")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Setor")
        print("4. Retornar ao menu")
        
        # Perguntar qual opção deseja
        opcao = input("Digite a opção desejada: ")
        
        if opcao == "1":
            # Consultar todos os funcionários
            print("\n=== TODOS OS FUNCIONÁRIOS ===")
            if len(lista_funcionarios) == 0:
                print("Nenhum funcionário cadastrado!")
            else:
                for funcionario in lista_funcionarios:
                    print(f"ID: {funcionario['id']}")
                    print(f"Nome: {funcionario['nome']}")
                    print(f"Setor: {funcionario['setor']}")
                    print(f"Salário: {funcionario['salario']}")
                    print("-" * 30)
        
        elif opcao == "2":
            # Consultar por ID
            print("\n=== CONSULTAR POR ID ===")
            id_busca = input("Digite o ID do funcionário: ")
            
            # Procurar o funcionário na lista
            funcionario_encontrado = False
            for funcionario in lista_funcionarios:
                if str(funcionario['id']) == id_busca:
                    print(f"ID: {funcionario['id']}")
                    print(f"Nome: {funcionario['nome']}")
                    print(f"Setor: {funcionario['setor']}")
                    print(f"Salário: {funcionario['salario']}")
                    funcionario_encontrado = True
                    break
            
            if not funcionario_encontrado:
                print("Funcionário não encontrado!")
        
        elif opcao == "3":
            # Consultar por setor
            print("\n=== CONSULTAR POR SETOR ===")
            setor_busca = input("Digite o setor: ")
            
            # Procurar funcionários do setor
            funcionarios_encontrados = False
            for funcionario in lista_funcionarios:
                if funcionario['setor'].lower() == setor_busca.lower():
                    print(f"ID: {funcionario['id']}")
                    print(f"Nome: {funcionario['nome']}")
                    print(f"Setor: {funcionario['setor']}")
                    print(f"Salário: {funcionario['salario']}")
                    print("-" * 30)
                    funcionarios_encontrados = True
            
            if not funcionarios_encontrados:
                print("Nenhum funcionário encontrado neste setor!")
        
        elif opcao == "4":
            # Retornar ao menu principal
            return
        
        else:
            # Opção inválida
            print("Opção inválida!")

def remover_funcionario():
    """
    Função para remover um funcionário da lista
    """
    while True:
        print("\n=== REMOVER FUNCIONÁRIO ===")
        
        # Perguntar pelo ID do funcionário a ser removido
        id_remover = input("Digite o ID do funcionário a ser removido: ")
        
        # Procurar o funcionário na lista
        for i in range(len(lista_funcionarios)):
            if str(lista_funcionarios[i]['id']) == id_remover:
                # Remover o funcionário da lista
                funcionario_removido = lista_funcionarios.pop(i)
                print(f"Funcionário {funcionario_removido['nome']} removido com sucesso!")
                return
        
        # Se chegou aqui, o ID não foi encontrado
        print("Id inválido!")

# Programa principal (main)
print("\nSistema iniciado com sucesso!")
print("=" * 50)

while True:
    # Menu principal
    print("\n=== MENU PRINCIPAL ===")
    print("1. Cadastrar Funcionário")
    print("2. Consultar Funcionário")
    print("3. Remover Funcionário")
    print("4. Encerrar Programa")
    
    # Perguntar qual opção deseja
    opcao_principal = input("Digite a opção desejada: ")
    
    if opcao_principal == "1":
        # Cadastrar funcionário
        cadastrar_funcionario(id_global)
        # Incrementar o ID global
        id_global = id_global + 1
    
    elif opcao_principal == "2":
        # Consultar funcionários
        consultar_funcionarios()
    
    elif opcao_principal == "3":
        # Remover funcionário
        remover_funcionario()
    
    elif opcao_principal == "4":
        # Encerrar programa
        print("\nPrograma encerrado!")
        print("Obrigado por usar o Sistema de Gerenciamento de Funcionários!")
        break
    
    else:
        # Opção inválida
        print("Opção inválida!") 