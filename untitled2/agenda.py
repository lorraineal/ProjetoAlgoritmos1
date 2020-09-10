import sys
#import time
#import numpy as np
#import matplot.pyplot as plt



TODO_FILE = '/home/lorraine/PycharmProjects/untitled2/todo.txt'
ARCHIVE_FILE = 'done.txt'

RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"
YELLOW = "\033[0;33m"

ADICIONAR = 'a'
REMOVER = 'r'
FAZER = 'f'
PRIORIZAR = 'p'
LISTAR = 'l'


class Compromisso:
    ################ COMPLETAR
    def __init__(self):
        self.data = ""
        self.hora = ""
        self.pri = ""
        self.descricao = ""
        self.contexto = ""
        self.projeto = ""

        return


# Imprime texto com cores. Por exemplo, para imprimir "Oi mundo!" em vermelho, basta usar
#
# printCores('Oi mundo!', RED)
# printCores('Texto amarelo e negrito', YELLOW + BOLD)

def printCores(texto, cor):
    print(cor + texto + RESET)


# Adiciona um compromisso aa agenda. Um compromisso tem no minimo
# uma descrição. Adicionalmente, pode ter, em caráter opcional, uma
# data (formato DDMMAAAA), um horário (formato HHMM), uma prioridade de A a Z,
# um contexto onde a atividade será realizada (precedido pelo caractere
# '@') e um projeto do qual faz parte (precedido pelo caractere '+'). Esses
# itens opcionais podem ser implementados como uma tupla, dicionário  ou objeto. A função
# recebe esse item através do parâmetro extras.
#
# extras tem como elementos data, hora, prioridade, contexto, projeto
#
def adicionar(compromisso):
    # não é possível adicionar uma atividade que não possui descrição.
    #print(compromisso)
    if not compromisso.descricao:
        #print("False")
        return False

    ################ COMPLETAR
    #print(compromisso.data + " " + compromisso.hora + " " + compromisso.pri + " " + compromisso.descricao + " " + compromisso.contexto + " " + compromisso.projeto)
    # Escreve no TODO_FILE.
    try:
        fp = open(TODO_FILE, 'a')
        fp.write(str(compromisso.data) + " " + str(compromisso.hora) + " " + str(compromisso.pri) + " " + compromisso.descricao + " " + str(compromisso.contexto) + " " + str(compromisso.projeto) + "\n")
    except IOError as err:
        print("Não foi possível escrever para o arquivo " + TODO_FILE)
        print(err)
        return False
    finally:
        fp.close()

    return True


# Valida a prioridade.
def prioridadeValida(prioridade):
    if len(prioridade) != 3:
        return False
    else:
        if prioridade[0] == "(" and prioridade[2] == ")":
            return True
        else:
            return False

# Valida a hora. Consideramos que o dia tem 24 horas, como no Brasil, ao invés
# de dois blocos de 12 (AM e PM), como nos EUA.
def horaValida(horaMin):
    #print("hora Minin =", horaMin)
    if len(horaMin) != 4 or not soDigitos(horaMin):
        return False
    else:
        if (horaMin[0] == "0" and horaMin[2] <= "5"):
            #print("true")
            return True
        elif (horaMin[0] == "1" and horaMin[2] <= "5"):
            #print("true")
            return True
        elif (horaMin[0] == "2" and horaMin[1] <= "3") and (horaMin[2] <= "5"):
            #print("true")
            return True
        else:
            return False

# Valida datas. Verificar inclusive se não estamos tentando
# colocar 31 dias em fevereiro. Não precisamos nos certificar, porém,
# de que um ano é bissexto.
def dataValida(data):
    if len(data) != 8 or not soDigitos(data):
        return False
    else:
        #data[0] ~ data[1] digitos dos dias
        #data[2] ~ data[3] digitos dos meses
        #data[4] ~ data[5] ~ data[6] ~ data[7] digitos do ano

        if (data[0] == "0" and data[1] == "0") or (data[0] > "3"):
            return False
        else:
            if (data[0] == "3") and (data[1] > "2" ):
                return False
            else:
                if (data[2] >= "1") and (data[3] > "2"):
                    return False
                else:
                    if(data[0] > "2" and data[3] == "2" and data[2] == "0"):
                        return False
                    elif (data[0] >= "3" and data[1] > "0") and ( data[3] == "4" or data[3] == "6" or data[3] == "9"  or (data[2] =="1" and data[3] == "1")):
                        return False
                    elif (data[0] >= "3" and data[1] > "1") and ( data[3] == "1" or data[3] == "3" or data[3] == "5" or data[3] == "7" or data[3] == "8" or (data[2] == "1" and data[3] == "0") or (data[2] == "1" and data[3] == "2")):
                        return False
                    else:
                        return True

