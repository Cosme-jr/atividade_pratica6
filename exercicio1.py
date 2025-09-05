"""
Crie um programa que gera uma senha aleatória com o módulo random, utilizando caracteres especiais, possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória.

"""
import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha

tamanho = int(input("Informe o tamanho da senha: "))
print("Senha gerada:", gerar_senha(tamanho))
# Fim do código