import mysql.connector


def createTables():

    use = "use projetobdcrud;"
    cursor.execute(use)
    connection.commit()

    arbitro = """create table if not exists arbitro (
	idArbitro int unsigned auto_increment,
	nome varchar(80) not null,
	dataNasc date not null,
	qtdJogos int not null,
	dataEstreia date not null,
	primary key (idArbitro)); """

    cursor.execute(arbitro)
    connection.commit()

    estadio = """create table if not exists estadio (
	idEstadio int unsigned auto_increment,
	nome varchar(80) not null,
	dataInaug date not null,
	valor float not null,
	capacidade int not null,
	primary key(idEstadio));"""

    cursor.execute(estadio)
    connection.commit()

    lesao = """create table if not exists lesao (
	idLesao int unsigned auto_increment,
	descricao varchar(150) not null,
	primary key (idLesao));"""

    cursor.execute(lesao)
    connection.commit()

    comp = """create table if not exists competicao (
	idComp int unsigned auto_increment,
	descricao varchar(150) not null,
	primary key (idComp));"""

    cursor.execute(comp)
    connection.commit()

    tecnico = """create table if not exists tecnico (
	idTecnico int unsigned auto_increment,
	nome varchar(80) not null,
	dataNasc date not null,
	qtdJogos int not null,
	dataEstreia date not null,
	primary key (idTecnico));"""

    cursor.execute(tecnico)
    connection.commit()

    clube = """create table if not exists clube (
	idClube int unsigned auto_increment,
	nome varchar(80) not null,
	dataFund date not null,
	idEstadio int unsigned,
	idTecnico int unsigned not null,
	primary key (idClube),
	foreign key (idEstadio) references estadio (idEstadio),
	foreign key (idTecnico) references tecnico (idTecnico));"""

    cursor.execute(clube)
    connection.commit()

    jogador = """create table if not exists jogador (
	idJogador int unsigned auto_increment,
	nome varchar(80) not null,
	dataNasc date not null,
	posicao varchar(20) not null,
	qtdJogos int not null,
	qtdGols int not null,
	qtdAssist int not null,
	idClube int unsigned,
	primary key (idJogador),
	foreign key (idClube) references clube (idClube));"""

    cursor.execute(jogador)
    connection.commit()

    lesaojog = """create table if not exists LesaoJogador (
	idLesao int unsigned not null,
	idJogador int unsigned not null,
	dataLesao date not null,
	gravidade varchar(20) not null,
	regiao varchar(20) not null,
	dataRecu date,
	primary key (idLesao, idJogador),
	foreign key (idLesao) references lesao (idLesao),
	foreign key (idJogador) references jogador (idJogador));"""

    cursor.execute(lesaojog)
    connection.commit()

    jogo = """create table if not exists jogo (
	idJogo int unsigned not null,
	idClube1 int unsigned not null,
	idClube2 int unsigned not null,
	idArbitro int unsigned not null,
	resultado varchar(10),
	idComp int unsigned not null,
	primary key (idJogo),
	foreign key (idClube1) references clube (idClube),
	foreign key (idClube2) references clube (idClube),
	foreign key (idArbitro) references arbitro (idArbitro),
	foreign key (idComp) references competicao (idComp));"""

    cursor.execute(jogo)
    connection.commit()

    cartaojog = """create table if not exists CartaoJogador (
	idCartao int unsigned auto_increment,
	idJogador int unsigned not null,
	idJogo int unsigned not null,
	idArbitro int unsigned not null,
	cor varchar(20) not null,
	primary key (idCartao),
	foreign key (idJogador) references jogador (idJogador),
	foreign key (idJogo) references jogo (idJogo),
	foreign key (idArbitro) references arbitro (idArbitro));"""

    cursor.execute(cartaojog)
    connection.commit()

    cartaotec = """create table if not exists CartaoTecnico (
	idCartao int unsigned auto_increment,
	idTecnico int unsigned not null,
	idJogo int unsigned not null,
	idArbitro int unsigned not null,
	cor varchar(20) not null,
	primary key (idCartao),
	foreign key (idTecnico) references Tecnico (idTecnico),
	foreign key (idJogo) references jogo (idJogo),
	foreign key (idArbitro) references arbitro (idArbitro));"""

    cursor.execute(cartaotec)
    connection.commit()

    titulo = """create table if not exists titulo (
	idTitulo int unsigned auto_increment,
	idComp int unsigned not null,
	idClube int unsigned not null,
	ano int not null,
	idArtilheiro int unsigned not null,
	primary key (idTitulo),
	foreign key (idComp) references competicao (idComp),
	foreign key (idClube) references clube (idClube),
	foreign key (idArtilheiro) references jogador (idJogador));"""

    cursor.execute(titulo)
    connection.commit()