# Valida que o string do projeto está no formato correto.
def projetoValido(projeto):
    print(projeto)
    if len(projeto) < 2:
        return False
    else:
        if projeto[0] == "+":
            return True
        else:
            return False

# Valida que o string do contexto está no formato correto.
def contextoValido(contexto):
    if len(contexto) < 2:
        return False
    else:
        if contexto[0] == "@":
            return True
        else:
            return False

# Valida que a data ou a hora contém apenas dígitos, desprezando espaços
# extras no início e no fim.
def soDigitos(numero):
    if type(numero) != str:
        return False
    for x in numero:
        if x < '0' or x > '9':
            return False
    return True


# Dadas as linhas de texto obtidas a partir do arquivo texto todo.txt, devolve
# uma lista de tuplas contendo os pedaços de cada linha, conforme o seguinte
# formato:
#
# (descrição, prioridade, (data, hora, contexto, projeto))
#
# É importante lembrar que linhas do arquivo todo.txt devem estar organizadas de acordo com o
# seguinte formato:
#
# DDMMAAAA HHMM (P) DESC @CONTEXT +PROJ
#
# Todos os itens menos DESC são opcionais. Se qualquer um deles estiver fora do formato, por exemplo,
# data que não tem todos os componentes ou prioridade com mais de um caractere (além dos parênteses),
# tudo que vier depois será considerado parte da descrição.
def organizar(linhas):
    #print(linhas)
    itens = []

    for l in linhas:
        #print("l=",l)
        data = ''
        hora = ''
        pri = ''
        desc = ''
        contexto = ''
        projeto = ''


        l = l.strip()  # remove espaços em branco e quebras de linha do começo e do fim
        #print("l strip=", l )
        tokens = l.split()  # quebra o string em palavras
        #print("tokens=", tokens)

        #Istanciando compromisso
        compromisso = Compromisso()

        horaLista = list(filter(lambda x: (x[0]) in '0123456789' and (len(x) ==4), tokens))
        #Solved IndexError: list index out of range
        if not horaLista:
            print("")
        else:
            hora = horaLista[0]
        #print("Resultado da funcao", horaValida(hora))

        if horaValida(hora) == True:
            compromisso.hora = hora
            tokens.remove(hora)

        dataLista = list(filter(lambda x: (x[0]) in '0123456789' and (len(x) ==8), tokens))
        if not dataLista:
            print("")
        else:
            data = dataLista[0]
        #print(data)
        #print("Resultado da funcao data", dataValida(data))
        if dataValida(data) == True:
            compromisso.data = data
            tokens.remove(data)


        projetoLista = list(filter(lambda x: (x[0]) in '+' and (len(x) >= 2), tokens))
        #print(projetoLista)
        if not projetoLista:
            print("")
        else:
            projeto = projetoLista[0]

        #print("Resultado da funcao projeto", projetoValido(projeto))

        if projetoValido(projeto) == True:
            compromisso.projeto = projeto
            tokens.remove(projeto)


        contextoLista = list(filter(lambda x: (x[0]) in '@' and (len(x) >= 2), tokens))
        if not contextoLista:
            print("")
        else:
            contexto = contextoLista[0]

        #print(contexto)
        #print("Resultado de contexto", contextoValido(contexto))

        if (contextoValido(contexto) == True):
            compromisso.contexto = contexto
            tokens.remove(contexto)

        prioridadeLista = list(filter(lambda x: (x[0]) in '(' and ')' and (len(x) == 3), tokens))
        #print(type(prioridadeLista))
        if not prioridadeLista:
            print("")
        else:
            pri = prioridadeLista[0]
        #print(pri)
        #print("Resultado de prioridade", prioridadeValida(pri))

        if(prioridadeValida(pri) == True):
            compromisso.pri = pri
            tokens.remove(pri)

        descricao = " ".join(tokens)
        #print(descricao)
        #descricao = StrA
        #print(descricao)
        #if not descricao:
        #    print("Todos os compromissos devem ter uma descricao")
        #    exit(0)
        #else:
        compromisso.descricao = descricao

        #itens.append(data)
        #itens.append(hora)
        #itens.append(pri)
        #itens.append(descricao)
        #itens.append(contexto)
        #itens.append(projeto)


        # A linha abaixo inclui em itens um objeto contendo as informações relativas aos compromissos
        # nas várias linhas do arquivo.
        itens.append(compromisso)

    #print(itens)
    return itens

