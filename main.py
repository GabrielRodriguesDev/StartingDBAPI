import MySQLdb
user = 'root'
password = 'fx870'
database = 'son_python_db_api'
host = '127.0.0.1'
port = '3306'

'''
#PEP 249 
É um padrão posto sobre as libs do python para que elas sigam um mesmo padrão,
Caso queiramos alterar a lib sobre a qual o projeto está rodando,
não teriamos que mudar por exemplo a função a baixo, pois a sua contrução (parametros e retorno),
seguem a PEP 249, então qualquer uma que atenda a essa PEP terá esse padrão.
'''

db = MySQLdb.connect(
        user=user, 
        password=password, 
        db=database
        #host=host,
        #port=port
        )

print('Conexão feita com sucesso')
'''
#Metodos de uma instancia Connection
db.commit()
db.rollback()
db.cursor()
db.close()
'''

'''#Cursor
Contudo, existem situações em que trazer os registros de uma só vez não é conveniente ou possível para realizar,
certos tipos de operações, onde é necessário obter resultado de cada linha uma a uma. Nestes casos os SGBD’s atuais,
fornecem um recurso bastante interessante, chamado cursor.

O cursor é uma instrução SELECT que será acessada linha a linha através de um laço While e alguns comandos,
específicos para cursores e é utilizado normalmente em procedimentos armazenados (stored procedures).
'''

cursor = db.cursor() #Gerando uma nova instancia de um cursor

row_affected = cursor.execute('SELECT * FROM bank_accounts')
print(row_affected)#A principio o cursor retorna a "Quantidade de linhas afetadas"


rows = cursor.fetchall()#Buscando tudo do cursor  e aplicando a tupla de resultados na variavel

for row in rows:#Iterando sobre a tupla
    print(row)