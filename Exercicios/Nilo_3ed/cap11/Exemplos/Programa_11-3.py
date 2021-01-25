# Uso do with para fechar a conexão

import sqlite3
from contextlib import closing

""""with sqlite3.connect("agenda.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("select * from agenda")
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                break
            print(f"Nome: {resultado[0]}\nTelefone: {resultado[1]}")"""


with sqlite3.connect("precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("select * from precos")
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                break
            print(f"Nome: {resultado[0]}\nTelefone: {resultado[1]}")