# Datas e horas são armazenadas nos formatos DDMMAAAA e HHMM, mas são exibidas
# como se espera (com os separadores apropridados).
#
# Uma extensão possível é listar com base em diversos critérios: (i) atividades com certa prioridade;
# (ii) atividades a ser realizadas em certo contexto; (iii) atividades associadas com
# determinado projeto; (vi) atividades de determinado dia (data específica, hoje ou amanhã). Isso não
# é uma das tarefas básicas do projeto, porém.
def listar():
    ################ COMPLETAR
    #fp = open("todo.txt", "r")

    return


def ordenarPorDataHora(itens):
    ################ COMPLETAR

    return itens


def ordenarPorPrioridade(itens):
    ################ COMPLETAR

    return itens


def fazer(num):
    ################ COMPLETAR
    #atividade.pop(num)

    return


def remover(numero):
    ################ COMPLETAR
    #compromisso.pop(numerox)
    #if numerox != ncompromisso:
        #print("Numero invalido, a remoção nao poderá ocorer")
    return

# prioridade é uma letra entre A a Z, onde A é a mais alta e Z a mais baixa.
# num é o número da atividade cuja prioridade se planeja modificar, conforme
# exibido pelo comando 'l'.

def priorizar(num, prioridade):
    #prioridade = letra
    #if num != compromisso:
        #print("Erro, essa atividade não existe, logo não pode receber priorização")
    ################ COMPLETAR

    return


def desenhar(dias):
    #inicia a construção do grafico de barra dando as coordenadas através dos argumentos.

    #plt.bar(dias, tarefasCompletadas, color="red")

    #define o eixo x e ye o parâmetro que produzirá o elementro do gráfico.
    #plt.xticks("dias")

    #adiciona as barras do eixo x e y.
    #plt.ylabel("tarefasCompletadas")
    #plt.xlabel("diasdeCompromisso")

    #adiciona o título do gráfico
    #plt.title("Compromissos")

    #mostra o gráfico na tela.
    #plt.show()

    ################ COMPLETAR

    return


# Esta função processa os comandos e informações passados através da linha de comando e identifica
# que função do programa deve ser invocada. Por exemplo, se o comando 'adicionar' foi usado,
# isso significa que a função adicionar() deve ser invocada para registrar a nova atividade.
# O bloco principal fica responsável também por tirar espaços em branco no início e fim dos strings
# usando o método strip(). Além disso, realiza a validação de horas, datas, prioridades, contextos e
# projetos.
def processarComandos(comandos):
    if comandos[1] == "a" or comandos[1] == "A":
        print("ADICIONAR")
        comandos.pop(0)  # remove 'agenda.py'
        comandos.pop(0)  # remove 'adicionar'
        #print(comandos)
        itemParaAdicionar = organizar([' '.join(comandos)])[0]
        #print(itemParaAdicionar)
        arquivo = adicionar(itemParaAdicionar)  # Objeto compromisso
        print(arquivo)

    elif comandos[1] == "l" or comandos[1] == "L":
        print("LISTAR")
        return
        ################ COMPLETAR

    elif comandos[1] == "r" or comandos[1] == "R":

        print("REMOVER")
        #remover(numero)
        return

        ################ COMPLETAR

    elif comandos[1] == "f" or comandos[1] == "F":
     #   print("FAZER")
      #  fazer(num)
        return

        ################ COMPLETAR

    elif comandos[1] == "p" or comandos[1] == "P":
     #   print("PRIORIZAR")
      #  priorizar(num, prioridade)

         return

    elif comandos[1] == "l" or comandos[1] == "L":
        listar()
      #  return

        ################ COMPLETAR

    #elif comandos[1] == "g" or comandos[1] == "G":
    #   desenhar(dias)
     #   if dias < 0:
      #      print("Erro, numero de dias invalido")
    else:
        print("Comando inválido.")




# sys.argv é uma lista de strings onde o primeiro elemento é o nome do programa
# invocado a partir da linha de comando e os elementos restantes são tudo que
# foi fornecido em sequência. Por exemplo, se o programa foi invocado como
#
# python3 agenda.py a Mudar de nome.
#
# sys.argv terá como conteúdo
#


def main():
    # ['agenda.py', 'a', 'Mudar', 'de', 'nome']
    # examplos DDMMAAAA HHMM (PRI) DESC @CTX +PROJ
    #print(sys.argv)
    processarComandos(sys.argv)






if __name__ == "__main__":
    main()





