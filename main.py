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
        com1 = "insert into jogador(nome,dataNasc,posicao,qtdJogos,qtdGols,qtdAssist,idClube) values();"
        com2 = "insert into jogador(nome,dataNasc,posicao,qtdJogos,qtdGols,qtdAssist,idClube) values();"
        com3 = "insert into jogador(nome,dataNasc,posicao,qtdJogos,qtdGols,qtdAssist,idClube) values();"
        com4 = "insert into jogador(nome,dataNasc,posicao,qtdJogos,qtdGols,qtdAssist,idClube) values();"
        com5 = "insert into jogador(nome,dataNasc,posicao,qtdJogos,qtdGols,qtdAssist,idClube) values();"

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
        com1 = "insert into lesaojogador(dataLesao,gravidade,regiao,dataRecu) values();"
        com2 = "insert into lesaojogador(dataLesao,gravidade,regiao,dataRecu) values();"
        com3 = "insert into lesaojogador(dataLesao,gravidade,regiao,dataRecu) values();"
        com4 = "insert into lesaojogador(dataLesao,gravidade,regiao,dataRecu) values();"
        com5 = "insert into lesaojogador(dataLesao,gravidade,regiao,dataRecu) values();"

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
        com1 = "insert into jogo(idClube1,idClube2,idArbitro,resultado,idComp) values();"
        com2 = "insert into jogo(idClube1,idClube2,idArbitro,resultado,idComp) values();"
        com3 = "insert into jogo(idClube1,idClube2,idArbitro,resultado,idComp) values();"
        com4 = "insert into jogo(idClube1,idClube2,idArbitro,resultado,idComp) values();"
        com5 = "insert into jogo(idClube1,idClube2,idArbitro,resultado,idComp) values();"

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
        com1 = "insert into cartaojogador(idJogador,idJogo,idArbitro,cor) values();"
        com2 = "insert into cartaojogador(idJogador,idJogo,idArbitro,cor) values();"
        com3 = "insert into cartaojogador(idJogador,idJogo,idArbitro,cor) values();"
        com4 = "insert into cartaojogador(idJogador,idJogo,idArbitro,cor) values();"
        com5 = "insert into cartaojogador(idJogador,idJogo,idArbitro,cor) values();"

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
        com1 = "insert into cartaotecnico(idTecnico,idJogo,idArbitro,cor) values();"
        com2 = "insert into cartaotecnico(idTecnico,idJogo,idArbitro,cor) values();"
        com3 = "insert into cartaotecnico(idTecnico,idJogo,idArbitro,cor) values();"
        com4 = "insert into cartaotecnico(idTecnico,idJogo,idArbitro,cor) values();"
        com5 = "insert into cartaotecnico(idTecnico,idJogo,idArbitro,cor) values();"

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
        com1 = "insert into titulo(idComp,idClube,ano,idArtilheiro) values();"
        com2 = "insert into titulo(idComp,idClube,ano,idArtilheiro) values();"
        com3 = "insert into titulo(idComp,idClube,ano,idArtilheiro) values();"
        com4 = "insert into titulo(idComp,idClube,ano,idArtilheiro) values();"
        com5 = "insert into titulo(idComp,idClube,ano,idArtilheiro) values();"

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
            print("data de fundação doi clube: ")
            dataFund = input()
            print('digite o id do estadio: ')
            idEstadio = input()
            print("digite idTecnico")
            idTecnico = input()
            comando = f"insert into clube(nome, dataFund, idEstadio, idTecnico) values('{nome}', '{dataFund}','{str(idEstadio)}', '{str(idTecnico)}')"
            cursor.execute(comando)
            connection.commit()
        elif opcao == 7:
            print("Digite informações do jogador")
            print("Digite o nome do jogador: ")
            nome = input()
            print("Digite a data de nascimento do jogador (YYYY-MM-DD): ")
            dataNasc = input()
            print('a posicao: ')
            posicao = input()
            print('a quantidade de jogos: ')
            qtdJogos = input()
            print('a quantidade de gols: ')
            qtdGols = input()
            print("a quantidae de assistencias: ")
            qtdAssist = input()
            print("id do clube: ")
            idClube = input()
            comando = f"insert into jogador(nome, dataNasc, posicao, qtdJogos, qtdGols, qtdAssist, idClube) values('{nome}','{dataNasc}','{posicao}', '{str(qtdJogos)}', '{str(qtdGols)}', '{str(qtdAssist)}', '{str(idClube)}')"
            cursor.execute(comando)
            connection.commit()
        elif opcao == 8:
            print("Digite as informações da lesão do jogador")
            print("Digite o id da lesão do jogador: ")
            idLesao = input()
            print('Digite o id do jogador: ')
            idJogador = input()
            print('data da lesao: ')
            dataLesao = input()
            print("dados da gravidade: ")
            gravidade = input()
            print("regiao da lesao: ")
            regiao = input()
            print("digite a data de recuperacao")
            dataRecu = input()
            comando = f"insert into LesaoJogador(idLesao, idJogador, dataLesao, gravidade, regiao, dataRecu) values('{str(idLesao)}', '{str(idJogador)}', '{dataLesao}', '{gravidade}', '{regiao}', '{dataRecu}')"
            cursor.execute(comando)
            connection.commit()
        elif opcao == 9:
            print("Digite as informações do jogo")
            print("Digite o id do clube em casa: ")
            idClube1 = input()
            print("Digite o id do clube fora: ")
            idClube2 = input()
            print('digite o idArbitro: ')
            idArbitro = input()
            print('resultado da partida: ')
            resultado = input()
            print('Digite o id da competicao')
            idComp = input()
            comando = f"insert into jogo(idClube1, idClube2, idArbitro, resultado, idComp) values('{str(idClube1)}','{str(idClube2)}, '{str(idArbitro)}', '{resultado}', '{str(idComp)}')"
            cursor.execute(comando)
            connection.commit()
        elif opcao == 10:
            print("Digite as informações do cartão recebido pelo jogador")
            print("Digite o id do jogador")
            idJogador = input()
            print("id do jogo: ")
            idJogo = input()
            print("id do Arbitro")
            idArbitro = input()
            print("cor do cartao")
            cor = input()
            comando = f"insert into CartaoJogador(idJogador, idJogo, idArbitro, cor) values('{str(idJogador)}','{str(idJogo)}', '{str(idArbitro)}', '{cor}')"
            cursor.execute(comando)
            connection.commit()
        elif opcao == 11:
            print("Digite as informações do cartão recebido pelo técnico")
            print("Digite o id do tecnico: ")
            idTecnico = input()
            print("digite o id do jogo: ")
            idJogo = input()
            print("digite o id do arbitro: ")
            idArbitro = input()
            print("digite a cor do cartao: ")
            cor = input()
            comando = f"insert into CartaoTecnico(idTecnico, idJogo, idArbitro, cor) values('{str(idTecnico)}', '{str(idJogo)}', '{str(idArbitro)}', '{cor}')"
            cursor.execute(comando)
            connection.commit()
        elif opcao == 12:
            print("Digite as informações do título")
            print("Digite o id da competicao")
            idComp = input()
            print("digite o id do clube")
            idClube = input()
            print("digite o id do artilheiro")
            idArtilheiro = input()
            comando = f"insert into titulo(idComp, idClube, idArtilheiro) values('{str(idComp)}', '{str(idClube)}', '{str(idArtilheiro)}')"
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
                "| idLesao" + " " * 32 + "| descricao" + " " * 40 + "|")
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

        if opcao == 7:
            comando = "select * from jogador"
            cursor.execute(comando)
            result = cursor.fetchall()
            print(("+" + "-" * 40) * 8 + "+")
            print("| idJogador" + " "*30 + "| nome" + " "*35 +
                  "| data de nascimento " + "| posicao" + " "*32, end="")
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
                "| idLesao" + " "*32 + "| idJogador" + " "*30 + "| data de lesao"+" "*26 + "| gravidade"+" "*30 + "| região" +" "*33 + "| data de recuperação" + " "*20 + "|")
            for linha in result:
                print(("+" + "-" * 40) * 6 + "+")
                print("| " + str(linha[0]) + " " * (39 - len(str(linha[0]))), end="")
                print("| " + str(linha[1]) + " " * (39 - len(str(linha[1]))), end="")
                print("| " + str(linha[2]) + " " * (39 - len(str(linha[2]))), end="")
                print("| " + str(linha[3]) + " " * (39 - len(str(linha[3]))), end="")
                print("| " + str(linha[4]) + " " * (39 - len(str(linha[4]))), end="")
                print("| " + str(linha[5]) + " " * (39 - len(str(linha[5]))) + "|")
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
                print("| " + str(linha[0]) + " " * (39 - len(str(linha[0]))), end="")
                print("| " + str(linha[1]) + " " * (39 - len(str(linha[1]))), end="")
                print("| " + str(linha[2]) + " " * (39 - len(str(linha[2]))), end="")
                print("| " + str(linha[3]) + " " * (39 - len(str(linha[3]))), end="")
                print("| " + str(linha[4]) + " " * (39 - len(str(linha[4]))), end="")
                print("| " + str(linha[5]) + " " * (39 - len(str(linha[5]))) + "|")
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
                print("| " + str(linha[0]) + " " * (39 - len(str(linha[0]))), end="")
                print("| " + str(linha[1]) + " " * (39 - len(str(linha[1]))), end="")
                print("| " + str(linha[2]) + " " * (39 - len(str(linha[2]))), end="")
                print("| " + str(linha[3]) + " " * (39 - len(str(linha[3]))), end="")
                print("| " + str(linha[4]) + " " * (39 - len(str(linha[4]))) + "|")
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
                print("| " + str(linha[0]) + " " * (39 - len(str(linha[0]))), end="")
                print("| " + str(linha[1]) + " " * (39 - len(str(linha[1]))), end="")
                print("| " + str(linha[2]) + " " * (39 - len(str(linha[2]))), end="")
                print("| " + str(linha[3]) + " " * (39 - len(str(linha[3]))), end="")
                print("| " + str(linha[4]) + " " * (39 - len(str(linha[4]))) + "|")
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
                print("| " + str(linha[0]) + " " * (39 - len(str(linha[0]))), end="")
                print("| " + str(linha[1]) + " " * (39 - len(str(linha[1]))), end="")
                print("| " + str(linha[2]) + " " * (39 - len(str(linha[2]))), end="")
                print("| " + str(linha[3]) + " " * (39 - len(str(linha[3]))), end="")
                print("| " + str(linha[4]) + " " * (39 - len(str(linha[4]))) + "|")
            print(("+" + "-" * 40) * 5 + "+")
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
