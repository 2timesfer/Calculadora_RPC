from xmlrpc.client import ServerProxy

def consultar_operacao():
    print("Bem vindo usuário!\n Operações disponíveis: soma, subtração, multiplicação e divisão")
    operacao = input("Escolha uma operação: ").strip().lower()

    # Verifica se a operação escolhida é válida
    # Mapeamento das operações para funções RPC
    if operacao not in ('soma', 'subtração', 'multiplicação', 'divisão'):
        print("Operação inválida.")
        return

    numeros = input("Digite 2 números separados por espaço: ")

    # Divide a string em substrings separadas por espaços
    entrada = numeros.split()   
    # Verifica se o número de elementos é válido
    if len(entrada) > 2:
        print("Por favor, digite no máximo 2 números.")
        return
    
    try:
        # Conectar ao servidor RPC
        with ServerProxy(f'http://{host_server}:{port_server}') as proxy:
            # Chamar a função remota no servidor RPC
            result = getattr(proxy, operacao)(*map(float, numeros.split()))
            print(f"Resultado: {result}")

    except Exception as e:
        print(f"Erro ao conectar ao servidor: {e}")

# Configuração do cliente    
# o host utilizado na execução foi 'ec2-34-207-79-103.compute-1.amazonaws.com'
host_server = ''
port_server = 15000

while True:
    consultar_operacao()
    another = input("Deseja realizar outra operação? (S/N): ").strip().lower()
    if another != 's':
        break 