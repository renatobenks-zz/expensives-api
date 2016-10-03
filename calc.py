#!/bin/env python3
#coding: utf-8

from operator import itemgetter

def transforma_csv_em_lista(dividas):
    ''' Recebe os dados que vieram de um arquivo csv e devolve-os numa lista de tuplas'''
    lista = []
    for divida in dividas:
        nome, valor = divida.split(';')
        lista.append((nome, float(valor)))
    return sorted(lista)

def agrupa_dividas_por_nome(dividas):
    ''' Recebe os dados das dividas dos clientes e os agrupa num dicionário por nome do cliente'''
    dic = {}
    for divida in dividas:
        group_dividas = []
        if divida[0] in dic.keys():
            group_dividas = dic[divida[0]]
        group_dividas.append(divida[1])
        dic[divida[0]] = group_dividas
    return dic

def soma_dividas_por_nome(dividas):
    ''' Recebe o dicionário com as dívidas dos clientes e devolve um dicionário com a soma da dívida de cada cliente'''
    for divida in dividas:
        dividas[divida] = round(sum(dividas[divida]), 2)
    return dividas

def top_dividas(dividas, n=None):
    '''Recebe o dicionário com os totais e o ordena, devolvendo os n maiores devedores.
    Se n não for passado, devolve todos.'''
    return sorted(dividas.items(), key=itemgetter(1), reverse=True)[:n]

if __name__ == '__main__':
    csv = open('selma_contas.csv').readlines()
    lista_de_dividas = transforma_csv_em_lista(csv)
    dic_dividas = agrupa_dividas_por_nome(lista_de_dividas)
    dic_dividas_cliente = soma_dividas_por_nome(dic_dividas)
    top_n = 4
    lista_top_dividas = top_dividas(dic_dividas_cliente, top_n)

    print('Lista dos %d maiores devedores: ' %(top_n))
    for cliente, valor in lista_top_dividas:
        print('%-30s: R$%5.2f' %(cliente, valor))
