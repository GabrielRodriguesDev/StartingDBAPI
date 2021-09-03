import MySQLdb
user = 'root'
password = 'fx870'
database = 'son_python_db_api'
host = '127.0.0.1'
port = '3306'


#PEP 249 é um padrão posto sobre as libs do python para que elas sigam um mesmo padrão,
#Caso queiramos alterar a lib sobre a qual o projeto está rodando,
#não teriamos que mudar por exemplo a função a baixo, pois a sua contrução (parametros e retorno),
#seguem a PEP 249, então qualquer uma que atenda a essa PEP terá esse padrão.

db = MySQLdb.connect(
        user=user, 
        password=password, 
        db=database
        #host=host,
        #port=port
        )

print('Conexão feita com sucesso')
db.commit()
db.rollback()
db.cursor()
db.close()


