
import os 
os.system("pip install mysql-connector-python") 

import mysql.connector 
import datetime 

import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

def connectBD(host, usuario, senha, DB):
    connection = mysql.connector.connect( 
        host = host, 
        user= usuario, 
        password=senha, 
        database=DB 
    ) 
    return connection


def insertEmb(material, tamanho, preco, pizza_ID, conn):
    connection = conn 
    cursor = connection.cursor()  
    sql = "INSERT INTO Embalagem (material, tamanho, preco, pizza_ID) VALUES (%s, %s, %s, %s)"
    data = (
    material,
    tamanho,
    preco,
    pizza_ID
    )
    cursor.execute(sql, data)
    connection.commit() 

    userid = cursor.lastrowid 

    cursor.close()
    connection.close() 
    print("Foi cadastrado a nova embalagem de ID: ", userid)

def insertPiz(sabor, preco, descricao, tamanho, pizzaiolo_ID, conn):
    connection = conn 
    cursor = connection.cursor()  
    sql = "INSERT INTO Pizza (sabor, preco, descricao, tamanho, pizzaiolo_ID) VALUES (%s, %s, %s, %s, %s)"
    data = (
    sabor,
    preco,
    descricao,
    tamanho,
    pizzaiolo_ID
    )
    cursor.execute(sql, data)
    connection.commit() 

    userid = cursor.lastrowid 

    cursor.close()
    connection.close() 
    print("Foi cadastrado a nova pizza de ID: ", userid)

def insertIngr(ingredientes, pizza_ID, conn):
    connection = conn 
    cursor = connection.cursor()  
    sql = "INSERT INTO Ingredientes (ingredientes, pizza_ID) VALUES (%s, %s)"
    data = (
    ingredientes,
    pizza_ID
    )
    cursor.execute(sql, data)
    connection.commit() 

    userid = cursor.lastrowid 

    cursor.close()
    connection.close() 
    print("Foi cadastrado o novo ingrediente de ID: ", userid)

def insertRec(intrucoes, autor, pizza_ID, conn):
    connection = conn 
    cursor = connection.cursor()  
    sql = "INSERT INTO Receita (intrucoes, autor, pizza_ID) VALUES (%s, %s, %s)"
    data = (
    intrucoes,
    autor,
    pizza_ID
    )
    cursor.execute(sql, data)
    connection.commit() 

    userid = cursor.lastrowid 

    cursor.close()
    connection.close() 
    print("Foi cadastrado a nova receita de ID: ", userid)

def insertPizzaiolo(nome, salario_bruto, conn):
    connection = conn 
    cursor = connection.cursor()      
    sql = "INSERT INTO Pizzaiolo (nome, salario_bruto) VALUES (%s, %s)"
    data = (
    nome,
    salario_bruto
    )
    cursor.execute(sql, data)
    connection.commit() 

    userid = cursor.lastrowid 

    cursor.close()
    connection.close() 
    print("Foi cadastrado o novo pizzaiolo de ID: ", userid)


def read_BD(table, conn):
    connection = conn 
    cursor = connection.cursor() 

    sql = f"SELECT * FROM {table}" 

    cursor.execute(sql) 
    results = cursor.fetchall() 

    cursor.close() 
    connection.close() 

    for result in results: #Ler os registros existentes com o select
        print(result) #imprime os registros existentes


def updateEmb(material, tamanho, preco, pizza_ID, ID, conn):
    connection = conn 
    cursor = connection.cursor()

    sql = "UPDATE Embalagem SET material = %s, tamanho = %s, preco = %s, pizza_ID = %s WHERE ID = %s"
    data = (material, 
            tamanho,
            preco,
            pizza_ID,
            ID
            )

    cursor.execute(sql, data) 
    connection.commit() 

    recordsaffected = cursor.rowcount 

    cursor.close()
    connection.close() 

    print(recordsaffected, " registros alterados")

def updatePiz(sabor, preco, descricao, tamanho, pizzaiolo_ID, ID, conn):
    connection = conn 
    cursor = connection.cursor()

    sql = "UPDATE Pizza SET sabor = %s, preco = %s, descricao = %s, tamanho = %s, pizzaiolo_ID = %s WHERE ID = %s"
    data = (sabor, 
            preco,
            descricao,
            tamanho,
            pizzaiolo_ID,
            ID
            )

    cursor.execute(sql, data) 
    connection.commit() 

    recordsaffected = cursor.rowcount 

    cursor.close()
    connection.close() 

    print(recordsaffected, " registros alterados")