def menuPrincipal():

    while True:
        print('-------------------------Comandos-------------------------')
        print("1.- Create")
        print("2.- Read")
        print("3.- Update")
        print("4.- Delete")
        print("5.- Sair")
        print("----------------------------------------------------------")

        print("Digite sua opção: ")
        opcao = int(input())
        if 5 < opcao or opcao < 1:
            print("Digite um valor válido!")
        elif opcao == 5:
            print("Obrigado por me usar!")
            break
        elif opcao == 1:
            telaCreate()
        elif opcao == 2:
            telaRead()
        elif opcao == 3:
            telaUpdate()
        elif opcao == 4:
            telaDelete()
        input("Pressione enter para voltar!")


def telaCreate():
    while True:
        print('-------------------------CREATE-------------------------')
        print('1.- Arbitro')
        print('2.- Estadio')
        print('3.- Lesao')
        print('4.- Competicao')
        print('5.- Tecnico')
        print('6.- Clube')
        print('7.- Jogador')
        print('8.- LesaoJogador')
        print('9.- Jogo')
        print('10.- CartaoJogador')
        print('11.- CartaoTecnico')
        print('12.- Titulo')
        print('13.- Sair')
        print('----------------------------------------------------------')

        print("Selecione uma tabela: ")
        opcao = int(input())
        if opcao == 13:
            break
        if opcao == 1:
            print('Digite o nome do arbitro: ')
            nome = input()
            print('Digite a data de nascimento do arbitro (YYYY-MM-DD)')
            datanasc = input()
            print('Digite o numero de jogos apitados pelo arbitro')
            qtdJogos = int(input())
            print('Digite a data de estreia do arbitro (YYYY-MM-DD')
            dataEstreia = input()
            comando = f"insert into arbitro(nome, dataNasc, qtdJogos, dataEstreia) values('{nome}', '{datanasc}', {str(qtdJogos)}, '{dataEstreia}')"
            cursor.execute(comando)
            connection.commit()
        if opcao == 2:
            print('Digite o nome do estádio: ')
            nome = input()
            print('Digite a data de inaugaração do estádio (YYYY-MM-DD): ')
            dataInaug = input()
            print('Digite o valor do estádio: ')
            valor = float(input())
            print('Digite a capacidade do estádio: ')
            capac = int(input())
            comando = f"insert into estadio(nome, dataInaug, valor, capacidade) values('{nome}', '{dataInaug}', {str(valor)}, '{str(capac)}')"
            cursor.execute(comando)
            connection.commit()
        if opcao == 3:
            print("Digite a descrição da lesão")
            desc = input()
            comando = f"insert into lesao(descricao) values('{desc}')"
            cursor.execute(comando)
            connection.commit()
        input("Digite enter para voltar")


