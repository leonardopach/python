from mysql.connector import connect


conexao = connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='senha123',
    auth_plugin='mysql_native_password'
)

print(conexao)
