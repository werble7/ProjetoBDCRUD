import mysql.connector


def createTables():

    # criando tabelas

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
	idJogo int unsigned not null auto_increment,
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

    # criando inserts para arbitro
    arbitrocount = "select count(*) from arbitro"
    cursor.execute(arbitrocount)
    result = cursor.fetchall()

    if result[0][0] == 0:

        arbitro1 = "insert into arbitro(nome,dataNasc,qtdJogos,dataEstreia) values('Carlos','1976-12-18',15,'1996-02-18');"
        arbitro2 = "insert into arbitro(nome,dataNasc,qtdJogos,dataEstreia) values('Romário','1982-05-19',123,'2002-07-08');"
        arbitro3 = "insert into arbitro(nome,dataNasc,qtdJogos,dataEstreia) values('Cássio','1977-03-03', 38,'2003-04-09');"
        arbitro4 = "insert into arbitro(nome,dataNasc,qtdJogos,dataEstreia) values('Valdemar','1990-08-30',4,'2010-05-17');"
        arbitro5 = "insert into arbitro(nome,dataNasc,qtdJogos,dataEstreia) values('Roberto','1978-01-10',13,'1998-11-18');"

        cursor.execute(arbitro1)
        cursor.execute(arbitro2)
        cursor.execute(arbitro3)
        cursor.execute(arbitro4)
        cursor.execute(arbitro5)
        connection.commit()

    # criando inserts para estadio
    estadiocount = "select count(*) from estadio"
    cursor.execute(estadiocount)
    result = cursor.fetchall()

    if result[0][0] == 0:
        estadio1 = "insert into estadio(nome,dataInaug,valor,capacidade) values('Pacaembu','1976-12-18',150000000,50000);"
        estadio2 = "insert into estadio(nome,dataInaug,valor,capacidade) values('Allianz Parque','2012-12-18',1000000000,45000);"
        estadio3 = "insert into estadio(nome,dataInaug,valor,capacidade) values('Morumbi','1970-10-28',100000000,100000);"
        estadio4 = "insert into estadio(nome,dataInaug,valor,capacidade) values('Maracanã','1940-01-01',1000000,150000);"
        estadio5 = "insert into estadio(nome,dataInaug,valor,capacidade) values('Mané Garrincha','1960-04-21',4000000000,70000);"

        cursor.execute(estadio1)
        connection.commit()
        cursor.execute(estadio2)
        connection.commit()
        cursor.execute(estadio3)
        connection.commit()
        cursor.execute(estadio4)
        connection.commit()
        cursor.execute(estadio5)
        connection.commit()

    # criando inserts para lesao
    lesaocount = "select count(*) from lesao"
    cursor.execute(lesaocount)
    result = cursor.fetchall()

    if result[0][0] == 0:
        lesao1 = "insert into lesao(descricao) values('Fratura do joelho esquerdo');"
        lesao2 = "insert into lesao(descricao) values('Torção do tornozelo direito');"
        lesao3 = "insert into lesao(descricao) values('Fratura exposta da tíbia esquerda');"
        lesao4 = "insert into lesao(descricao) values('Desolcamento do ombro direito');"
        lesao5 = "insert into lesao(descricao) values('Deslocamento do ombro esquerdo');"

        cursor.execute(lesao1)
        connection.commit()
        cursor.execute(lesao2)
        connection.commit()
        cursor.execute(lesao3)
        connection.commit()
        cursor.execute(lesao4)
        connection.commit()
        cursor.execute(lesao5)
        connection.commit()

    # criando inserts para competição
    compcount = "select count(*) from competicao"
    cursor.execute(compcount)
    result = cursor.fetchall()

    if result[0][0] == 0:
        comp1 = "insert into competicao(descricao) values('Brasileirão');"
        comp2 = "insert into competicao(descricao) values('Copa do Brasil');"
        comp3 = "insert into competicao(descricao) values('Libertadores');"
        comp4 = "insert into competicao(descricao) values('Supercopa do Brasil');"
        comp5 = "insert into competicao(descricao) values('Recopa Sulamericana');"

        cursor.execute(comp1)
        connection.commit()
        cursor.execute(comp2)
        connection.commit()
        cursor.execute(comp3)
        connection.commit()
        cursor.execute(comp4)
        connection.commit()
        cursor.execute(comp5)
        connection.commit()

    # criando inserts para tecnico
    teccount = "select count(*) from tecnico"
    cursor.execute(teccount)
    result = cursor.fetchall()

    if result[0][0] == 0:
        tec1 = "insert into tecnico(nome,dataNasc,qtdJogos,dataEstreia) values('Luxemburgo','1960-05-19',915,'1983-12-04');"
        tec2 = "insert into tecnico(nome,dataNasc,qtdJogos,dataEstreia) values('Felipão','1958-12-17',1056,'1985-06-05');"
        tec3 = "insert into tecnico(nome,dataNasc,qtdJogos,dataEstreia) values('Muricy','1967-05-09',765,'1990-01-31');"
        tec4 = "insert into tecnico(nome,dataNasc,qtdJogos,dataEstreia) values('Parreira','1948-09-29',451,'1970-08-14');"
        tec5 = "insert into tecnico(nome,dataNasc,qtdJogos,dataEstreia) values('Ancelotti','1956-12-17',589,'1984-03-05');"

        cursor.execute(tec1)
        connection.commit()
        cursor.execute(tec2)
        connection.commit()
        cursor.execute(tec3)
        connection.commit()
        cursor.execute(tec4)
        connection.commit()
        cursor.execute(tec5)
        connection.commit()

    # criando inserts para clube
    count = "select count(*) from clube"
    cursor.execute(count)
    result = cursor.fetchall()

    if result[0][0] == 0:
        com1 = "insert into clube(nome,dataFund,idEstadio,idTecnico) values('Palmeiras','1914-08-26',1,1);"
        com2 = "insert into clube(nome,dataFund,idEstadio,idTecnico) values('Flamengo','1889-12-17',2,2);"
        com3 = "insert into clube(nome,dataFund,idEstadio,idTecnico) values('São Paulo','1932-05-09',3,3);"
        com4 = "insert into clube(nome,dataFund,idEstadio,idTecnico) values('Grêmio','1910-09-29',4,4);"
        com5 = "insert into clube(nome,dataFund,idEstadio,idTecnico) values('Vasco','1894-12-17',5,5);"

        cursor.execute(com1)
        connection.commit()
        cursor.execute(com2)
        connection.commit()
        cursor.execute(com3)
        connection.commit()
        cursor.execute(com4)
        connection.commit()
        cursor.execute(com5)
        connection.commit()

    # criando inserts para jogador
    count = "select count(*) from jogador"
    cursor.execute(count)
    result = cursor.fetchall()

    if result[0][0] == 0:
        com1 = "insert into jogador(nome,dataNasc,posicao,qtdJogos,qtdGols,qtdAssist,idClube) values('David Luiz', '1987-04-22','Zagueiro',30, 7, 5, 2);"
        com2 = "insert into jogador(nome,dataNasc,posicao,qtdJogos,qtdGols,qtdAssist,idClube) values('Joaquín Piquerez', '1998-08-24','lateral esq.',23, 15, 8, 1);"
        com3 = "insert into jogador(nome,dataNasc,posicao,qtdJogos,qtdGols,qtdAssist,idClube) values('Luis Suárez', '1987-01-24','Centroavante',5, 4, 3, 4);"
        com4 = "insert into jogador(nome,dataNasc,posicao,qtdJogos,qtdGols,qtdAssist,idClube) values('Rodrigo Nestor', '2000-09-08','Meia Central',36, 14, 9, 3);"
        com5 = "insert into jogador(nome,dataNasc,posicao,qtdJogos,qtdGols,qtdAssist,idClube) values('Endrick', '2006-07-21','Centroavante',7, 2, 1, 1);"

        cursor.execute(com1)
        connection.commit()
        cursor.execute(com2)
        connection.commit()
        cursor.execute(com3)
        connection.commit()
        cursor.execute(com4)
        connection.commit()
        cursor.execute(com5)
        connection.commit()

    # criando inserts para lesaoJogador
    count = "select count(*) from lesaojogador"
    cursor.execute(count)
    result = cursor.fetchall()

    if result[0][0] == 0:
        com1 = "insert into lesaojogador(dataLesao,gravidade,regiao,dataRecu,idLesao,idJogador) values('2022-09-15', 'leve', 'joelho', '2022-09-29',1,2);"
        com2 = "insert into lesaojogador(dataLesao,gravidade,regiao,dataRecu,idLesao,idJogador) values('2022-08-15', 'leve', 'ombro', '2022-09-02',3,2);"
        com3 = "insert into lesaojogador(dataLesao,gravidade,regiao,dataRecu,idLesao,idJogador) values('2022-09-15', 'médio', 'tornozelo', '2022-09-29',2,3);"
        com4 = "insert into lesaojogador(dataLesao,gravidade,regiao,dataRecu,idLesao,idJogador) values('2022-09-15', 'leve', 'tbia', '2022-09-15',5,1);"
        com5 = "insert into lesaojogador(dataLesao,gravidade,regiao,dataRecu,idLesao,idJogador) values('2022-09-15', 'leve', 'ombro', '2022-09-29',2,1);"

        cursor.execute(com1)
        connection.commit()
        cursor.execute(com2)
        connection.commit()
        cursor.execute(com3)
        connection.commit()
        cursor.execute(com4)
        connection.commit()
        cursor.execute(com5)
        connection.commit()

    # criando inserts para jogo
    count = "select count(*) from jogo"
    cursor.execute(count)
    result = cursor.fetchall()

    if result[0][0] == 0:
        com1 = "insert into jogo(idClube1,idClube2,idArbitro,resultado,idComp) values(1,2,3,'3x1',1);"
        com2 = "insert into jogo(idClube1,idClube2,idArbitro,resultado,idComp) values(3,5,3,'4x1',3);"
        com3 = "insert into jogo(idClube1,idClube2,idArbitro,resultado,idComp) values(4,1,1,'1x2',2);"
        com4 = "insert into jogo(idClube1,idClube2,idArbitro,resultado,idComp) values(5,3,2,'2x4',4);"
        com5 = "insert into jogo(idClube1,idClube2,idArbitro,resultado,idComp) values(5,2,4,'3x4',2);"

        cursor.execute(com1)
        connection.commit()
        cursor.execute(com2)
        connection.commit()
        cursor.execute(com3)
        connection.commit()
        cursor.execute(com4)
        connection.commit()
        cursor.execute(com5)
        connection.commit()

    # criando inserts para cartaojogador
    count = "select count(*) from cartaojogador"
    cursor.execute(count)
    result = cursor.fetchall()

    if result[0][0] == 0:
        com1 = "insert into cartaojogador(idJogador,idJogo,idArbitro,cor) values(1,3,1,'amarelo');"
        com2 = "insert into cartaojogador(idJogador,idJogo,idArbitro,cor) values(3,2,3,'amarelo');"
        com3 = "insert into cartaojogador(idJogador,idJogo,idArbitro,cor) values(4,2,3,'amarelo');"
        com4 = "insert into cartaojogador(idJogador,idJogo,idArbitro,cor) values(4,4,2,'vermelho');"
        com5 = "insert into cartaojogador(idJogador,idJogo,idArbitro,cor) values(2,5,4,'amarelo');"

        cursor.execute(com1)
        connection.commit()
        cursor.execute(com2)
        connection.commit()
        cursor.execute(com3)
        connection.commit()
        cursor.execute(com4)
        connection.commit()
        cursor.execute(com5)
        connection.commit()

    # criando inserts para cartaotecnico
    count = "select count(*) from cartaotecnico"
    cursor.execute(count)
    result = cursor.fetchall()

    if result[0][0] == 0:
        com1 = "insert into cartaotecnico(idTecnico,idJogo,idArbitro,cor) values(1,3,1,'amarelo');"
        com2 = "insert into cartaotecnico(idTecnico,idJogo,idArbitro,cor) values(2,3,3,'amarelo');"
        com3 = "insert into cartaotecnico(idTecnico,idJogo,idArbitro,cor) values(3,4,2,'vermelho');"
        com4 = "insert into cartaotecnico(idTecnico,idJogo,idArbitro,cor) values(3,2,3,'vermelho');"
        com5 = "insert into cartaotecnico(idTecnico,idJogo,idArbitro,cor) values(3,4,2,'vermelho');"

        cursor.execute(com1)
        connection.commit()
        cursor.execute(com2)
        connection.commit()
        cursor.execute(com3)
        connection.commit()
        cursor.execute(com4)
        connection.commit()
        cursor.execute(com5)
        connection.commit()

    # criando inserts para titulo
    count = "select count(*) from titulo"
    cursor.execute(count)
    result = cursor.fetchall()

    if result[0][0] == 0:
        com1 = "insert into titulo(idComp,idClube,ano,idArtilheiro) values(1,2,2016,2);"
        com2 = "insert into titulo(idComp,idClube,ano,idArtilheiro) values(2,3,2007,4);"
        com3 = "insert into titulo(idComp,idClube,ano,idArtilheiro) values(5,1,2023,5);"
        com4 = "insert into titulo(idComp,idClube,ano,idArtilheiro) values(3,3,2017,2);"
        com5 = "insert into titulo(idComp,idClube,ano,idArtilheiro) values(2,2,2013,4);"

        cursor.execute(com1)
        connection.commit()
        cursor.execute(com2)
        connection.commit()
        cursor.execute(com3)
        connection.commit()
        cursor.execute(com4)
        connection.commit()
        cursor.execute(com5)
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
        elif opcao == 2:
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
        elif opcao == 3:
            print("Digite a descrição da lesão")
            desc = input()
            comando = f"insert into lesao(descricao) values('{desc}')"
            cursor.execute(comando)
            connection.commit()
        elif opcao == 4:
            print("Digite a descrição da competicao")
            desc = input()
            comando = f"insert into competicao(descricao) values('{desc}')"
            cursor.execute(comando)
            connection.commit()
        elif opcao == 5:
            print("Digite informações do técnico")
            print("digite o nome do técnico: ")
            nome = input()
            print('Digite a data de nascimento (YYYY-MM-DD): ')
            dataNasc = input()
            print('Digite a quantidade de jogos: ')
            qtdJogos = input()
            print('Digite a data de nascimento (YYYY-MM-DD): ')
            dataEstreia = input()
            comando = f"insert into tecnico(nome, dataNasc, qtdJogos, dataEstreia) values('{nome}', '{dataNasc}', {str(qtdJogos)}, '{dataEstreia}')"
            cursor.execute(comando)
            connection.commit()
        elif opcao == 6:
            print("Digite a informação do clube")
            print('Digite o nome do Clube: ')
            nome = input()
            print("data de fundação do clube (YYYY-MM-DD): ")
            dataFund = input()
            print('digite o id do estadio: ')
            idEstadio = int(input())
            print("digite o id do tecnico")
            idTecnico = int(input())
            comando = f"insert into clube(nome, dataFund, idEstadio, idTecnico) values('{nome}', '{dataFund}',{str(idEstadio)}, {str(idTecnico)})"
            cursor.execute(comando)
            connection.commit()
        elif opcao == 7:
            print("Digite informações do jogador")
            print("Digite o nome do jogador: ")
            nome = input()
            print("Digite a data de nascimento do jogador (YYYY-MM-DD): ")
            dataNasc = input()
            print('digite a posicao do jogador: ')
            posicao = input()
            print('digite a quantidade de jogos do jogador: ')
            qtdJogos = int(input())
            print('digite a quantidade de gols do jogador: ')
            qtdGols = int(input())
            print("digite a quantidade de assistencias do jogador: ")
            qtdAssist = int(input())
            print("digite o id do clube: ")
            idClube = int(input())
            comando = f"insert into jogador(nome, dataNasc, posicao, qtdJogos, qtdGols, qtdAssist, idClube) values('{nome}','{dataNasc}','{posicao}', {str(qtdJogos)}, {str(qtdGols)}, {str(qtdAssist)}, {str(idClube)})"
            cursor.execute(comando)
            connection.commit()
        elif opcao == 8:
            print("Digite as informações da lesão do jogador")
            print("Digite o id da lesão do jogador: ")
            idLesao = int(input())
            print('Digite o id do jogador: ')
            idJogador = int(input())
            print('data da lesao (YYYY-MM-DD): ')
            dataLesao = input()
            print("dados da gravidade: ")
            gravidade = input()
            print("regiao da lesao: ")
            regiao = input()
            print("digite a data de recuperacao (YYYY-MM-DD)")
            dataRecu = input()
            comando = f"insert into LesaoJogador(idLesao, idJogador, dataLesao, gravidade, regiao, dataRecu) values({str(idLesao)}, {str(idJogador)}, '{dataLesao}', '{gravidade}', '{regiao}', '{dataRecu}')"
            cursor.execute(comando)
            connection.commit()
        elif opcao == 9:
            print("Digite as informações do jogo")
            print("Digite o id do clube em casa: ")
            idClube1 = int(input())
            print("Digite o id do clube fora: ")
            idClube2 = int(input())
            print('digite o idArbitro: ')
            idArbitro = int(input())
            print('resultado da partida: ')
            resultado = input()
            print('Digite o id da competicao')
            idComp = int(input())
            comando = f"insert into jogo(idClube1, idClube2, idArbitro, resultado, idComp) values({str(idClube1)},{str(idClube2)}, {str(idArbitro)}, '{resultado}', {str(idComp)})"
            cursor.execute(comando)
            connection.commit()
        elif opcao == 10:
            print("Digite as informações do cartão recebido pelo jogador")
            print("Digite o id do jogador")
            idJogador = int(input())
            print("id do jogo: ")
            idJogo = int(input())
            print("id do Arbitro")
            idArbitro = int(input())
            print("cor do cartao")
            cor = input()
            comando = f"insert into CartaoJogador(idJogador, idJogo, idArbitro, cor) values({str(idJogador)},{str(idJogo)}, {str(idArbitro)}, '{cor}')"
            cursor.execute(comando)
            connection.commit()
        elif opcao == 11:
            print("Digite as informações do cartão recebido pelo técnico")
            print("Digite o id do tecnico: ")
            idTecnico = int(input())
            print("digite o id do jogo: ")
            idJogo = int(input())
            print("digite o id do arbitro: ")
            idArbitro = int(input())
            print("digite a cor do cartao: ")
            cor = input()
            comando = f"insert into CartaoTecnico(idTecnico, idJogo, idArbitro, cor) values({str(idTecnico)}, {str(idJogo)}, {str(idArbitro)}, '{cor}')"
            cursor.execute(comando)
            connection.commit()
        elif opcao == 12:
            print("Digite as informações do título")
            print("Digite o id da competicao")
            idComp = int(input())
            print("digite o id do clube")
            idClube = int(input())
            print("Digite o ano do título")
            ano = int(input())
            print("digite o id do artilheiro")
            idArtilheiro = int(input())
            comando = f"insert into titulo(idComp, idClube, ano, idArtilheiro) values({str(idComp)}, {str(idClube)}, {str(ano)}, {str(idArtilheiro)})"
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
        print('13.- Views')
        print('14.- Sair')
        print('----------------------------------------------------------')

        print("Selecione uma tabela: ")
        opcao = int(input())

        if opcao == 1:
            comando = "select * from arbitro"
            cursor.execute(comando)
            result = cursor.fetchall()

            print(("+" + "-" * 40) * 5 + "+")
            print("| idArbitro" + " "*30 + "| nome" + " "*35 + "| data de nascimento" + " "*21 +
                  "| qtd de jogos" + " "*27 + "| data de Estreia" + " "*24 + "|")
            for linha in result:
                print(("+" + "-" * 40) * 5 + "+")
                print("| " + str(linha[0]) + " " *
                      (39-len(str(linha[0]))), end="")
                print("| " + str(linha[1]) + " " *
                      (39 - len(str(linha[1]))), end="")
                print("| " + str(linha[2]) + " " *
                      (39 - len(str(linha[2]))), end="")
                print("| " + str(linha[3]) + " " *
                      (39 - len(str(linha[3]))), end="")
                print("| " + str(linha[4]) + " " *
                      (39 - len(str(linha[4]))) + "|")
            print(("+" + "-" * 40) * 5 + "+")

        if opcao == 2:
            comando = "select * from estadio"
            cursor.execute(comando)
            result = cursor.fetchall()

            print(("+" + "-" * 40) * 5 + "+")
            print("| idEstadio" + " " * 30 + "| nome" + " " * 35 +
                  "| data de inauguração" + " "*20 + "| valor" + " " * 34 + "| capacidade" + ' '*29 + "|")
            for linha in result:
                print(("+" + "-" * 40) * 5 + "+")
                print("| " + str(linha[0]) + " " *
                      (39 - len(str(linha[0]))), end="")
                print("| " + str(linha[1]) + " " *
                      (39 - len(str(linha[1]))), end="")
                print("| " + str(linha[2]) + " " *
                      (39 - len(str(linha[2]))), end="")
                print("| " + str(linha[3]) + " " *
                      (39 - len(str(linha[3]))), end="")
                print("| " + str(linha[4]) + " " *
                      (39 - len(str(linha[4]))) + "|")
            print(("+" + "-" * 40) * 5 + "+")

        if opcao == 3:
            comando = "select * from lesao"
            cursor.execute(comando)
            result = cursor.fetchall()
            print(("+" + "-" * 40) * 2 + "+")
            print(
                "| idLesao" + " " * 32 + "| descricao" + " " * 30 + "|")
            for linha in result:
                print(("+" + "-" * 40) * 2 + "+")
                print("| " + str(linha[0]) + " " *
                      (39 - len(str(linha[0]))), end="")
                print("| " + str(linha[1]) + " " *
                      (39 - len(str(linha[1]))) + "|")
            print(("+" + "-" * 40) * 2 + "+")

        if opcao == 4:
            comando = "select * from competicao"
            cursor.execute(comando)
            result = cursor.fetchall()
            print(("+" + "-" * 40) * 2 + "+")
            print(
                "| idComp" + " " * 33 + "| descricao" + " " * 30 + "|")
            for linha in result:
                print(("+" + "-" * 40) * 2 + "+")
                print("| " + str(linha[0]) + " " *
                      (39 - len(str(linha[0]))), end="")
                print("| " + str(linha[1]) + " " *
                      (39 - len(str(linha[1]))) + "|")
            print(("+" + "-" * 40) * 2 + "+")

        if opcao == 5:
            comando = "select * from tecnico"
            cursor.execute(comando)
            result = cursor.fetchall()
            print(("+" + "-" * 40) * 5 + "+")
            print(
                "| idTecnico" + " " * 30 + "| nome" + " " * 35 + "| data de nascimento" + " "*21 + "| qtd de jogos" + " " * 27 + "| data de estreia" + ' ' * 24 + "|")
            for linha in result:
                print(("+" + "-" * 40) * 5 + "+")
                print("| " + str(linha[0]) + " " *
                      (39 - len(str(linha[0]))), end="")
                print("| " + str(linha[1]) + " " *
                      (39 - len(str(linha[1]))), end="")
                print("| " + str(linha[2]) + " " *
                      (39 - len(str(linha[2]))), end="")
                print("| " + str(linha[3]) + " " *
                      (39 - len(str(linha[3]))), end="")
                print("| " + str(linha[4]) + " " *
                      (39 - len(str(linha[4]))) + "|")
            print(("+" + "-" * 40) * 5 + "+")

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
            print(("+" + "-" * 40) * 8 + "+")
            print("| idJogador" + " "*30 + "| nome" + " "*35 +
                  "| data de nascimento" + " " * 21 + "| posicao" + " "*32, end="")
            print("| qtd de jogos" + ' '*27 + "| qtd de gols" + " "*28 +
                  "| qtd de assists" + " "*25 + "| idClube" + " "*32 + "|")
            for linha in result:
                print(("+" + "-" * 40) * 8 + "+")
                print("| " + str(linha[0]) + " " *
                      (39 - len(str(linha[0]))), end="")
                print("| " + str(linha[1]) + " " *
                      (39 - len(str(linha[1]))), end="")
                print("| " + str(linha[2]) + " " *
                      (39 - len(str(linha[2]))), end="")
                print("| " + str(linha[3]) + " " *
                      (39 - len(str(linha[3]))), end="")
                print("| " + str(linha[4]) + " " *
                      (39 - len(str(linha[4]))), end="")
                print("| " + str(linha[5]) + " " *
                      (39 - len(str(linha[5]))), end="")
                print("| " + str(linha[6]) + " " *
                      (39 - len(str(linha[6]))), end="")
                print("| " + str(linha[7]) + " " *
                      (39 - len(str(linha[7]))) + "|")
            print(("+" + "-" * 40) * 8 + "+")

        if opcao == 8:
            comando = "select * from lesaoJogador"
            cursor.execute(comando)
            result = cursor.fetchall()
            print(("+" + "-" * 40) * 6 + "+")
            print(
                "| idLesao" + " "*32 + "| idJogador" + " "*30 + "| data de lesao"+" "*26 + "| gravidade"+" "*30 + "| região" + " "*33 + "| data de recuperação" + " "*20 + "|")
            for linha in result:
                print(("+" + "-" * 40) * 6 + "+")
                print("| " + str(linha[0]) + " " *
                      (39 - len(str(linha[0]))), end="")
                print("| " + str(linha[1]) + " " *
                      (39 - len(str(linha[1]))), end="")
                print("| " + str(linha[2]) + " " *
                      (39 - len(str(linha[2]))), end="")
                print("| " + str(linha[3]) + " " *
                      (39 - len(str(linha[3]))), end="")
                print("| " + str(linha[4]) + " " *
                      (39 - len(str(linha[4]))), end="")
                print("| " + str(linha[5]) + " " *
                      (39 - len(str(linha[5]))) + "|")
            print(("+" + "-" * 40) * 6 + "+")
        if opcao == 9:
            comando = "select * from jogo"
            cursor.execute(comando)
            result = cursor.fetchall()
            print(("+" + "-" * 40) * 6 + "+")
            print(
                "| idJogo" + " " * 33 + "| idClube1" + " " * 31 + "| idClube2" + " " * 31 + "| idArbitro" + " "*30 + "| resultado" + " " * 30 + "| idComp" + " "*33 + "|")
            for linha in result:
                print(("+" + "-" * 40) * 6 + "+")
                print("| " + str(linha[0]) + " " *
                      (39 - len(str(linha[0]))), end="")
                print("| " + str(linha[1]) + " " *
                      (39 - len(str(linha[1]))), end="")
                print("| " + str(linha[2]) + " " *
                      (39 - len(str(linha[2]))), end="")
                print("| " + str(linha[3]) + " " *
                      (39 - len(str(linha[3]))), end="")
                print("| " + str(linha[4]) + " " *
                      (39 - len(str(linha[4]))), end="")
                print("| " + str(linha[5]) + " " *
                      (39 - len(str(linha[5]))) + "|")
            print(("+" + "-" * 40) * 6 + "+")
        if opcao == 10:
            comando = "select * from cartaoJogador"
            cursor.execute(comando)
            result = cursor.fetchall()
            print(("+" + "-" * 40) * 5 + "+")
            print(
                "| idCartao" + " " * 31 + "| idJogador" + " " * 30 + "| idJogo" + " "*33 + "| idArbitro" + " " * 30 + "| cor" + ' ' * 36 + "|")
            for linha in result:
                print(("+" + "-" * 40) * 5 + "+")
                print("| " + str(linha[0]) + " " *
                      (39 - len(str(linha[0]))), end="")
                print("| " + str(linha[1]) + " " *
                      (39 - len(str(linha[1]))), end="")
                print("| " + str(linha[2]) + " " *
                      (39 - len(str(linha[2]))), end="")
                print("| " + str(linha[3]) + " " *
                      (39 - len(str(linha[3]))), end="")
                print("| " + str(linha[4]) + " " *
                      (39 - len(str(linha[4]))) + "|")
            print(("+" + "-" * 40) * 5 + "+")
        if opcao == 11:
            comando = "select * from cartaoTecnico"
            cursor.execute(comando)
            result = cursor.fetchall()
            print(("+" + "-" * 40) * 5 + "+")
            print(
                "| idCartao" + " " * 31 + "| idTecnico" + " " * 30 + "| idJogo" + " " * 33 + "| idArbitro" + " " * 30 + "| cor" + ' ' * 36 + "|")
            for linha in result:
                print(("+" + "-" * 40) * 5 + "+")
                print("| " + str(linha[0]) + " " *
                      (39 - len(str(linha[0]))), end="")
                print("| " + str(linha[1]) + " " *
                      (39 - len(str(linha[1]))), end="")
                print("| " + str(linha[2]) + " " *
                      (39 - len(str(linha[2]))), end="")
                print("| " + str(linha[3]) + " " *
                      (39 - len(str(linha[3]))), end="")
                print("| " + str(linha[4]) + " " *
                      (39 - len(str(linha[4]))) + "|")
            print(("+" + "-" * 40) * 5 + "+")
        if opcao == 12:
            comando = "select * from titulo"
            cursor.execute(comando)
            result = cursor.fetchall()
            print(("+" + "-" * 40) * 5 + "+")
            print(
                "| idTitulo" + " " * 31 + "| idComp" + " " * 33 + "| idClube" + " " * 32 + "| ano" + " " * 36 + "| idArtilheiro" + ' ' * 27 + "|")
            for linha in result:
                print(("+" + "-" * 40) * 5 + "+")
                print("| " + str(linha[0]) + " " *
                      (39 - len(str(linha[0]))), end="")
                print("| " + str(linha[1]) + " " *
                      (39 - len(str(linha[1]))), end="")
                print("| " + str(linha[2]) + " " *
                      (39 - len(str(linha[2]))), end="")
                print("| " + str(linha[3]) + " " *
                      (39 - len(str(linha[3]))), end="")
                print("| " + str(linha[4]) + " " *
                      (39 - len(str(linha[4]))) + "|")
            print(("+" + "-" * 40) * 5 + "+")
        if opcao == 13:
            print("Visualizando a quantidade total de registros")
            comando = "select count(*) from arbitro"
            cursor.execute(comando)
            result1 = cursor.fetchall()
            comando = "select count(*) from estadio"
            cursor.execute(comando)
            result2 = cursor.fetchall()
            comando = "select count(*) from lesao"
            cursor.execute(comando)
            result3 = cursor.fetchall()
            comando = "select count(*) from competicao"
            cursor.execute(comando)
            result4 = cursor.fetchall()
            comando = "select count(*) from tecnico"
            cursor.execute(comando)
            result5 = cursor.fetchall()
            comando = "select count(*) from clube"
            cursor.execute(comando)
            result6 = cursor.fetchall()
            comando = "select count(*) from jogador"
            cursor.execute(comando)
            result7 = cursor.fetchall()
            comando = "select count(*) from lesaojogador"
            cursor.execute(comando)
            result8 = cursor.fetchall()
            comando = "select count(*) from jogo"
            cursor.execute(comando)
            result9 = cursor.fetchall()
            comando = "select count(*) from cartaojogador"
            cursor.execute(comando)
            result10 = cursor.fetchall()
            comando = "select count(*) from cartaotecnico"
            cursor.execute(comando)
            result11 = cursor.fetchall()
            comando = "select count(*) from titulo"
            cursor.execute(comando)
            result12 = cursor.fetchall()
            print(("+" + "-" * 30) * 12 + "+")
            print(
                "| qtd de árbitros" + " " * 14 + "| qtd de estádios" + " " * 14 + "| qtd de lesões" + " " * 16 + "| qtd de competições" + " " * 11 + "| qtd de técnicos" + ' ' * 14, end="")
            print(
                "| qtd de clubes" + " " * 16 + "| qtd de jogadores" + " " * 13 + "| qtd de lesões de jogadores" + " " * 3 + "| qtd de jogos" + " " * 17 + "| qtd de cartões de jogadores" + "  ", end="")
            print(
                "| qtd de cartões de técnicos" + " " * 3 + "| qtd de títulos" + " " * 15 + "|")
            print(("+" + "-" * 30) * 12 + "+")
            print("| " + str(result1[0][0]) + " " *
                  (29 - len(str(result1[0][0]))), end="")
            print("| " + str(result2[0][0]) + " " *
                  (29 - len(str(result2[0][0]))), end="")
            print("| " + str(result3[0][0]) + " " *
                  (29 - len(str(result3[0][0]))), end="")
            print("| " + str(result4[0][0]) + " " *
                  (29 - len(str(result4[0][0]))), end="")
            print("| " + str(result5[0][0]) + " " *
                  (29 - len(str(result5[0][0]))), end="")
            print("| " + str(result6[0][0]) + " " *
                  (29 - len(str(result6[0][0]))), end="")
            print("| " + str(result7[0][0]) + " " *
                  (29 - len(str(result7[0][0]))), end="")
            print("| " + str(result8[0][0]) + " " *
                  (29 - len(str(result8[0][0]))), end="")
            print("| " + str(result9[0][0]) + " " *
                  (29 - len(str(result9[0][0]))), end="")
            print("| " + str(result10[0][0]) + " " *
                  (29 - len(str(result10[0][0]))), end="")
            print("| " + str(result11[0][0]) + " " *
                  (29 - len(str(result11[0][0]))), end="")
            print("| " + str(result12[0][0]) + " " *
                  (29 - len(str(result12[0][0]))) + "|")
            print(("+" + "-" * 30) * 12 + "+")
        if opcao == 14:
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
            print("Digite o id da competicao a ser mudada: ")
            id = int(input())
            print("Digite a descrição da competicao")
            desc = input()
            comando = f"update competicao set descricao = '{desc}' where idComp = {id}"
            cursor.execute(comando)
            connection.commit()
        if opcao == 5:
            print("Digite o id do técnico a ser mudado: ")
            id = int(input())
            print("digite o nome do técnico: ")
            nome = input()
            print('Digite a data de nascimento (YYYY-MM-DD): ')
            dataNasc = input()
            print('Digite a quantidade de jogos: ')
            qtdJogos = input()
            print('Digite a data de nascimento (YYYY-MM-DD): ')
            dataEstreia = input()
            comando = f"update tecnico set nome = '{nome}', dataNasc = '{dataNasc}', qtdJogos = {qtdJogos}, dataEstreia = {dataEstreia} where idTecnico = {id}"
            cursor.execute(comando)
            connection.commit()
        if opcao == 6:
            print("Digite a id do clube a ser mudado")
            id = int(input())
            print('Digite o nome do Clube: ')
            nome = input()
            print("data de fundação do clube (YYYY-MM-DD): ")
            dataFund = input()
            print('digite o id do estadio: ')
            idEstadio = int(input())
            print("digite o id do tecnico")
            idTecnico = int(input())
            comando = f"update clube set nome = '{nome}', dataFund = '{dataFund}', idEstadio = {str(idEstadio)}, idTecnico = {str(idTecnico)} where idClube = {id};"
            cursor.execute(comando)
            connection.commit()
        if opcao == 7:
            print("Digite a id do jogador a ser mudado: ")
            id = int(input())
            print("Digite o nome do jogador: ")
            nome = input()
            print("Digite a data de nascimento do jogador (YYYY-MM-DD): ")
            dataNasc = input()
            print('digite a posicao do jogador: ')
            posicao = input()
            print('digite a quantidade de jogos do jogador: ')
            qtdJogos = int(input())
            print('digite a quantidade de gols do jogador: ')
            qtdGols = int(input())
            print("digite a quantidade de assistencias do jogador: ")
            qtdAssist = int(input())
            print("digite o id do clube: ")
            idClube = int(input())
            comando = f"update jogador set nome = '{nome}', dataNasc = '{dataNasc}', posicao = '{posicao}', qtdJogos = {qtdJogos}, qtdGols = {qtdGols}, qtdAssist = {qtdAssist}, idClube = {idClube}) where idJogador = {id};"
            cursor.execute(comando)
            connection.commit()
        if opcao == 8:
            print("Digite a id da lesão a ser mudada: ")
            id = int(input())
            print("Digite a id do jogador a ser mudado:")
            id2 = int(input())
            print("Digite o id da lesão do jogador: ")
            idLesao = int(input())
            print('Digite o id do jogador: ')
            idJogador = int(input())
            print('data da lesao (YYYY-MM-DD): ')
            dataLesao = input()
            print("dados da gravidade: ")
            gravidade = input()
            print("regiao da lesao: ")
            regiao = input()
            print("digite a data de recuperacao (YYYY-MM-DD)")
            dataRecu = input()
            comando = f"update LesaoJogador set dataLesao = '{dataLesao}', gravidade = '{gravidade}', regiao = '{regiao}', dataRecu = '{dataRecu}' where idLesao = {id} and idJogador = {id2};"
            cursor.execute(comando)
            connection.commit()
        if opcao == 9:
            print("Digite a id do jogo: ")
            id = int(input())
            print("Digite o id do clube em casa: ")
            idClube1 = int(input())
            print("Digite o id do clube fora: ")
            idClube2 = int(input())
            print('digite o idArbitro: ')
            idArbitro = int(input())
            print('resultado da partida: ')
            resultado = input()
            print('Digite o id da competicao')
            idComp = int(input())
            comando = f"update jogo set idClube1 = {idClube1}, idClube2 = {idClube2}, idArbitro = {idArbitro}, resultado = '{resultado}', idComp = {idComp} where idJogo = {id};"
            cursor.execute(comando)
            connection.commit()
        if opcao == 10:
            print("Digite a id do cartão recebido pelo jogador a ser mudado: ")
            id = int(input())
            print("Digite o id do jogador")
            idJogador = int(input())
            print("id do jogo: ")
            idJogo = int(input())
            print("id do Arbitro")
            idArbitro = int(input())
            print("cor do cartao")
            cor = input()
            comando = f"update CartaoJogador set idJogador = {idJogador}, idJogo = {idJogo}, idArbitro = {idArbitro}, cor = '{cor}' where idCartao = {id};"
            cursor.execute(comando)
            connection.commit()
        if opcao == 11:
            print("Digite a id do cartão recebido pelo técnico a ser mudado: ")
            id = int(input())
            print("Digite o id do tecnico: ")
            idTecnico = int(input())
            print("digite o id do jogo: ")
            idJogo = int(input())
            print("digite o id do arbitro: ")
            idArbitro = int(input())
            print("digite a cor do cartao: ")
            cor = input()
            comando = f"update CartaoTecnico set idTecnico = {idTecnico}, idJogo = {idJogo}, idArbitro = {idArbitro}, cor = '{cor}' where idCartao = {id};"
            cursor.execute(comando)
            connection.commit()
        if opcao == 12:
            print("Digite a id do título a ser mudado: ")
            id = int(input())
            print("Digite o id da competicao")
            idComp = int(input())
            print("digite o id do clube")
            idClube = int(input())
            print("Digite o ano do título")
            ano = int(input())
            print("digite o id do artilheiro")
            idArtilheiro = int(input())
            comando = f"update titulo set idComp = {idComp}, idClube = {idClube}, ano = '{ano}', idArtilheiro = {idArtilheiro} where idTitulo = {id};"
            cursor.execute(comando)
            connection.commit()
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