def telaRead():
    while True:
        print('-------------------------READ-------------------------')
        print('1.- Arbitro')
        print('2.- Estadio')
        print('3.- Lesao')
        print('4.- Competicao')
        print('5.- Tecnico')
        print('6.- Clube')
        print('7.- Jogador')
        print('8.- LesaoJogador')
        print('9.- Jogo')
        print('10.- CartaoJogador')
        print('11.- CartaoTecnico')
        print('12.- Titulo')
        print('13.- Sair')
        print('----------------------------------------------------------')

        print("Selecione uma tabela: ")
        opcao = int(input())

        if opcao == 1:
            comando = "select * from arbitro"
            cursor.execute(comando)
            result = cursor.fetchall()
            print(("+" + "-" * 20) * 5 + "+")
            print("| idArbitro" + " "*10 + "| nome" + " "*15 + "| data de nascimento " + "| qtd de jogos" + " "*7 + "| data de Estreia    |")
            for linha in result:
                print(("+" + "-" * 20) * 5 + "+")
                print("| " + str(linha[0]) + " "*(19-len(str(linha[0]))), end="")
                print("| " + str(linha[1]) + " " * (19 - len(str(linha[1]))), end="")
                print("| " + str(linha[2]) + " " * (19 - len(str(linha[2]))), end="")
                print("| " + str(linha[3]) + " " * (19 - len(str(linha[3]))), end="")
                print("| " + str(linha[4]) + " " * (19 - len(str(linha[4]))) + "|")
            print(("+" + "-" * 20) * 5 + "+")
        if opcao == 2:
            comando = "select * from estadio"
            cursor.execute(comando)
            result = cursor.fetchall()
            print(("+" + "-" * 20) * 5 + "+")
            print("| idEstadio" + " " * 10 + "| nome" + " " * 15 + "| data de inauguração" + "| valor" + " " * 14 + "| capacidade" + ' '*9 + "|")
            for linha in result:
                print(("+" + "-" * 20) * 5 + "+")
                print("| " + str(linha[0]) + " " * (19 - len(str(linha[0]))), end="")
                print("| " + str(linha[1]) + " " * (19 - len(str(linha[1]))), end="")
                print("| " + str(linha[2]) + " " * (19 - len(str(linha[2]))), end="")
                print("| " + str(linha[3]) + " " * (19 - len(str(linha[3]))), end="")
                print("| " + str(linha[4]) + " " * (19 - len(str(linha[4]))) + "|")
            print(("+" + "-" * 20) * 5 + "+")
        if opcao == 3:
            comando = "select * from lesao"
            cursor.execute(comando)
            result = cursor.fetchall()
            print(("+" + "-" * 20) * 2 + "+")
            print(
                "| idLesao" + " " * 12 + "| descricao" + " " * 10 + "|")
            for linha in result:
                print(("+" + "-" * 20) * 2 + "+")
                print("| " + str(linha[0]) + " " * (19 - len(str(linha[0]))), end="")
                print("| " + str(linha[1]) + " " * (19 - len(str(linha[1]))) + "|")
            print(("+" + "-" * 20) * 2 + "+")
        if opcao == 4:
            comando = "select * from competicao"
            cursor.execute(comando)
            result = cursor.fetchall()
            print(("+" + "-" * 20) * 2 + "+")
            print(
                "| idComp" + " " * 13 + "| descricao" + " " * 10 + "|")
            for linha in result:
                print(("+" + "-" * 20) * 2 + "+")
                print("| " + str(linha[0]) + " " * (19 - len(str(linha[0]))), end="")
                print("| " + str(linha[1]) + " " * (19 - len(str(linha[1]))) + "|")
            print(("+" + "-" * 20) * 2 + "+")
        if opcao == 5:
            comando = "select * from tecnico"
            cursor.execute(comando)
            result = cursor.fetchall()
            print(("+" + "-" * 20) * 5 + "+")
            print(
                "| idTecnico" + " " * 10 + "| nome" + " " * 15 + "| data de nascimento " + "| qtd de jogos" + " " * 7 + "| data de estreia" + ' ' * 4 + "|")
            for linha in result:
                print(("+" + "-" * 20) * 5 + "+")
                print("| " + str(linha[0]) + " " * (19 - len(str(linha[0]))), end="")
                print("| " + str(linha[1]) + " " * (19 - len(str(linha[1]))), end="")
                print("| " + str(linha[2]) + " " * (19 - len(str(linha[2]))), end="")
                print("| " + str(linha[3]) + " " * (19 - len(str(linha[3]))), end="")
                print("| " + str(linha[4]) + " " * (19 - len(str(linha[4]))) + "|")
            print(("+" + "-" * 20) * 5 + "+")
        if opcao == 6:
            comando = "select * from clube"
            cursor.execute(comando)
            result = cursor.fetchall()
            print(("+" + "-" * 20) * 5 + "+")
            print(
                "| idClube" + " " * 12 + "| nome" + " " * 15 + "| data de fundacao   " + "| idEstadio" + " " * 10 + "| idTecnico" + ' ' * 10 + "|")
            for linha in result:
                print(("+" + "-" * 20) * 5 + "+")
                print("| " + str(linha[0]) + " " * (19 - len(str(linha[0]))), end="")
                print("| " + str(linha[1]) + " " * (19 - len(str(linha[1]))), end="")
                print("| " + str(linha[2]) + " " * (19 - len(str(linha[2]))), end="")
                print("| " + str(linha[3]) + " " * (19 - len(str(linha[3]))), end="")
                print("| " + str(linha[4]) + " " * (19 - len(str(linha[4]))) + "|")
            print(("+" + "-" * 20) * 5 + "+")
        if opcao == 7:
            comando = "select * from jogador"
            cursor.execute(comando)
            result = cursor.fetchall()
            print(("+" + "-" * 20) * 8 + "+")
            print("| idJogador" + " "*10 + "| nome" + " "*15 + "| data de nascimento " + "| posicao" + " "*12, end="")
            print("| qtd de jogos" + ' '*7 + "| qtd de gols" + " "*8 + "| qtd de assists" + " "*5 + "| idClube" + " "*12 + "|")
            for linha in result:
                print(("+" + "-" * 20) * 8 + "+")
                print("| " + str(linha[0]) + " " * (19 - len(str(linha[0]))), end="")
                print("| " + str(linha[1]) + " " * (19 - len(str(linha[1]))), end="")
                print("| " + str(linha[2]) + " " * (19 - len(str(linha[2]))), end="")
                print("| " + str(linha[3]) + " " * (19 - len(str(linha[3]))), end="")
                print("| " + str(linha[4]) + " " * (19 - len(str(linha[4]))), end="")
                print("| " + str(linha[5]) + " " * (19 - len(str(linha[5]))), end="")
                print("| " + str(linha[6]) + " " * (19 - len(str(linha[6]))), end="")
                print("| " + str(linha[7]) + " " * (19 - len(str(linha[7]))) + "|")
            print(("+" + "-" * 20) * 8 + "+")
        if opcao == 8:
            comando = "select * from lesaoJogador"
            cursor.execute(comando)
            result = cursor.fetchall()
            print(("+" + "-" * 20) * 6 + "+")
            print(
                "| idLesao" + " "*12 + "| idJogador" + " "*10 + "| data de lesao"+" "*6 + "| gravidade"+" "*10 + "| região" +" "*13 + "| data de recuperação" + "|")
            for linha in result:
                print(("+" + "-" * 20) * 6 + "+")
                print("| " + str(linha[0]) + " " * (19 - len(str(linha[0]))), end="")
                print("| " + str(linha[1]) + " " * (19 - len(str(linha[1]))), end="")
                print("| " + str(linha[2]) + " " * (19 - len(str(linha[2]))), end="")
                print("| " + str(linha[3]) + " " * (19 - len(str(linha[3]))), end="")
                print("| " + str(linha[4]) + " " * (19 - len(str(linha[4]))), end="")
                print("| " + str(linha[5]) + " " * (19 - len(str(linha[5]))) + "|")
            print(("+" + "-" * 20) * 6 + "+")
        if opcao == 9:
            comando = "select * from jogo"
            cursor.execute(comando)
            result = cursor.fetchall()
            print(("+" + "-" * 20) * 6 + "+")
            print(
                "| idJogo" + " " * 13 + "| idClube1" + " " * 11 + "| idClube2" + " " * 11 + "| idArbitro" + " "*10 + "| resultado" + " " * 10 + "| idComp" + " "*13 + "|")
            for linha in result:
                print(("+" + "-" * 20) * 6 + "+")
                print("| " + str(linha[0]) + " " * (19 - len(str(linha[0]))), end="")
                print("| " + str(linha[1]) + " " * (19 - len(str(linha[1]))), end="")
                print("| " + str(linha[2]) + " " * (19 - len(str(linha[2]))), end="")
                print("| " + str(linha[3]) + " " * (19 - len(str(linha[3]))), end="")
                print("| " + str(linha[4]) + " " * (19 - len(str(linha[4]))), end="")
                print("| " + str(linha[5]) + " " * (19 - len(str(linha[5]))) + "|")
            print(("+" + "-" * 20) * 6 + "+")
        if opcao == 10:
            comando = "select * from cartaoJogador"
            cursor.execute(comando)
            result = cursor.fetchall()
            print(("+" + "-" * 20) * 5 + "+")
            print(
                "| idCartao" + " " * 11 + "| idJogador" + " " * 10 + "| idJogo" + " "*13 + "| idArbitro" + " " * 10 + "| cor" + ' ' * 16 + "|")
            for linha in result:
                print(("+" + "-" * 20) * 5 + "+")
                print("| " + str(linha[0]) + " " * (19 - len(str(linha[0]))), end="")
                print("| " + str(linha[1]) + " " * (19 - len(str(linha[1]))), end="")
                print("| " + str(linha[2]) + " " * (19 - len(str(linha[2]))), end="")
                print("| " + str(linha[3]) + " " * (19 - len(str(linha[3]))), end="")
                print("| " + str(linha[4]) + " " * (19 - len(str(linha[4]))) + "|")
            print(("+" + "-" * 20) * 5 + "+")
        if opcao == 11:
            comando = "select * from cartaoTecnico"
            cursor.execute(comando)
            result = cursor.fetchall()
            print(("+" + "-" * 20) * 5 + "+")
            print(
                "| idCartao" + " " * 11 + "| idTecnico" + " " * 10 + "| idJogo" + " " * 13 + "| idArbitro" + " " * 10 + "| cor" + ' ' * 16 + "|")
            for linha in result:
                print(("+" + "-" * 20) * 5 + "+")
                print("| " + str(linha[0]) + " " * (19 - len(str(linha[0]))), end="")
                print("| " + str(linha[1]) + " " * (19 - len(str(linha[1]))), end="")
                print("| " + str(linha[2]) + " " * (19 - len(str(linha[2]))), end="")
                print("| " + str(linha[3]) + " " * (19 - len(str(linha[3]))), end="")
                print("| " + str(linha[4]) + " " * (19 - len(str(linha[4]))) + "|")
            print(("+" + "-" * 20) * 5 + "+")
        if opcao == 12:
            comando = "select * from titulo"
            cursor.execute(comando)
            result = cursor.fetchall()
            print(("+" + "-" * 20) * 5 + "+")
            print(
                "| idTitulo" + " " * 11 + "| idComp" + " " * 13 + "| idClube" + " " * 12 + "| ano" + " " * 16 + "| idArtilheiro" + ' ' * 7 + "|")
            for linha in result:
                print(("+" + "-" * 20) * 5 + "+")
                print("| " + str(linha[0]) + " " * (19 - len(str(linha[0]))), end="")
                print("| " + str(linha[1]) + " " * (19 - len(str(linha[1]))), end="")
                print("| " + str(linha[2]) + " " * (19 - len(str(linha[2]))), end="")
                print("| " + str(linha[3]) + " " * (19 - len(str(linha[3]))), end="")
                print("| " + str(linha[4]) + " " * (19 - len(str(linha[4]))) + "|")
            print(("+" + "-" * 20) * 5 + "+")
        if opcao == 13:
            break
        input("Digite enter para voltar")


