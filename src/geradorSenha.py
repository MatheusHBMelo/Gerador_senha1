# encoding= utf-8
import random
import os

# Grupo dos caracteres que serão usado para formar a senha
minus = 'abcdefghijklmnopqrstuvwxyz'
maius = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '0123456789'
simbolos = '@#$%&*_'

# Agrupando todas as possibilidades
all = minus + maius + numeros + simbolos

# Mensagem do autor
print("Gerador de senha 3.0 - Matheus Henrique")
print("")

# Interação com usuário para definição do tamanho da senha
length = int(input("Sua senha terá quantos caracteres: "))
print("")

# Gerando e armazenando a senha
password = "@" + "".join(random.sample(all, length)) + "@"

# Imprimindo a senha na tela
print('A senha gerada foi:', password)
print(
    f"A sua senha possui {length} caracteres e dois apontadores de segurança!")
print("")

# Função que demonstra as atualizações
def notasupdate():
    print("\033[32m"+"__________________Versão 1.0__________________"+"\033[0;0m")
    print("-Foi criado o metodo de junção de caracteres.")
    print("-Foi criada a estrutura de geração da senha.")
    print("-Agora o programa processa letras em minusculo.")
    print("")
    print("\033[32m"+"__________________Versão 2.0__________________"+"\033[0;0m")
    print("-Foram trocadas algumas estruturas IF por While.")
    print("-Foi adicionado um recurso de acessibilidade.")
    print("-Agora o programa processa letras em maiusculo.")
    print("")
    print("\033[32m"+"__________________Versão 3.0__________________"+"\033[0;0m")
    print("-Agora o programa processa números.")
    print("-Agora o programa processa simbolos especiais.")
    print("-Alguns aspectos da mecanica foram melhorados.")

def saircod():
    aperte = input("Digite " + "\033[31m" +
                   'sair' + "\033[0;0m" + " para fechar: ")
    while (aperte != 'sair'):
        aperte = input("Comando inválido - Digite sair para fechar: ")

# Condição para ver os updates e Instrução para encerrar o programa
up = input('Você gostaria de ver os updates desse código (s/n): ')
if (up == 's'):
    os.system('cls') or None
    notasupdate()
    print("")
    saircod()
else:
    print("")