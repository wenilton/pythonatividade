import pyodbc
import tkinter
def read():
    print("Read")
   # cursor = retornar_conexao_sql()
    cursor.execute("Select * from dbo.imc")
    for row in cursor:
        print(f'row = {row}')
    print()

def create(nome,endere,peso,altura,imc):
    print("Create")
    cursor = retornar_conexao_sql()
    query = """INSERT INTO dbo.imc (nome, endereco, peso, altura,imc) 
                                    VALUES (?, ?, ?, ?, ?) """

    recordTuple = (nome, endere,peso,altura,imc)
    cursor.execute(query, recordTuple)
    cursor.commit()
    print("Inserido com sucesso")
def retornar_conexao_sql():
    server = "endBanco"
    database = "imc"
    username = "login"
    password = "senha"
    string_conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';UID='+username+';PWD='+ password
    #string_conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';Trusted_Connection=yes;'
    return pyodbc.connect(string_conexao)
    #return conexao.cursor()

conexao = retornar_conexao_sql()
cursor = conexao.cursor()

#reate()
read()