def telaUpdate():
    while True:
        print('-------------------------UPDATE-------------------------')
        print('1.- Arbitro')
        print('2.- Estadio')
        print('3.- Lesao')
        print('4.- Competicao')
        print('5.- Tecnico')
        print('6.- Clube')
        print('7.- Jogador')
        print('8.- LesaoJogador')
        print('9.- Jogo')
        print('10.- CartaoJogador')
        print('11.- CartaoTecnico')
        print('12.- Titulo')
        print('13.- Sair')
        print('----------------------------------------------------------')

        print("Selecione uma tabela: ")
        opcao = int(input())

        if opcao == 1:
            print("digite o id do arbitro a ser mudado: ")
            id = int(input())
            print('Digite o nome do arbitro: ')
            nome = input()
            print('Digite a data de nascimento do arbitro (YYYY-MM-DD)')
            datanasc = input()
            print('Digite o numero de jogos apitados pelo arbitro')
            qtdJogos = int(input())
            print('Digite a data de estreia do arbitro (YYYY-MM-DD')
            dataEstreia = input()
            comando = f"update arbitro set nome = '{nome}', datanasc = '{datanasc}', qtdjogos = '{str(qtdJogos)}', dataEstreia = '{dataEstreia}' where idArbitro = {id}"
            cursor.execute(comando)
            connection.commit()
        if opcao == 2:
            print("digite o id do estadio a ser mudado: ")
            id = int(input())
            print('Digite o nome do estádio: ')
            nome = input()
            print('Digite a data de inaugaração do estádio (YYYY-MM-DD): ')
            dataInaug = input()
            print('Digite o valor do estádio: ')
            valor = float(input())
            print('Digite a capacidade do estádio: ')
            capac = int(input())
            comando = f"update estadio set nome = '{nome}', dataInaug = '{dataInaug}', valor = '{str(valor)}', capacidade = '{str(capac)}' where idEstadio = {id}"
            cursor.execute(comando)
            connection.commit()
        if opcao == 3:
            print("Digite o id da lesão a ser mudada: ")
            id = int(input())
            print("Digite a descrição da lesão")
            desc = input()
            comando = f"update lesao set descricao = '{desc}' where idLesao = {id}"
            cursor.execute(comando)
            connection.commit()
        if opcao == 4:
            pass
        if opcao == 5:
            pass
        if opcao == 6:
            pass
        if opcao == 7:
            pass
        if opcao == 8:
            pass
        if opcao == 9:
            pass
        if opcao == 10:
            pass
        if opcao == 11:
            pass
        if opcao == 12:
            pass
        if opcao == 13:
            break
        input("Digite enter para voltar")


