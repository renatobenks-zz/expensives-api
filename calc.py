#!/bin/env python3
# coding: utf-8

import json
import sys
import pprint
from operator import itemgetter


def transforma_csv_em_lista(dividas):
    lista = []
    for divida in dividas:
        nome, valor = divida.split(';')
        lista.append((nome, float(valor)))
    return sorted(lista)


def agrupa_dividas_por_nome(dividas):
    dic = {}
    for divida in dividas:
        group_dividas = []
        if divida[0] in dic.keys():
            group_dividas = dic[divida[0]]
        group_dividas.append(divida[1])
        dic[divida[0]] = group_dividas
    return dic


def soma_dividas_por_nome(dividas):
    for divida in dividas:
        dividas[divida] = round(sum(dividas[divida]), 2)
    return dividas


def top_dividas(dividas, n=None):
    return sorted(dividas.items(), key=itemgetter(1), reverse=True)[:n]


def calc():
    csv = open('selma_contas.csv').readlines()
    lista_de_dividas = transforma_csv_em_lista(csv)
    dic_dividas = agrupa_dividas_por_nome(lista_de_dividas)
    soma = soma_dividas_por_nome(dic_dividas)
    if len(sys.argv) == 2 and sys.argv[1] == 'json':
        generateJSON(soma)
        print('JSON parsed and generated')
    else:
        print('Object returned with sum of expenses:')
        pprint.pprint(soma)


def generateJSON(dividas):
    dividas = {
        'name': 'Lanchonete da Selma',
        'expenses': dividas
    }
    with open('build/mongo.json', 'w') as fb:
        json.dump(dividas, fb)
    fb.close()


if __name__ == '__main__':
    calc()
