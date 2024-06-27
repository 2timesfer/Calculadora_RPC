from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

#funcoes da calculadora
def soma(numeros):
    return sum(numeros)

def subtracao(numeros):
    result = numeros[0]
    for n in numeros[1:]:
        result = result-n
    return result

def multiplicacao(numeros):
    result = numeros[0]
    for n in numeros[1:]:
        result = result * n
    return result

def divisao(numeros):
    result = numeros[0]
    for n in numeros[1:]:
        if(n == 0):
            print('Erro! - Divisão por zero')
            return 
        result = result/n
    return result

#Configura o RPC
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

#Cria servidor
with SimpleXMLRPCServer(('{ip}', 15000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()
    server.register_function(soma, 'soma')
    server.register_function(subtracao, 'subtracao')
    server.register_function(multiplicacao, 'multiplicacao')
    server.register_function(divisao, 'divisao')

    print("Servidor RPC aguardando conexões em {ip}:15000...")
    #loop eterno do servidor
    server.serve_forever()