def updateIngr(ingredientes, pizza_ID, ID, conn):
    connection = conn 
    cursor = connection.cursor()

    sql = "UPDATE Ingredientes SET ingredientes = %s, pizza_ID = %s WHERE ID = %s"
    data = (ingredientes, 
            pizza_ID,
            ID
            )

    cursor.execute(sql, data) 
    connection.commit() 

    recordsaffected = cursor.rowcount 

    cursor.close()
    connection.close() 

    print(recordsaffected, " registros alterados")

def updateRec(intrucoes, autor, pizza_ID, ID, conn):
    connection = conn 
    cursor = connection.cursor()

    sql = "UPDATE Receita SET intrucoes = %s, autor = %s, pizza_ID = %s WHERE ID = %s"
    data = (intrucoes, 
            autor,
            pizza_ID,
            ID
            )

    cursor.execute(sql, data) 
    connection.commit() 

    recordsaffected = cursor.rowcount 

    cursor.close()
    connection.close() 

    print(recordsaffected, " registros alterados")

def updatePizzaiolo(nome, salario_bruto, ID, conn):
    connection = conn 
    cursor = connection.cursor()

    sql = "UPDATE Pizzaiolo SET nome = %s, salario_bruto = %s WHERE ID = %s"
    data = (nome, 
            salario_bruto,
            ID
            )

    cursor.execute(sql, data) 
    connection.commit() 

    recordsaffected = cursor.rowcount 

    cursor.close()
    connection.close() 

    print(recordsaffected, " registros alterados")


def delete_BD(table, id, conn):
    connection = conn 
    cursor = connection.cursor() 

    sql = "DELETE FROM %s WHERE id = %s"
    data = (table,
            id)

    cursor.execute(sql, data) 
    connection.commit()

    recordsaffected = cursor.rowcount #Obtém o número de linhas afetadas

    cursor.close()
    connection.close() 

    print(recordsaffected, " registros excluídos")


import time
while(True): 
    os.system("cls")
    print (":::: Manipulação de dados da tabela Pizzaria ::::")
    print ("1 - Inserir na tabela (Insert)")
    print ("2 - Leitura da tabela (Select)")
    print ("3 - Atualização da tabela (Update)")
    print ("4 - Excluir da tabela (Delete)")
    print ("0 - Sair")
    opcao = int(input("Digite a opcao que deseja: "))

    password = os.getenv("passwordBD")
    bd = os.getenv("bdName")

    if opcao == 0 :
        break