def telaDelete():
    while True:
        print('-------------------------DELETE-------------------------')
        print('1.- Arbitro')
        print('2.- Estadio')
        print('3.- Lesao')
        print('4.- Competicao')
        print('5.- Tecnico')
        print('6.- Clube')
        print('7.- Jogador')
        print('8.- LesaoJogador')
        print('9.- Jogo')
        print('10.- CartaoJogador')
        print('11.- CartaoTecnico')
        print('12.- Titulo')
        print('13.- Sair')
        print('----------------------------------------------------------')

        print("Selecione uma tabela: ")
        opcao = int(input())

        if opcao == 1:
            print("Digite o id do arbitro: ")
            id = int(input())
            comando = f"delete from arbitro where idArbitro = {str(id)}"
            cursor.execute(comando)
            connection.commit()
        if opcao == 2:
            print("Digite o id do estadio: ")
            id = int(input())
            comando = f"delete from estadio where idEstadio = {str(id)}"
            cursor.execute(comando)
            connection.commit()
        if opcao == 3:
            print("Digite o id do lesao: ")
            id = int(input())
            comando = f"delete from lesao where idLesao = {str(id)}"
            cursor.execute(comando)
            connection.commit()
        if opcao == 4:
            print("Digite o id do competicao: ")
            id = int(input())
            comando = f"delete from competicao where idComp = {str(id)}"
            cursor.execute(comando)
            connection.commit()
        if opcao == 5:
            print("Digite o id do tecnico: ")
            id = int(input())
            comando = f"delete from tecnico where idTecnico = {str(id)}"
            cursor.execute(comando)
            connection.commit()
        if opcao == 6:
            print("Digite o id do clube: ")
            id = int(input())
            comando = f"delete from clube where idClube = {str(id)}"
            cursor.execute(comando)
            connection.commit()
        if opcao == 7:
            print("Digite o id do jogador: ")
            id = int(input())
            comando = f"delete from jogador where idJogador = {str(id)}"
            cursor.execute(comando)
            connection.commit()
        if opcao == 8:
            print("Digite o id do jogador: ")
            idj = int(input())
            print("Digite a id da lesao: ")
            idl = int(input())
            comando = f"delete from lesaojogador where idJogador = {str(idj)} and idLesao = {str(idl)}"
            cursor.execute(comando)
            connection.commit()
        if opcao == 9:
            print("Digite o id do jogo: ")
            id = int(input())
            comando = f"delete from jogo where idJogo = {str(id)}"
            cursor.execute(comando)
            connection.commit()
        if opcao == 10:
            print("Digite o id do cartaojogador: ")
            id = int(input())
            comando = f"delete from cartaojogador where idCartao = {str(id)}"
            cursor.execute(comando)
            connection.commit()
        if opcao == 11:
            print("Digite o id do cartaotecnico: ")
            id = int(input())
            comando = f"delete from cartaotecnico where idCartao = {str(id)}"
            cursor.execute(comando)
            connection.commit()
        if opcao == 12:
            print("Digite o id do titulo: ")
            id = int(input())
            comando = f"delete from titulo where idTitulo = {str(id)}"
            cursor.execute(comando)
            connection.commit()
        if opcao == 13:
            break
        input("Digite enter para voltar")


if __name__ == '__main__':

    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        database='projetobdcrud',
    )
    cursor = connection.cursor()

    createTables()

    menuPrincipal()

    cursor.close()
    connection.close()
