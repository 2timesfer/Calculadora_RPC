from xmlrpc.client import ServerProxy

def consultar_operacao():
    print("Bem vindo usuário!\n Operações disponíveis: soma, subtracao, multiplicacao e divisao")
    operacao = input("Escolha uma operação: ").strip().lower()

    # Verifica se a operação escolhida é válida
    if operacao not in ('soma', 'subtracao', 'multiplicacao', 'divisao'):
        print("Operação inválida.")
        return

    numeros = input("Digite os números separados por espaço: ")

    # Divide a string em substrings separadas por espaços
    entrada = numeros.split()
    
    try:
        # Conectar ao servidor RPC
        with ServerProxy(f'http://{host_server}:{port_server}') as proxy:
            # Chamar a função remota no servidor RPC
            result = getattr(proxy, operacao)(list(map(float, entrada)))
            print(f"Resultado: {result}")

    except Exception as e:
        print(f"Erro ao conectar ao servidor: {e}")

# Configuração do cliente
host_server = 'ec2-34-207-79-103.compute-1.amazonaws.com'
port_server = 15000

while True:
    consultar_operacao()
    another = input("Deseja realizar outra operação? (S/N): ").strip().lower()
    if another != 's':
        break