#Colocar uma opcao para voltar para o menu principal caso tenha feita a escolha de manipulacao errada
#Ao inves de ficar esperando o time sleep, colocar pra caso o usuario terminou de visualizar, teclar qq coisa do teclado para sair

    elif(opcao == 1):
        opcTab = int(input("\n 1 - Embalagem \n 2 - Pizza \n 3 - Ingrediente \n 4 - Receita \n 5 - Pizzaiolo \n Escolha em qual tabela voce deseja inserir: "))
        connection = connectBD("localhost", "root", password, bd) 
        if opcTab == 1:
            material = input("Insira o nome do material da embalagem: ")
            tamanho = input("Insira o tamanho da embalagem: ")
            preco = float(input("Insira o preco da embalagem (xx.xx): "))
            pizza_ID = int(input("Insira o ID da pizza que sera colocada na embalagem: "))
            insertEmb(material, tamanho, preco, pizza_ID, connection)

        elif opcTab == 2:
            sabor = input("Insira o nome do sabor da pizza: ")
            preco = float(input("Insira o preco da pizza (xx.xx): "))
            descricao = input("Insira a descricao da pizza: ")
            tamanho = input("Insira o tamanho da pizza: ")
            pizzaiolo_ID = int(input("Insira o ID do pizzaiolo que produzira a pizza: "))
            insertPiz(sabor, preco, descricao, tamanho, pizzaiolo_ID, connection)

        elif opcTab == 3:
            ingredientes = input("Insira o nome dos ingredientes da pizza: ")
            pizza_ID = int(input("Insira o ID da pizza em que ira esses ingredientes: "))
            insertIngr(ingredientes, pizza_ID, connection)

        elif opcTab == 4:
            intrucoes = input("Insira as instrucoes da pizza: ")
            autor = input("Insira a autor da receita da pizza: ")
            pizza_ID = int(input("Insira o ID da pizza que tem esta receita: "))
            insertRec(intrucoes, autor, pizza_ID, connection)

        elif opcTab == 5:
            nome = input("Insira o nome do pizzaiolo: ")
            salario_bruto = float(input("Insira o salario bruto do pizzaiolo (xxxx.xx): "))
            insertPizzaiolo(nome, salario_bruto, connection)
        
        else:
            print("Digite uma opcao valida!")
            quit()
        time.sleep(5)

    elif (opcao == 2):  
        connection = connectBD("localhost", "root", password, bd) 
        opcTab = int(input("\n 1 - Embalagem \n 2 - Pizza \n 3 - Ingrediente \n 4 - Receita \n 5 - Pizzaiolo \n Escolha em qual tabela voce deseja visualizar: "))
        if opcTab == 1:
            table = "Embalagem"
            read_BD(table, connection)

        elif opcTab == 2:
            table = "Pizza"
            read_BD(table, connection)

        elif opcTab == 3:
            table = "Ingredientes"
            read_BD(table, connection)

        elif opcTab == 4:
            table = "Receita"
            read_BD(table, connection)

        elif opcTab == 5:
            table = "Pizzaiolo"
            read_BD(table, connection)
        
        else:
            print("Digite uma opcao valida!")
            quit()

        time.sleep(5)

    elif (opcao == 3):
        connection = connectBD("localhost", "root", password, bd)     
        opcTab = int(input("\n 1 - Embalagem \n 2 - Pizza \n 3 - Ingrediente \n 4 - Receita \n 5 - Pizzaiolo \n Escolha em qual tabela voce deseja atualizar os dados: "))
        if opcTab == 1:
            newMaterial = input("Insira o novo nome do material da embalagem: ")
            newTamanho = input("Insira o novo tamanho da embalagem: ")
            newPreco = float(input("Insira o novo preco da embalagem (xx.xx): "))
            pizza_ID = int(input("Insira o ID da pizza que sera colocada na embalagem: "))
            newID = int(input("Insira o ID da embalagem que quer atualizar: "))
            updateEmb(newMaterial, newTamanho, newPreco, pizza_ID, newID, connection)

        elif opcTab == 2:
            newSabor = input("Insira o novo nome do sabor da pizza: ")
            newPreco = float(input("Insira o novo preco da pizza (xx.xx): "))
            newDescricao = input("Insira a nova descricao da pizza: ")
            newTamanho = input("Insira o novo tamanho da pizza: ")
            pizzaiolo_ID = int(input("Insira o ID do pizzaiolo que produzira a pizza: "))
            newID = int(input("Insira o ID da pizza que quer atualizar: "))
            updatePiz(newSabor, newPreco, newDescricao, newTamanho, pizzaiolo_ID, newID, connection)

        elif opcTab == 3:
            newIngredientes = input("Insira os novos nomes dos ingredientes da pizza: ")
            pizza_ID = int(input("Insira o ID da pizza em que ira esses ingredientes: "))
            newID = int(input("Insira o ID do ingrediente que quer atualizar: "))
            updateIngr(newIngredientes, pizza_ID, newID, connection)

        elif opcTab == 4:
            newIntrucoes = input("Insira as novas instrucoes da pizza: ")
            newAutor = input("Insira o novo autor da receita da pizza: ")
            pizza_ID = int(input("Insira o ID da pizza que tem esta receita: "))
            newID = int(input("Insira o ID da receita que quer atualizar: "))
            updateRec(newIntrucoes, newAutor, pizza_ID, newID, connection)

        elif opcTab == 5:
            newNome = input("Insira o novo nome do pizzaiolo: ")
            newSalario_bruto = float(input("Insira o novo salario bruto do pizzaiolo (xxxx.xx): "))
            newID = int(input("Insira o ID da embalagem que quer atualizar: "))
            updatePizzaiolo(newNome, newSalario_bruto, newID, connection)
        
        else:
            print("Digite uma opcao valida!")
            quit()

        time.sleep(5)

    elif (opcao == 4):
        connection = connectBD("localhost", "root", password, bd)
        opcTab = int(input("\n 1 - Embalagem \n 2 - Pizza \n 3 - Ingrediente \n 4 - Receita \n 5 - Pizzaiolo \n Escolha em qual tabela voce deseja deletar os dados: "))
        if opcTab == 1:
            table = "Embalagem"
            searchID = int(input("Insira o ID da embalagem que quer deletar: "))
            updateEmb(table, searchID, connection)

        elif opcTab == 2:
            table = "Pizza"
            searchID = int(input("Insira o ID da pizza que quer deletar: "))
            updateEmb(table, searchID, connection)

        elif opcTab == 3:
            table = "Ingrediente"
            searchID = int(input("Insira o ID do ingrediente que quer deletar: "))
            updateEmb(table, searchID, connection)

        elif opcTab == 4:
            table = "Receita"
            searchID = int(input("Insira o ID da receita que quer deletar: "))
            updateEmb(table, searchID, connection)


        elif opcTab == 5:
            table = "Pizzaiolo"
            searchID = int(input("Insira o ID do pizzaiolo que quer deletar: "))
            updateEmb(table, searchID, connection)


        else:
            print("Digite uma opcao valida!")
            quit()
        time.sleep(5)

    else: 
        print("Opcao invalida")