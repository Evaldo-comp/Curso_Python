import sqlite3
conexão = sqlite3.connect("agenda.db")
cursor = conexão.cursor()
cursor.execute('''
        create table agenda(
            nome text,
            telefone text)
        ''')
cursor.execute('''
        insert into agenda(nome, telefone)
            values(?, ?)
            ''', ("Evaldo", "1234-5678"))
conexão.commit()
cursor.close()
conexão.close()