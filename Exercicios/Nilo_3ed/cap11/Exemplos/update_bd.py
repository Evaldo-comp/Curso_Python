import sqlite3
from contextlib import closing

with sqlite3.connect("agenda.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("""update agenda
                                set telefone = '12345-6789'
                               """)
    conexao.commit()