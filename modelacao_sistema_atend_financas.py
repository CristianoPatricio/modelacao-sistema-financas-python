from geracao_tempos_utentes import listaUtentes
import datetime
#////////////////////////////////////  TESTING  //////////////////////////////////////////////#
'''class Cliente:
  def __init__(cliente, id, tchegada, tatendimento, tipoassunto, tatend2fase1, tatend2fase2, tatend3fase):
    cliente.id = id
    cliente.tchegada = tchegada
    cliente.tatendimento = tatendimento
    cliente.tipoassunto = tipoassunto
    cliente.tatend2fase1 = tatend2fase1
    cliente.tatend2fase2 = tatend2fase2
    cliente.tatend3fase = tatend3fase

tchegada = [1021,1021,1021,3456,5678,8767,9867,10092,11234,20545]
tatendimento = [5000,5200,5400,1234,5600,1000,1000,1000,1000,1000]
tipoassunto = ["A","A","A","B",'B','B','C','C','C',"-"]
tatend2fase1 = [5789,7987,456,500,500,500,5000,1000,1000,0]
tatend2fase2 = [0,2000,0,0,1000,0,0,2000,0,0]
tatend3fase = [0,500,1000,0,8889,500,0,500,500,1000]

listaUtentes = []

for i in range(0,10):
    if (i%2 == 0): #gerais
        listaUtentes.append(Cliente('C'+str(i+1),tchegada[i], tatendimento[i], tipoassunto[i], tatend2fase1[i], tatend2fase2[i], tatend3fase[i]))
    else: #prioritarios
        listaUtentes.append(Cliente('P'+str(i+1),tchegada[i], tatendimento[i], tipoassunto[i], tatend2fase1[i], tatend2fase2[i], tatend3fase[i]))

#for i in listaUtentes:
#    print(i.id,i.tchegada,i.tatendimento,i.tipoassunto,i.tatend2fase1,i.tatend2fase2,i.tatend3fase)'''
#/////////////////////////////////////////////////////////////////////////////////////////////#

#//////////////////////////////////FUNCOES E ROTINAS DE SIMULACAO //////////////////////////////////////#
#OBJETIVO: inserir utente fila triagem
def inserirUtenteFilaTriagem(NUtente, clock, tatendimento):
    item = []
    item.append(NUtente)
    item.append(clock)
    item.append(NUtente[0])
    item.append(tatendimento)
    filaTriagem.append(item)

#OBJETIVO: inserir utente fila PostoA
def inserirUtenteFilaPostoA(idUtente, clock, tatendimento):
    item = []
    item.append(idUtente)
    item.append(clock)
    item.append(idUtente[0])
    item.append(tatendimento)
    filaPostoA.append(item)

#OBJETIVO: inserir utente fila PostoA2Vez
def inserirUtenteFilaPostoA2Vez(idUtente, clock, tatendimento):
    item = []
    item.append(idUtente)
    item.append(clock)
    item.append(idUtente[0])
    item.append(tatendimento)
    filaPostoA2Vez.append(item)

#OBJETIVO: inserir utente fila PostoB
def inserirUtenteFilaPostoB(idUtente, clock, tatendimento):
    item = []
    item.append(idUtente)
    item.append(clock)
    item.append(idUtente[0])
    item.append(tatendimento)
    filaPostoB.append(item)

#OBJETIVO: inserir utente fila PostoB2Vez
def inserirUtenteFilaPostoB2Vez(idUtente, clock, tatendimento):
    item = []
    item.append(idUtente)
    item.append(clock)
    item.append(idUtente[0])
    item.append(tatendimento)
    filaPostoB2Vez.append(item)

#OBJETIVO: inserir utente fila PostoC
def inserirUtenteFilaPostoC(idUtente, clock, tatendimento):
    item = []
    item.append(idUtente)
    item.append(clock)
    item.append(idUtente[0])
    item.append(tatendimento)
    filaPostoC.append(item)

#OBJETIVO: inserir utente fila PostoC2Vez
def inserirUtenteFilaPostoC2Vez(idUtente, clock, tatendimento):
    item = []
    item.append(idUtente)
    item.append(clock)
    item.append(idUtente[0])
    item.append(tatendimento)
    filaPostoC2Vez.append(item)

#OBJETIVO: inserir utente fila Tesouraria
def inserirUtenteFilaTesouraria(idUtente, clock, tatendimento):
    item = []
    item.append(idUtente)
    item.append(clock)
    item.append(idUtente[0])
    item.append(tatendimento)
    filaTesouraria.append(item)

#OBJETIVO: remover utentes da fila de espera da triagem
def removerUtenteFilaTriagem(indice):
    del filaTriagem[indice]

#OBJETIVO: remover utentes da fila de espera do PostoA
def removerUtenteFilaPostoA(indice):
    del filaPostoA[indice]

#OBJETIVO: remover utentes da fila de espera do PostoA2Vez
def removerUtenteFilaPostoA2Vez(indice):
    del filaPostoA2Vez[indice]

#OBJETIVO: remover utentes da fila de espera do PostoB
def removerUtenteFilaPostoB(indice):
    del filaPostoB[indice]

#OBJETIVO: remover utentes da fila de espera do PostoB2Vez
def removerUtenteFilaPostoB2Vez(indice):
    del filaPostoB2Vez[indice]

#OBJETIVO: remover utentes da fila de espera do PostoC
def removerUtenteFilaPostoC(indice):
    del filaPostoC[indice]

#OBJETIVO: remover utentes da fila de espera 2 do PostoC
def removerUtenteFilaPostoC2Vez(indice):
    del filaPostoC2Vez[indice]

#OBJETIVO: remover utentes da fila de espera da Tesouraria
def removerUtenteFilaTesouraria(indice):
    del filaTesouraria[indice]

#OBJETIVO: obter o tempo do clock e o tipo de evento da próxima iteração
def gestaoTempo(TPChegada, TPTriagem, TPPostoA1, TPPostoA2, TPPostoB1, TPPostoB2, TPPostoC, TPTesouraria):
    clock = min(TPChegada,TPTriagem,TPPostoA1,TPPostoA2,TPPostoB1,TPPostoB2,TPPostoC,TPTesouraria)

    if (clock == TPChegada):
        tipoEvento = 0 #chegada
    elif (clock == TPTriagem):
        tipoEvento = 1 #partida triagem
    elif (clock == TPPostoA1):
        tipoEvento = 2 #partida PostoA1
    elif (clock == TPPostoA2):
        tipoEvento = 3 #partida PostoA2
    elif (clock == TPPostoB1):
        tipoEvento = 4 #partida PostoB1
    elif (clock == TPPostoB2):
        tipoEvento = 5 #partida PostoB2
    elif (clock == TPPostoC):
        tipoEvento = 6 #partida PostoC
    elif (clock == TPTesouraria):
        tipoEvento = 7 #partida Tesouraria

    if (TPChegada == INFINITO and TPTriagem == INFINITO and TPPostoA1 == INFINITO and TPPostoA2 == INFINITO and TPPostoB1 == INFINITO and TPPostoB2 == INFINITO and TPPostoC == INFINITO and TPTesouraria == INFINITO):
        tipoEvento = -1 #fim da simulação
    
    return [clock,tipoEvento]

#OBJETIVO: evento de chegada de um utente ao sistema
def eventoChegada(clock, listaUtentes, n):
    #Variables
    global TPChegada
    global ETriagem
    global TUFTriagem
    global NUSistema
    global TATriagem
    global TPTriagem
    global TTOcupacaoTriagem
    global TTOcupacaoTriagem0911
    global TTOcupacaoTriagem1113
    global TTOcupacaoTriagem1315
    global TTOcupacaoTriagem1517
    global UtentesTriagem

    if (n+1 == len(listaUtentes)):
        TPChegada = INFINITO
    else:
        TPChegada = listaUtentes[n+1].tchegada
    NUtente = listaUtentes[n].id
    if (ETriagem == 1): #ocupado
        inserirUtenteFilaTriagem(NUtente, clock, listaUtentes[n].tatendimento)
        TUFTriagem = TUFTriagem + 1
    else:
        NUSistema = NUSistema + 1
        ETriagem = 1 #ocupado
        UtentesTriagem.append(NUtente)
        TATriagem = listaUtentes[n].tatendimento
        TPTriagem = clock + TATriagem
        TTOcupacaoTriagem = TTOcupacaoTriagem + TATriagem
        if (clock >= 0 and clock <= 7200):
            TTOcupacaoTriagem0911 = TTOcupacaoTriagem0911 + TATriagem
        elif (clock > 7200 and clock <= 14400):
            TTOcupacaoTriagem1113 = TTOcupacaoTriagem1113 + TATriagem
        elif (clock > 14400 and clock <= 21600):
            TTOcupacaoTriagem1315 = TTOcupacaoTriagem1315 + TATriagem
        else:
            TTOcupacaoTriagem1517 = TTOcupacaoTriagem1517 + TATriagem

#OBJETIVO: evento de partida do posto de triagem
def eventoPartidaTriagem(clock, listaUtentes):
     #Variables
    global TPChegada
    global ETriagem
    global TUFTriagem
    global NUSistema
    global TATriagem
    global TPTriagem
    global TTOcupacaoTriagem
    global TTOcupacaoTriagem0911
    global TTOcupacaoTriagem1113
    global TTOcupacaoTriagem1315
    global TTOcupacaoTriagem1517
    global TTEsperaTriagem
    global TTEsperaTriagem0911
    global TTEsperaTriagem1113
    global TTEsperaTriagem1315
    global TTEsperaTriagem1517
    global UtentesTriagem

    prioritarios = []
    gerais = []
    prioritariosExist = False

    utente2Fase = UtentesTriagem[0]
    del UtentesTriagem[0]

    if (filaTriagem == []):
        ETriagem = 0 #livre
        TPTriagem = INFINITO
    else:
        for item in filaTriagem:
            if item.__contains__("P"):
                prioritarios.append(filaTriagem.index(item))
                prioritariosExist = True
            else:
                gerais.append(filaTriagem.index(item))
        if (prioritariosExist): 
            indice = min(prioritarios) 
        else:
            indice = min(gerais)
        TChegada = filaTriagem[indice][1]
        TEsperaUtente = clock - TChegada
        NUSistema = NUSistema + 1
        UtentesTriagem.append(filaTriagem[indice][0])
        TATriagem = filaTriagem[indice][3]
        TPTriagem = clock + TATriagem
        removerUtenteFilaTriagem(indice)
        TTEsperaTriagem = TTEsperaTriagem + TEsperaUtente
        TTOcupacaoTriagem = TTOcupacaoTriagem + TATriagem
        if (clock >= 0 and clock <= 7200):
            TTOcupacaoTriagem0911 = TTOcupacaoTriagem0911 + TATriagem
            TTEsperaTriagem0911 = TTEsperaTriagem0911 + TEsperaUtente
        elif (clock > 7200 and clock <= 14400):
            TTOcupacaoTriagem1113 = TTOcupacaoTriagem1113 + TATriagem
            TTEsperaTriagem1113 = TTEsperaTriagem1113 + TEsperaUtente
        elif (clock > 14400 and clock <= 21600):
            TTOcupacaoTriagem1315 = TTOcupacaoTriagem1315 + TATriagem
            TTEsperaTriagem1315 = TTEsperaTriagem1315 + TEsperaUtente
        else:
            TTOcupacaoTriagem1517 = TTOcupacaoTriagem1517 + TATriagem
            TTEsperaTriagem1517 = TTEsperaTriagem1517 + TEsperaUtente
    
    for item in listaUtentes:
        if item.id.__contains__(utente2Fase):
            tipoAssunto = item.tipoassunto
            indice = listaUtentes.index(item)

    if (tipoAssunto == 'A'):
        eventoChegadaPostoA(indice,clock,1)
    elif (tipoAssunto == 'B'):
        eventoChegadaPostoB(indice,clock,1)
    elif (tipoAssunto == 'C'):
        eventoChegadaPostoC(indice,clock,1)
    elif (tipoAssunto == '-'):
        eventoChegadaTesouraria(indice,clock)

#OBJETIVO: evento de chegada ao posto A1
def eventoChegadaPostoA(indexUtente, clock, nvezes):
    #variáveis
    global EPostoA1
    global EPostoA2
    global TUFPostoA
    global TAPostoA2
    global TPPostoA2
    global TTOcupacaoPostoA2
    global TTOcupacaoPostoA20911
    global TTOcupacaoPostoA21113
    global TTOcupacaoPostoA21315
    global TTOcupacaoPostoA21517
    global TAPostoA1
    global TPPostoA1
    global TTOcupacaoPostoA1
    global TTOcupacaoPostoA10911
    global TTOcupacaoPostoA11113
    global TTOcupacaoPostoA11315
    global TTOcupacaoPostoA11517
    global NUPostoA
    global UtentesPostoA1
    global UtentesPostoA2

    if (EPostoA1 == 1): #ocupado
        if (EPostoA2 == 1): #ocupado
            if (nvezes == 2): #utente que regressa ao PostoA
                inserirUtenteFilaPostoA2Vez(listaUtentes[indexUtente].id, clock, listaUtentes[indexUtente].tatend2fase2)
                TUFPostoA = TUFPostoA + 1
            else:
                inserirUtenteFilaPostoA(listaUtentes[indexUtente].id, clock, listaUtentes[indexUtente].tatend2fase1)
                TUFPostoA = TUFPostoA + 1
        else:
            if (nvezes == 2): #utente que regressa ao PostoA
                EPostoA2 = 1 #ocupado
                TAPostoA2 = listaUtentes[indexUtente].tatend2fase2
                TPPostoA2 = clock + TAPostoA2
                TTOcupacaoPostoA2 = TTOcupacaoPostoA2 + TAPostoA2
                if (clock >= 0 and clock <= 7200):
                    TTOcupacaoPostoA20911 = TTOcupacaoPostoA20911 + TAPostoA2
                elif (clock > 7200 and clock <= 14400):
                    TTOcupacaoPostoA21113 = TTOcupacaoPostoA21113 + TAPostoA2
                elif (clock > 14400 and clock <= 21600):
                    TTOcupacaoPostoA21315 = TTOcupacaoPostoA21315 + TAPostoA2
                else:
                    TTOcupacaoPostoA21517 = TTOcupacaoPostoA21517 + TAPostoA2
            else:
                EPostoA2 = 1 #ocupado
                NUPostoA = NUPostoA + 1
                UtentesPostoA2.append(listaUtentes[indexUtente].id)
                TAPostoA2 = listaUtentes[indexUtente].tatend2fase1
                TPPostoA2 = clock + TAPostoA2
                TTOcupacaoPostoA2 = TTOcupacaoPostoA2 + TAPostoA2
                if (clock >= 0 and clock <= 7200):
                    TTOcupacaoPostoA20911 = TTOcupacaoPostoA20911 + TAPostoA2
                elif (clock > 7200 and clock <= 14400):
                    TTOcupacaoPostoA21113 = TTOcupacaoPostoA21113 + TAPostoA2
                elif (clock > 14400 and clock <= 21600):
                    TTOcupacaoPostoA21315 = TTOcupacaoPostoA21315 + TAPostoA2
                else:
                    TTOcupacaoPostoA21517 = TTOcupacaoPostoA21517 + TAPostoA2
    else:
        if (nvezes == 2): #utente que regressa ao PostoA
            EPostoA1 = 1 #ocupado
            TAPostoA1 = listaUtentes[indexUtente].tatend2fase2
            TPPostoA1 = clock + TAPostoA1
            TTOcupacaoPostoA1 = TTOcupacaoPostoA1 + TAPostoA1
            if (clock >= 0 and clock <= 7200):
                TTOcupacaoPostoA10911 = TTOcupacaoPostoA10911 + TAPostoA1
            elif (clock > 7200 and clock <= 14400):
                TTOcupacaoPostoA11113 = TTOcupacaoPostoA11113 + TAPostoA1
            elif (clock > 14400 and clock <= 21600):
                TTOcupacaoPostoA11315 = TTOcupacaoPostoA11315 + TAPostoA1
            else:
                TTOcupacaoPostoA11517 = TTOcupacaoPostoA11517 + TAPostoA1
        else:
            EPostoA1 = 1 #ocupado
            NUPostoA = NUPostoA + 1
            UtentesPostoA1.append(listaUtentes[indexUtente].id)
            TAPostoA1 = listaUtentes[indexUtente].tatend2fase1
            TPPostoA1 = clock + TAPostoA1
            TTOcupacaoPostoA1 = TTOcupacaoPostoA1 + TAPostoA1
            if (clock >= 0 and clock <= 7200):
                TTOcupacaoPostoA10911 = TTOcupacaoPostoA10911 + TAPostoA1
            elif (clock > 7200 and clock <= 14400):
                TTOcupacaoPostoA11113 = TTOcupacaoPostoA11113 + TAPostoA1
            elif (clock > 14400 and clock <= 21600):
                TTOcupacaoPostoA11315 = TTOcupacaoPostoA11315 + TAPostoA1
            else:
                TTOcupacaoPostoA11517 = TTOcupacaoPostoA11517 + TAPostoA1

#OBJETIVO: evento de partida do PostoA1
def eventoPartidaPostoA1(clock):
    #variáveis
    global EPostoA1
    global TPPostoA1
    global TAPostoA1
    global TTEsperaPostoA
    global TTEsperaPostoA0911
    global TTEsperaPostoA1113
    global TTEsperaPostoA1315
    global TTEsperaPostoA1517
    global TTOcupacaoPostoA1
    global TTOcupacaoPostoA10911
    global TTOcupacaoPostoA11113
    global TTOcupacaoPostoA11315
    global TTOcupacaoPostoA11517
    global NUPostoA
    global UtentesPostoA1

    prioritarios = []
    gerais = []
    prioritariosExist = False
    prioritarios2Vez = []
    gerais2Vez = []
    prioritariosExist2Vez = False
    utente3Fase = ''

    if (len(UtentesPostoA1) != 0):
        utente3Fase = UtentesPostoA1[0]
        del UtentesPostoA1[0]

    if (filaPostoA == []):
        if (filaPostoA2Vez == []):
            EPostoA1 = 0 #livre
            TPPostoA1 = INFINITO
        else:
            for item in filaPostoA2Vez:
                if item.__contains__("P"):
                    prioritarios2Vez.append(filaPostoA2Vez.index(item))
                    prioritariosExist2Vez = True
                else:
                    gerais2Vez.append(filaPostoA2Vez.index(item))

            if (prioritariosExist2Vez): 
                indice = min(prioritarios2Vez) 
            else:
                indice = min(gerais2Vez)

            TChegada = filaPostoA2Vez[indice][1]
            TEsperaUtente = clock - TChegada
            TAPostoA1 = filaPostoA2Vez[indice][3]
            TPPostoA1 = clock + TAPostoA1
            removerUtenteFilaPostoA2Vez(indice)
            TTEsperaPostoA = TTEsperaPostoA + TEsperaUtente
            TTOcupacaoPostoA1 = TTOcupacaoPostoA1 + TAPostoA1
            if (clock >= 0 and clock <= 7200):
                TTOcupacaoPostoA10911 = TTOcupacaoPostoA10911 + TAPostoA1
                TTEsperaPostoA0911 = TTEsperaPostoA0911 + TEsperaUtente
            elif (clock > 7200 and clock <= 14400):
                TTOcupacaoPostoA11113 = TTOcupacaoPostoA11113 + TAPostoA1
                TTEsperaPostoA1113 = TTEsperaPostoA1113 + TEsperaUtente
            elif (clock > 14400 and clock <= 21600):
                TTOcupacaoPostoA11315 = TTOcupacaoPostoA11315 + TAPostoA1
                TTEsperaPostoA1315 = TTEsperaPostoA1315 + TEsperaUtente
            else:
                TTOcupacaoPostoA11517 = TTOcupacaoPostoA11517 + TAPostoA1
                TTEsperaPostoA1517 = TTEsperaPostoA1517 + TEsperaUtente
    else:
        if (filaPostoA2Vez == []):
            for item in filaPostoA:
                if item.__contains__("P"):
                    prioritarios.append(filaPostoA.index(item))
                    prioritariosExist = True
                else:
                    gerais.append(filaPostoA.index(item))

            if (prioritariosExist): 
                indice = min(prioritarios) 
            else:
                indice = min(gerais)

            TChegada = filaPostoA[indice][1]
            NUPostoA = NUPostoA + 1
            UtentesPostoA1.append(filaPostoA[indice][0])
            TEsperaUtente = clock - TChegada
            TAPostoA1 = filaPostoA[indice][3]
            TPPostoA1 = clock + TAPostoA1
            removerUtenteFilaPostoA(indice)
            TTEsperaPostoA = TTEsperaPostoA + TEsperaUtente
            TTOcupacaoPostoA1 = TTOcupacaoPostoA1 + TAPostoA1
            if (clock >= 0 and clock <= 7200):
                TTOcupacaoPostoA10911 = TTOcupacaoPostoA10911 + TAPostoA1
                TTEsperaPostoA0911 = TTEsperaPostoA0911 + TEsperaUtente
            elif (clock > 7200 and clock <= 14400):
                TTOcupacaoPostoA11113 = TTOcupacaoPostoA11113 + TAPostoA1
                TTEsperaPostoA1113 = TTEsperaPostoA1113 + TEsperaUtente
            elif (clock > 14400 and clock <= 21600):
                TTOcupacaoPostoA11315 = TTOcupacaoPostoA11315 + TAPostoA1
                TTEsperaPostoA1315 = TTEsperaPostoA1315 + TEsperaUtente
            else:
                TTOcupacaoPostoA11517 = TTOcupacaoPostoA11517 + TAPostoA1
                TTEsperaPostoA1517 = TTEsperaPostoA1517 + TEsperaUtente
        else:
            for item in filaPostoA:
                if item.__contains__("P"):
                    prioritarios.append(filaPostoA.index(item))
                    prioritariosExist = True
            
            if (prioritariosExist != True):
                for item in filaPostoA2Vez:
                    if item.__contains__("P"):
                        prioritarios2Vez.append(filaPostoA2Vez.index(item))
                        prioritariosExist2Vez = True
                    else:
                        gerais2Vez.append(filaPostoA2Vez.index(item))
            
            if (prioritariosExist):
                indice = min(prioritarios)

                TChegada = filaPostoA[indice][1]
                NUPostoA = NUPostoA + 1
                UtentesPostoA1.append(filaPostoA[indice][0])
                TEsperaUtente = clock - TChegada
                TAPostoA1 = filaPostoA[indice][3]
                TPPostoA1 = clock + TAPostoA1
                removerUtenteFilaPostoA(indice)
                TTEsperaPostoA = TTEsperaPostoA + TEsperaUtente
                TTOcupacaoPostoA1 = TTOcupacaoPostoA1 + TAPostoA1
                if (clock >= 0 and clock <= 7200):
                    TTOcupacaoPostoA10911 = TTOcupacaoPostoA10911 + TAPostoA1
                    TTEsperaPostoA0911 = TTEsperaPostoA0911 + TEsperaUtente
                elif (clock > 7200 and clock <= 14400):
                    TTOcupacaoPostoA11113 = TTOcupacaoPostoA11113 + TAPostoA1
                    TTEsperaPostoA1113 = TTEsperaPostoA1113 + TEsperaUtente
                elif (clock > 14400 and clock <= 21600):
                    TTOcupacaoPostoA11315 = TTOcupacaoPostoA11315 + TAPostoA1
                    TTEsperaPostoA1315 = TTEsperaPostoA1315 + TEsperaUtente
                else:
                    TTOcupacaoPostoA11517 = TTOcupacaoPostoA11517 + TAPostoA1
                    TTEsperaPostoA1517 = TTEsperaPostoA1517 + TEsperaUtente
            else:
                if (prioritariosExist2Vez):
                    indice = min(prioritarios2Vez)
                else:
                    indice = min(gerais2Vez)

                TChegada = filaPostoA2Vez[indice][1]
                TEsperaUtente = clock - TChegada
                TAPostoA1 = filaPostoA2Vez[indice][3]
                TPPostoA1 = clock + TAPostoA1
                removerUtenteFilaPostoA2Vez(indice)
                TTEsperaPostoA = TTEsperaPostoA + TEsperaUtente
                TTOcupacaoPostoA1 = TTOcupacaoPostoA1 + TAPostoA1
                if (clock >= 0 and clock <= 7200):
                    TTOcupacaoPostoA10911 = TTOcupacaoPostoA10911 + TAPostoA1
                    TTEsperaPostoA0911 = TTEsperaPostoA0911 + TEsperaUtente
                elif (clock > 7200 and clock <= 14400):
                    TTOcupacaoPostoA11113 = TTOcupacaoPostoA11113 + TAPostoA1
                    TTEsperaPostoA1113 = TTEsperaPostoA1113 + TEsperaUtente
                elif (clock > 14400 and clock <= 21600):
                    TTOcupacaoPostoA11315 = TTOcupacaoPostoA11315 + TAPostoA1
                    TTEsperaPostoA1315 = TTEsperaPostoA1315 + TEsperaUtente
                else:
                    TTOcupacaoPostoA11517 = TTOcupacaoPostoA11517 + TAPostoA1
                    TTEsperaPostoA1517 = TTEsperaPostoA1517 + TEsperaUtente

    if (utente3Fase != ''):
        for item in listaUtentes:
            if item.id.__contains__(utente3Fase):
                index = listaUtentes.index(item)

        if (listaUtentes[index].tatend3fase != 0):
            eventoChegadaTesouraria(index,clock)

#OBJETIVO: evento de partida do PostoA2
def eventoPartidaPostoA2(clock):
    #variáveis
    global EPostoA2
    global TPPostoA2
    global TAPostoA2
    global TTEsperaPostoA
    global TTEsperaPostoA0911
    global TTEsperaPostoA1113
    global TTEsperaPostoA1315
    global TTEsperaPostoA1517
    global TTOcupacaoPostoA2
    global TTOcupacaoPostoA20911
    global TTOcupacaoPostoA21113
    global TTOcupacaoPostoA21315
    global TTOcupacaoPostoA21517
    global NUPostoA
    global UtentesPostoA2

    prioritarios = []
    gerais = []
    prioritariosExist = False
    prioritarios2Vez = []
    gerais2Vez = []
    prioritariosExist2Vez = False
    utente3Fase = ''

    if (len(UtentesPostoA2) != 0):
        utente3Fase = UtentesPostoA2[0]
        del UtentesPostoA2[0]

    if (filaPostoA == []):
        if (filaPostoA2Vez == []):
            EPostoA2 = 0 #livre
            TPPostoA2 = INFINITO
        else:
            for item in filaPostoA2Vez:
                if item.__contains__("P"):
                    prioritarios2Vez.append(filaPostoA2Vez.index(item))
                    prioritariosExist2Vez = True
                else:
                    gerais2Vez.append(filaPostoA2Vez.index(item))

            if (prioritariosExist2Vez): 
                indice = min(prioritarios2Vez) 
            else:
                indice = min(gerais2Vez)

            TChegada = filaPostoA2Vez[indice][1]
            TEsperaUtente = clock - TChegada
            TAPostoA2 = filaPostoA2Vez[indice][3]
            TPPostoA2 = clock + TAPostoA2
            removerUtenteFilaPostoA2Vez(indice)
            TTEsperaPostoA = TTEsperaPostoA + TEsperaUtente
            TTOcupacaoPostoA2 = TTOcupacaoPostoA2 + TAPostoA2
            if (clock >= 0 and clock <= 7200):
                TTOcupacaoPostoA20911 = TTOcupacaoPostoA20911 + TAPostoA2
                TTEsperaPostoA0911 = TTEsperaPostoA0911 + TEsperaUtente
            elif (clock > 7200 and clock <= 14400):
                TTOcupacaoPostoA21113 = TTOcupacaoPostoA21113 + TAPostoA2
                TTEsperaPostoA1113 = TTEsperaPostoA1113 + TEsperaUtente
            elif (clock > 14400 and clock <= 21600):
                TTOcupacaoPostoA21315 = TTOcupacaoPostoA21315 + TAPostoA2
                TTEsperaPostoA1315 = TTEsperaPostoA1315 + TEsperaUtente
            else:
                TTOcupacaoPostoA21517 = TTOcupacaoPostoA21517 + TAPostoA2
                TTEsperaPostoA1517 = TTEsperaPostoA1517 + TEsperaUtente
    else:
        if (filaPostoA2Vez == []):
            for item in filaPostoA:
                if item.__contains__("P"):
                    prioritarios.append(filaPostoA.index(item))
                    prioritariosExist = True
                else:
                    gerais.append(filaPostoA.index(item))

            if (prioritariosExist): 
                indice = min(prioritarios) 
            else:
                indice = min(gerais)
                
            TChegada = filaPostoA[indice][1]
            NUPostoA = NUPostoA + 1
            UtentesPostoA2.append(filaPostoA[indice][0])
            TEsperaUtente = clock - TChegada
            TAPostoA2 = filaPostoA[indice][3]
            TPPostoA2 = clock + TAPostoA2
            removerUtenteFilaPostoA(indice)
            TTEsperaPostoA = TTEsperaPostoA + TEsperaUtente
            TTOcupacaoPostoA2 = TTOcupacaoPostoA2 + TAPostoA2
            if (clock >= 0 and clock <= 7200):
                TTOcupacaoPostoA20911 = TTOcupacaoPostoA20911 + TAPostoA2
                TTEsperaPostoA0911 = TTEsperaPostoA0911 + TEsperaUtente
            elif (clock > 7200 and clock <= 14400):
                TTOcupacaoPostoA21113 = TTOcupacaoPostoA21113 + TAPostoA2
                TTEsperaPostoA1113 = TTEsperaPostoA1113 + TEsperaUtente
            elif (clock > 14400 and clock <= 21600):
                TTOcupacaoPostoA21315 = TTOcupacaoPostoA21315 + TAPostoA2
                TTEsperaPostoA1315 = TTEsperaPostoA1315 + TEsperaUtente
            else:
                TTOcupacaoPostoA21517 = TTOcupacaoPostoA21517 + TAPostoA2
                TTEsperaPostoA1517 = TTEsperaPostoA1517 + TEsperaUtente
        else:
            for item in filaPostoA:
                if item.__contains__("P"):
                    prioritarios.append(filaPostoA.index(item))
                    prioritariosExist = True
            
            if (prioritariosExist != True):
                for item in filaPostoA2Vez:
                    if item.__contains__("P"):
                        prioritarios2Vez.append(filaPostoA2Vez.index(item))
                        prioritariosExist2Vez = True
                    else:
                        gerais2Vez.append(filaPostoA2Vez.index(item))
            
            if (prioritariosExist):
                indice = min(prioritarios)

                TChegada = filaPostoA[indice][1]
                NUPostoA = NUPostoA + 1
                UtentesPostoA2.append(filaPostoA[indice][0])
                TEsperaUtente = clock - TChegada
                TAPostoA2 = filaPostoA[indice][3]
                TPPostoA2 = clock + TAPostoA2
                removerUtenteFilaPostoA(indice)
                TTEsperaPostoA = TTEsperaPostoA + TEsperaUtente
                TTOcupacaoPostoA2 = TTOcupacaoPostoA2 + TAPostoA2
                if (clock >= 0 and clock <= 7200):
                    TTOcupacaoPostoA20911 = TTOcupacaoPostoA20911 + TAPostoA2
                    TTEsperaPostoA0911 = TTEsperaPostoA0911 + TEsperaUtente
                elif (clock > 7200 and clock <= 14400):
                    TTOcupacaoPostoA21113 = TTOcupacaoPostoA21113 + TAPostoA2
                    TTEsperaPostoA1113 = TTEsperaPostoA1113 + TEsperaUtente
                elif (clock > 14400 and clock <= 21600):
                    TTOcupacaoPostoA21315 = TTOcupacaoPostoA21315 + TAPostoA2
                    TTEsperaPostoA1315 = TTEsperaPostoA1315 + TEsperaUtente
                else:
                    TTOcupacaoPostoA21517 = TTOcupacaoPostoA21517 + TAPostoA2
                    TTEsperaPostoA1517 = TTEsperaPostoA1517 + TEsperaUtente
            else:
                if (prioritariosExist2Vez):
                    indice = min(prioritarios2Vez)
                else:
                    indice = min(gerais2Vez)

                TChegada = filaPostoA2Vez[indice][1]
                TEsperaUtente = clock - TChegada
                TAPostoA2 = filaPostoA2Vez[indice][3]
                TPPostoA2 = clock + TAPostoA2
                removerUtenteFilaPostoA2Vez(indice)
                TTEsperaPostoA = TTEsperaPostoA + TEsperaUtente
                TTOcupacaoPostoA2 = TTOcupacaoPostoA2 + TAPostoA2
                if (clock >= 0 and clock <= 7200):
                    TTOcupacaoPostoA20911 = TTOcupacaoPostoA20911 + TAPostoA2
                    TTEsperaPostoA0911 = TTEsperaPostoA0911 + TEsperaUtente
                elif (clock > 7200 and clock <= 14400):
                    TTOcupacaoPostoA21113 = TTOcupacaoPostoA21113 + TAPostoA2
                    TTEsperaPostoA1113 = TTEsperaPostoA1113 + TEsperaUtente
                elif (clock > 14400 and clock <= 21600):
                    TTOcupacaoPostoA21315 = TTOcupacaoPostoA21315 + TAPostoA2
                    TTEsperaPostoA1315 = TTEsperaPostoA1315 + TEsperaUtente
                else:
                    TTOcupacaoPostoA21517 = TTOcupacaoPostoA21517 + TAPostoA2
                    TTEsperaPostoA1517 = TTEsperaPostoA1517 + TEsperaUtente
                
    if (utente3Fase != ''):
        for item in listaUtentes:
            if item.id.__contains__(utente3Fase):
                index = listaUtentes.index(item)

        if (listaUtentes[index].tatend3fase != 0):
            eventoChegadaTesouraria(index,clock)

#OBJETIVO: evento de chegada ao posto B
def eventoChegadaPostoB(indexUtente,clock,nvezes):
    #variáveis
    global EPostoB1
    global EPostoB2
    global TUFPostoB
    global TAPostoB2
    global TPPostoB2
    global TTOcupacaoPostoB2
    global TTOcupacaoPostoB20911
    global TTOcupacaoPostoB21113
    global TTOcupacaoPostoB21315
    global TTOcupacaoPostoB21517
    global TAPostoB1
    global TPPostoB1
    global TTOcupacaoPostoB1
    global TTOcupacaoPostoB10911
    global TTOcupacaoPostoB11113
    global TTOcupacaoPostoB11315
    global TTOcupacaoPostoB11517
    global NUPostoB
    global UtentesPostoB1
    global UtentesPostoB2

    if (EPostoB1 == 1): #ocupado
        if (EPostoB2 == 1): #ocupado
            if (nvezes == 2): #utente regressa ao PostoB
                inserirUtenteFilaPostoB2Vez(listaUtentes[indexUtente].id, clock, listaUtentes[indexUtente].tatend2fase2)
                TUFPostoB = TUFPostoB + 1
            else:
                inserirUtenteFilaPostoB(listaUtentes[indexUtente].id, clock, listaUtentes[indexUtente].tatend2fase1)
                TUFPostoB = TUFPostoB + 1
        else:
            if (nvezes == 2): #utente regressa ao PostoB
                EPostoB2 = 1 #ocupado
                TAPostoB2 = listaUtentes[indexUtente].tatend2fase2
                TPPostoB2 = clock + TAPostoB2
                TTOcupacaoPostoB2 = TTOcupacaoPostoB2 + TAPostoB2
                if (clock >= 0 and clock <= 7200):
                    TTOcupacaoPostoB20911 = TTOcupacaoPostoB20911 + TAPostoB2
                elif (clock > 7200 and clock <= 14400):
                    TTOcupacaoPostoB21113 = TTOcupacaoPostoB21113 + TAPostoB2
                elif (clock > 14400 and clock <= 21600):
                    TTOcupacaoPostoB21315 = TTOcupacaoPostoB21315 + TAPostoB2
                else:
                    TTOcupacaoPostoB21517 = TTOcupacaoPostoB21517 + TAPostoB2
            else:
                EPostoB2 = 1 #ocupado
                NUPostoB = NUPostoB + 1
                UtentesPostoB2.append(listaUtentes[indexUtente].id)
                TAPostoB2 = listaUtentes[indexUtente].tatend2fase1
                TPPostoB2 = clock + TAPostoB2
                TTOcupacaoPostoB2 = TTOcupacaoPostoB2 + TAPostoB2
                if (clock >= 0 and clock <= 7200):
                    TTOcupacaoPostoB20911 = TTOcupacaoPostoB20911 + TAPostoB2
                elif (clock > 7200 and clock <= 14400):
                    TTOcupacaoPostoB21113 = TTOcupacaoPostoB21113 + TAPostoB2
                elif (clock > 14400 and clock <= 21600):
                    TTOcupacaoPostoB21315 = TTOcupacaoPostoB21315 + TAPostoB2
                else:
                    TTOcupacaoPostoB21517 = TTOcupacaoPostoB21517 + TAPostoB2
    else:
        if (nvezes == 2): #utente regressa ao PostoB
            EPostoB1 = 1 #ocupado
            TAPostoB1 = listaUtentes[indexUtente].tatend2fase2
            TPPostoB1 = clock + TAPostoB1
            TTOcupacaoPostoB1 = TTOcupacaoPostoB1 + TAPostoB1
            if (clock >= 0 and clock <= 7200):
                TTOcupacaoPostoB10911 = TTOcupacaoPostoB10911 + TAPostoB1
            elif (clock > 7200 and clock <= 14400):
                TTOcupacaoPostoB11113 = TTOcupacaoPostoB11113 + TAPostoB1
            elif (clock > 14400 and clock <= 21600):
                TTOcupacaoPostoB11315 = TTOcupacaoPostoB11315 + TAPostoB1
            else:
                TTOcupacaoPostoB11517 = TTOcupacaoPostoB11517 + TAPostoB1
        else:
            EPostoB1 = 1 #ocupado
            NUPostoB = NUPostoB + 1
            UtentesPostoB1.append(listaUtentes[indexUtente].id)
            TAPostoB1 = listaUtentes[indexUtente].tatend2fase1
            TPPostoB1 = clock + TAPostoB1
            TTOcupacaoPostoB1 = TTOcupacaoPostoB1 + TAPostoB1
            if (clock >= 0 and clock <= 7200):
                TTOcupacaoPostoB10911 = TTOcupacaoPostoB10911 + TAPostoB1
            elif (clock > 7200 and clock <= 14400):
                TTOcupacaoPostoB11113 = TTOcupacaoPostoB11113 + TAPostoB1
            elif (clock > 14400 and clock <= 21600):
                TTOcupacaoPostoB11315 = TTOcupacaoPostoB11315 + TAPostoB1
            else:
                TTOcupacaoPostoB11517 = TTOcupacaoPostoB11517 + TAPostoB1

#OBJETIVO: evento de partida do PostoB1
def eventoPartidaPostoB1(clock):
    #variáveis
    global EPostoB1
    global TPPostoB1
    global TAPostoB1
    global TTEsperaPostoB
    global TTEsperaPostoB0911
    global TTEsperaPostoB1113
    global TTEsperaPostoB1315
    global TTEsperaPostoB1517
    global TTOcupacaoPostoB1
    global TTOcupacaoPostoB10911
    global TTOcupacaoPostoB11113
    global TTOcupacaoPostoB11315
    global TTOcupacaoPostoB11517
    global NUPostoB
    global UtentesPostoB1

    prioritarios = []
    gerais = []
    prioritariosExist = False
    prioritarios2Vez = []
    gerais2Vez = []
    prioritariosExist2Vez = False
    utente3Fase = ''

    if (len(UtentesPostoB1) != 0):
        utente3Fase = UtentesPostoB1[0]
        del UtentesPostoB1[0]

    if (filaPostoB == []):
        if (filaPostoB2Vez == []):
            EPostoB1 = 0 #livre
            TPPostoB1 = INFINITO
        else:
            for item in filaPostoB2Vez:
                if item.__contains__("P"):
                    prioritarios2Vez.append(filaPostoB2Vez.index(item))
                    prioritariosExist2Vez = True
                else:
                    gerais2Vez.append(filaPostoB2Vez.index(item))

            if (prioritariosExist2Vez): 
                indice = min(prioritarios2Vez) 
            else:
                indice = min(gerais2Vez)

            TChegada = filaPostoB2Vez[indice][1]
            TEsperaUtente = clock - TChegada
            TAPostoB1 = filaPostoB2Vez[indice][3]
            TPPostoB1 = clock + TAPostoB1
            removerUtenteFilaPostoB2Vez(indice)
            TTEsperaPostoB = TTEsperaPostoB + TEsperaUtente
            TTOcupacaoPostoB1 = TTOcupacaoPostoB1 + TAPostoB1
            if (clock >= 0 and clock <= 7200):
                TTOcupacaoPostoB10911 = TTOcupacaoPostoB10911 + TAPostoB1
                TTEsperaPostoB0911 = TTEsperaPostoB0911 + TEsperaUtente
            elif (clock > 7200 and clock <= 14400):
                TTOcupacaoPostoB11113 = TTOcupacaoPostoB11113 + TAPostoB1
                TTEsperaPostoB1113 = TTEsperaPostoB1113 + TEsperaUtente
            elif (clock > 14400 and clock <= 21600):
                TTOcupacaoPostoB11315 = TTOcupacaoPostoB11315 + TAPostoB1
                TTEsperaPostoB1315 = TTEsperaPostoB1315 + TEsperaUtente
            else:
                TTOcupacaoPostoB11517 = TTOcupacaoPostoB11517 + TAPostoB1
                TTEsperaPostoB1517 = TTEsperaPostoB1517 + TEsperaUtente
    else:
        if (filaPostoB2Vez == []):
            for item in filaPostoB:
                if item.__contains__("P"):
                    prioritarios.append(filaPostoB.index(item))
                    prioritariosExist = True
                else:
                    gerais.append(filaPostoB.index(item))
            if (prioritariosExist): 
                indice = min(prioritarios) 
            else:
                indice = min(gerais)

            TChegada = filaPostoB[indice][1]
            NUPostoB = NUPostoB + 1
            UtentesPostoB1.append(filaPostoB[indice][0])
            TEsperaUtente = clock - TChegada
            TAPostoB1 = filaPostoB[indice][3]
            TPPostoB1 = clock + TAPostoB1
            removerUtenteFilaPostoB(indice)
            TTEsperaPostoB = TTEsperaPostoB + TEsperaUtente
            TTOcupacaoPostoB1 = TTOcupacaoPostoB1 + TAPostoB1
            if (clock >= 0 and clock <= 7200):
                TTOcupacaoPostoB10911 = TTOcupacaoPostoB10911 + TAPostoB1
                TTEsperaPostoB0911 = TTEsperaPostoB0911 + TEsperaUtente
            elif (clock > 7200 and clock <= 14400):
                TTOcupacaoPostoB11113 = TTOcupacaoPostoB11113 + TAPostoB1
                TTEsperaPostoB1113 = TTEsperaPostoB1113 + TEsperaUtente
            elif (clock > 14400 and clock <= 21600):
                TTOcupacaoPostoB11315 = TTOcupacaoPostoB11315 + TAPostoB1
                TTEsperaPostoB1315 = TTEsperaPostoB1315 + TEsperaUtente
            else:
                TTOcupacaoPostoB11517 = TTOcupacaoPostoB11517 + TAPostoB1
                TTEsperaPostoB1517 = TTEsperaPostoB1517 + TEsperaUtente
        else:
            for item in filaPostoB:
                if item.__contains__("P"):
                    prioritarios.append(filaPostoB.index(item))
                    prioritariosExist = True
            
            if (prioritariosExist != True):
                for item in filaPostoB2Vez:
                    if item.__contains__("P"):
                        prioritarios2Vez.append(filaPostoB2Vez.index(item))
                        prioritariosExist2Vez = True
                    else:
                        gerais2Vez.append(filaPostoB2Vez.index(item))
            
            if (prioritariosExist):
                indice = min(prioritarios)

                TChegada = filaPostoB[indice][1]
                NUPostoB = NUPostoB + 1
                UtentesPostoB1.append(filaPostoB[indice][0])
                TEsperaUtente = clock - TChegada
                TAPostoB1 = filaPostoB[indice][3]
                TPPostoB1 = clock + TAPostoB1
                removerUtenteFilaPostoB(indice)
                TTEsperaPostoB = TTEsperaPostoB + TEsperaUtente
                TTOcupacaoPostoB1 = TTOcupacaoPostoB1 + TAPostoB1
                if (clock >= 0 and clock <= 7200):
                    TTOcupacaoPostoB10911 = TTOcupacaoPostoB10911 + TAPostoB1
                    TTEsperaPostoB0911 = TTEsperaPostoB0911 + TEsperaUtente
                elif (clock > 7200 and clock <= 14400):
                    TTOcupacaoPostoB11113 = TTOcupacaoPostoB11113 + TAPostoB1
                    TTEsperaPostoB1113 = TTEsperaPostoB1113 + TEsperaUtente
                elif (clock > 14400 and clock <= 21600):
                    TTOcupacaoPostoB11315 = TTOcupacaoPostoB11315 + TAPostoB1
                    TTEsperaPostoB1315 = TTEsperaPostoB1315 + TEsperaUtente
                else:
                    TTOcupacaoPostoB11517 = TTOcupacaoPostoB11517 + TAPostoB1
                    TTEsperaPostoB1517 = TTEsperaPostoB1517 + TEsperaUtente
            else:
                if (prioritariosExist2Vez):
                    indice = min(prioritarios2Vez)
                else:
                    indice = min(gerais2Vez)
                
                TChegada = filaPostoB2Vez[indice][1]
                TEsperaUtente = clock - TChegada
                TAPostoB1 = filaPostoB2Vez[indice][3]
                TPPostoB1 = clock + TAPostoB1
                removerUtenteFilaPostoB2Vez(indice)
                TTEsperaPostoB = TTEsperaPostoB + TEsperaUtente
                TTOcupacaoPostoB1 = TTOcupacaoPostoB1 + TAPostoB1
                if (clock >= 0 and clock <= 7200):
                    TTOcupacaoPostoB10911 = TTOcupacaoPostoB10911 + TAPostoB1
                    TTEsperaPostoB0911 = TTEsperaPostoB0911 + TEsperaUtente
                elif (clock > 7200 and clock <= 14400):
                    TTOcupacaoPostoB11113 = TTOcupacaoPostoB11113 + TAPostoB1
                    TTEsperaPostoB1113 = TTEsperaPostoB1113 + TEsperaUtente
                elif (clock > 14400 and clock <= 21600):
                    TTOcupacaoPostoB11315 = TTOcupacaoPostoB11315 + TAPostoB1
                    TTEsperaPostoB1315 = TTEsperaPostoB1315 + TEsperaUtente
                else:
                    TTOcupacaoPostoB11517 = TTOcupacaoPostoB11517 + TAPostoB1
                    TTEsperaPostoB1517 = TTEsperaPostoB1517 + TEsperaUtente
            
    if (utente3Fase != ''):
        for item in listaUtentes:
            if item.id.__contains__(utente3Fase):
                index = listaUtentes.index(item)

        if (listaUtentes[index].tatend3fase != 0):
            eventoChegadaTesouraria(index,clock)

#OBJETIVO: evento de partida do PostoB2
def eventoPartidaPostoB2(clock):
    #variáveis
    global EPostoB2
    global TPPostoB2
    global TAPostoB2
    global TTEsperaPostoB
    global TTEsperaPostoB0911
    global TTEsperaPostoB1113
    global TTEsperaPostoB1315
    global TTEsperaPostoB1517
    global TTOcupacaoPostoB2
    global TTOcupacaoPostoB20911
    global TTOcupacaoPostoB21113
    global TTOcupacaoPostoB21315
    global TTOcupacaoPostoB21517
    global NUPostoB
    global UtentesPostoB2

    prioritarios = []
    gerais = []
    prioritariosExist = False
    prioritarios2Vez = []
    gerais2Vez = []
    prioritariosExist2Vez = False
    utente3Fase = ''

    if (len(UtentesPostoB2) != 0):
        utente3Fase = UtentesPostoB2[0]
        del UtentesPostoB2[0]

    if (filaPostoB == []):
        if (filaPostoB2Vez == []):
            EPostoB2 = 0 #livre
            TPPostoB2 = INFINITO
        else:
            for item in filaPostoB2Vez:
                if item.__contains__("P"):
                    prioritarios2Vez.append(filaPostoB2Vez.index(item))
                    prioritariosExist2Vez = True
                else:
                    gerais2Vez.append(filaPostoB2Vez.index(item))

            if (prioritariosExist2Vez): 
                indice = min(prioritarios2Vez) 
            else:
                indice = min(gerais2Vez)

            TChegada = filaPostoB2Vez[indice][1]
            TEsperaUtente = clock - TChegada
            TAPostoB2 = filaPostoB2Vez[indice][3]
            TPPostoB2 = clock + TAPostoB2
            removerUtenteFilaPostoB2Vez(indice)
            TTEsperaPostoB = TTEsperaPostoB + TEsperaUtente
            TTOcupacaoPostoB2 = TTOcupacaoPostoB2 + TAPostoB2
            if (clock >= 0 and clock <= 7200):
                TTOcupacaoPostoB20911 = TTOcupacaoPostoB20911 + TAPostoB2
                TTEsperaPostoB0911 = TTEsperaPostoB0911 + TEsperaUtente
            elif (clock > 7200 and clock <= 14400):
                TTOcupacaoPostoB21113 = TTOcupacaoPostoB21113 + TAPostoB2
                TTEsperaPostoB1113 = TTEsperaPostoB1113 + TEsperaUtente
            elif (clock > 14400 and clock <= 21600):
                TTOcupacaoPostoB21315 = TTOcupacaoPostoB21315 + TAPostoB2
                TTEsperaPostoB1315 = TTEsperaPostoB1315 + TEsperaUtente
            else:
                TTOcupacaoPostoB21517 = TTOcupacaoPostoB21517 + TAPostoB2
                TTEsperaPostoB1517 = TTEsperaPostoB1517 + TEsperaUtente
    else:
        if (filaPostoB2Vez == []):
            for item in filaPostoB:
                if item.__contains__("P"):
                    prioritarios.append(filaPostoB.index(item))
                    prioritariosExist = True
                else:
                    gerais.append(filaPostoB.index(item))
            if (prioritariosExist): 
                indice = min(prioritarios) 
            else:
                indice = min(gerais)
            TChegada = filaPostoB[indice][1]
            NUPostoB = NUPostoB + 1
            UtentesPostoB2.append(filaPostoB[indice][0])
            TEsperaUtente = clock - TChegada
            TAPostoB2 = filaPostoB[indice][3]
            TPPostoB2 = clock + TAPostoB2
            removerUtenteFilaPostoB(indice)
            TTEsperaPostoB = TTEsperaPostoB + TEsperaUtente
            TTOcupacaoPostoB2 = TTOcupacaoPostoB2 + TAPostoB2
            if (clock >= 0 and clock <= 7200):
                TTOcupacaoPostoB20911 = TTOcupacaoPostoB20911 + TAPostoB2
                TTEsperaPostoB0911 = TTEsperaPostoB0911 + TEsperaUtente
            elif (clock > 7200 and clock <= 14400):
                TTOcupacaoPostoB21113 = TTOcupacaoPostoB21113 + TAPostoB2
                TTEsperaPostoB1113 = TTEsperaPostoB1113 + TEsperaUtente
            elif (clock > 14400 and clock <= 21600):
                TTOcupacaoPostoB21315 = TTOcupacaoPostoB21315 + TAPostoB2
                TTEsperaPostoB1315 = TTEsperaPostoB1315 + TEsperaUtente
            else:
                TTOcupacaoPostoB21517 = TTOcupacaoPostoB21517 + TAPostoB2
                TTEsperaPostoB1517 = TTEsperaPostoB1517 + TEsperaUtente
        else:
            for item in filaPostoB:
                if item.__contains__("P"):
                    prioritarios.append(filaPostoB.index(item))
                    prioritariosExist = True
            
            if(prioritariosExist != True):
                for item in filaPostoB2Vez:
                    if item.__contains__("P"):
                        prioritarios2Vez.append(filaPostoB2Vez.index(item))
                        prioritariosExist2Vez = True
                    else:
                        gerais2Vez.append(filaPostoB2Vez.index(item))
            
            if (prioritariosExist):
                indice = min(prioritarios)

                TChegada = filaPostoB[indice][1]
                NUPostoB = NUPostoB + 1
                UtentesPostoB2.append(filaPostoB[indice][0])
                TEsperaUtente = clock - TChegada
                TAPostoB2 = filaPostoB[indice][3]
                TPPostoB2 = clock + TAPostoB2
                removerUtenteFilaPostoB(indice)
                TTEsperaPostoB = TTEsperaPostoB + TEsperaUtente
                TTOcupacaoPostoB2 = TTOcupacaoPostoB2 + TAPostoB2
                if (clock >= 0 and clock <= 7200):
                    TTOcupacaoPostoB20911 = TTOcupacaoPostoB20911 + TAPostoB2
                    TTEsperaPostoB0911 = TTEsperaPostoB0911 + TEsperaUtente
                elif (clock > 7200 and clock <= 14400):
                    TTOcupacaoPostoB21113 = TTOcupacaoPostoB21113 + TAPostoB2
                    TTEsperaPostoB1113 = TTEsperaPostoB1113 + TEsperaUtente
                elif (clock > 14400 and clock <= 21600):
                    TTOcupacaoPostoB21315 = TTOcupacaoPostoB21315 + TAPostoB2
                    TTEsperaPostoB1315 = TTEsperaPostoB1315 + TEsperaUtente
                else:
                    TTOcupacaoPostoB21517 = TTOcupacaoPostoB21517 + TAPostoB2
                    TTEsperaPostoB1517 = TTEsperaPostoB1517 + TEsperaUtente
            else:
                if (prioritariosExist2Vez):
                    indice = min(prioritarios2Vez)
                else:
                    indice = min(gerais2Vez)
                
                TChegada = filaPostoB2Vez[indice][1]
                TEsperaUtente = clock - TChegada
                TAPostoB2 = filaPostoB2Vez[indice][3]
                TPPostoB2 = clock + TAPostoB2
                removerUtenteFilaPostoB2Vez(indice)
                TTEsperaPostoB = TTEsperaPostoB + TEsperaUtente
                TTOcupacaoPostoB2 = TTOcupacaoPostoB2 + TAPostoB2
                if (clock >= 0 and clock <= 7200):
                    TTOcupacaoPostoB20911 = TTOcupacaoPostoB20911 + TAPostoB2
                    TTEsperaPostoB0911 = TTEsperaPostoB0911 + TEsperaUtente
                elif (clock > 7200 and clock <= 14400):
                    TTOcupacaoPostoB21113 = TTOcupacaoPostoB21113 + TAPostoB2
                    TTEsperaPostoB1113 = TTEsperaPostoB1113 + TEsperaUtente
                elif (clock > 14400 and clock <= 21600):
                    TTOcupacaoPostoB21315 = TTOcupacaoPostoB21315 + TAPostoB2
                    TTEsperaPostoB1315 = TTEsperaPostoB1315 + TEsperaUtente
                else:
                    TTOcupacaoPostoB21517 = TTOcupacaoPostoB21517 + TAPostoB2
                    TTEsperaPostoB1517 = TTEsperaPostoB1517 + TEsperaUtente
            
    if (utente3Fase != ''):
        for item in listaUtentes:
            if item.id.__contains__(utente3Fase):
                index = listaUtentes.index(item)

        if (listaUtentes[index].tatend3fase != 0):
            eventoChegadaTesouraria(index,clock)

#OBJETIVO: evento de chegada ao posto C
def eventoChegadaPostoC(indexUtente,clock,nvezes):
    #variáveis
    global EPostoC
    global TUFPostoC
    global TAPostoC
    global TPPostoC
    global TTOcupacaoPostoC
    global TTOcupacaoPostoC0911
    global TTOcupacaoPostoC1113
    global TTOcupacaoPostoC1315
    global TTOcupacaoPostoC1517
    global NUPostoC
    global UtentesPostoC

    if (EPostoC == 1): #ocupado
        if (nvezes == 2): #utente regressa ao PostoC
            inserirUtenteFilaPostoC2Vez(listaUtentes[indexUtente].id, clock, listaUtentes[indexUtente].tatend2fase2)
            TUFPostoC = TUFPostoC + 1
        else:
            inserirUtenteFilaPostoC(listaUtentes[indexUtente].id, clock, listaUtentes[indexUtente].tatend2fase1)
            TUFPostoC = TUFPostoC + 1
    else:
        if (nvezes == 2): #utente regressa ao PostoC
            EPostoC = 1 #ocupado
            TAPostoC = listaUtentes[indexUtente].tatend2fase2
            TPPostoC = clock + TAPostoC
            TTOcupacaoPostoC = TTOcupacaoPostoC + TAPostoC
            if (clock >= 0 and clock <= 7200):
                TTOcupacaoPostoC0911 = TTOcupacaoPostoC0911 + TAPostoC
            elif (clock > 7200 and clock <= 14400):
                TTOcupacaoPostoC1113 = TTOcupacaoPostoC1113 + TAPostoC
            elif (clock > 14400 and clock <= 21600):
                TTOcupacaoPostoC1315 = TTOcupacaoPostoC1315 + TAPostoC
            else:
                TTOcupacaoPostoC1517 = TTOcupacaoPostoC1517 + TAPostoC
        else:
            EPostoC = 1 #ocupado
            NUPostoC = NUPostoC + 1
            UtentesPostoC.append(listaUtentes[indexUtente].id)
            TAPostoC = listaUtentes[indexUtente].tatend2fase1
            TPPostoC = clock + TAPostoC
            TTOcupacaoPostoC = TTOcupacaoPostoC + TAPostoC
            if (clock >= 0 and clock <= 7200):
                TTOcupacaoPostoC0911 = TTOcupacaoPostoC0911 + TAPostoC
            elif (clock > 7200 and clock <= 14400):
                TTOcupacaoPostoC1113 = TTOcupacaoPostoC1113 + TAPostoC
            elif (clock > 14400 and clock <= 21600):
                TTOcupacaoPostoC1315 = TTOcupacaoPostoC1315 + TAPostoC
            else:
                TTOcupacaoPostoC1517 = TTOcupacaoPostoC1517 + TAPostoC

#OBJETIVO: evento de partida do PostoC
def eventoPartidaPostoC(clock):
    #variáveis
    global EPostoC
    global TPPostoC
    global TAPostoC
    global TTEsperaPostoC
    global TTEsperaPostoC0911
    global TTEsperaPostoC1113
    global TTEsperaPostoC1315
    global TTEsperaPostoC1517
    global TTOcupacaoPostoC
    global TTOcupacaoPostoC0911
    global TTOcupacaoPostoC1113
    global TTOcupacaoPostoC1315
    global TTOcupacaoPostoC1517
    global NUPostoC
    global UtentesPostoC

    prioritarios = []
    gerais = []
    prioritarios2Vez = []
    gerais2Vez = []
    prioritariosExist = False
    prioritariosExist2Vez = False
    utente3Fase = ''
    
    if (len(UtentesPostoC) != 0):
        utente3Fase = UtentesPostoC[0]
        del UtentesPostoC[0]

    if (filaPostoC == []):
        if (filaPostoC2Vez == []):
            EPostoC = 0 #livre
            TPPostoC = INFINITO
        else:
            for item in filaPostoC2Vez:
                if (item.__contains__("P")):
                    prioritarios2Vez.append(filaPostoC2Vez.index(item))
                    prioritariosExist2Vez = True
                else:
                    gerais2Vez.append(filaPostoC2Vez.index(item))
        
            if (prioritariosExist2Vez):
                indice = min(prioritarios2Vez)
            else:
                indice = min(gerais2Vez)
            
            TChegada = filaPostoC2Vez[indice][1]
            TEsperaUtente = clock - TChegada
            TAPostoC = filaPostoC2Vez[indice][3]
            TPPostoC = clock + TAPostoC
            removerUtenteFilaPostoC2Vez(indice)
            TTEsperaPostoC = TTEsperaPostoC + TEsperaUtente
            TTOcupacaoPostoC = TTOcupacaoPostoC + TAPostoC
            if (clock >= 0 and clock <= 7200):
                TTOcupacaoPostoC0911 = TTOcupacaoPostoC0911 + TAPostoC
                TTEsperaPostoC0911 = TTEsperaPostoC0911 + TEsperaUtente
            elif (clock > 7200 and clock <= 14400):
                TTOcupacaoPostoC1113 = TTOcupacaoPostoC1113 + TAPostoC
                TTEsperaPostoC1113 = TTEsperaPostoC1113 + TEsperaUtente
            elif (clock > 14400 and clock <= 21600):
                TTOcupacaoPostoC1315 = TTOcupacaoPostoC1315 + TAPostoC
                TTEsperaPostoC1315 = TTEsperaPostoC1315 + TEsperaUtente
            else:
                TTOcupacaoPostoC1517 = TTOcupacaoPostoC1517 + TAPostoC
                TTEsperaPostoC1517 = TTEsperaPostoC1517 + TEsperaUtente
    else:
        if (filaPostoC2Vez == []):
            for item in filaPostoC:
                if item.__contains__("P"):
                    prioritarios.append(filaPostoC.index(item))
                    prioritariosExist = True
                else:
                    gerais.append(filaPostoC.index(item))
            
            if (prioritariosExist): 
                indice = min(prioritarios) 
            else:
                indice = min(gerais)
            
            TChegada = filaPostoC[indice][1]
            NUPostoC = NUPostoC + 1
            UtentesPostoC.append(filaPostoC[indice][0])
            TEsperaUtente = clock - TChegada
            TAPostoC = filaPostoC[indice][3]
            TPPostoC = clock + TAPostoC
            removerUtenteFilaPostoC(indice)
            TTEsperaPostoC = TTEsperaPostoC + TEsperaUtente
            TTOcupacaoPostoC = TTOcupacaoPostoC + TAPostoC
            if (clock >= 0 and clock <= 7200):
                TTOcupacaoPostoC0911 = TTOcupacaoPostoC0911 + TAPostoC
                TTEsperaPostoC0911 = TTEsperaPostoC0911 + TEsperaUtente
            elif (clock > 7200 and clock <= 14400):
                TTOcupacaoPostoC1113 = TTOcupacaoPostoC1113 + TAPostoC
                TTEsperaPostoC1113 = TTEsperaPostoC1113 + TEsperaUtente
            elif (clock > 14400 and clock <= 21600):
                TTOcupacaoPostoC1315 = TTOcupacaoPostoC1315 + TAPostoC
                TTEsperaPostoC1315 = TTEsperaPostoC1315 + TEsperaUtente
            else:
                TTOcupacaoPostoC1517 = TTOcupacaoPostoC1517 + TAPostoC
                TTEsperaPostoC1517 = TTEsperaPostoC1517 + TEsperaUtente
        else:
            for item in filaPostoC:
                if (item.__contains__("P")):
                    prioritarios.append(filaPostoC.index(item))
                    prioritariosExist = True
            
            if (prioritariosExist != True):
                for item in filaPostoC2Vez:
                    if (item.__contains__("P")):
                        prioritarios2Vez.append(filaPostoC2Vez.index(item))
                        prioritariosExist2Vez = True
                    else:
                        gerais2Vez.append(filaPostoC2Vez.index(item))
        
            if (prioritariosExist):
                indice = min(prioritarios)

                TChegada = filaPostoC[indice][1]
                NUPostoC = NUPostoC + 1
                UtentesPostoC.append(filaPostoC[indice][0])
                TEsperaUtente = clock - TChegada
                TAPostoC = filaPostoC[indice][3]
                TPPostoC = clock + TAPostoC
                removerUtenteFilaPostoC(indice)
                TTEsperaPostoC = TTEsperaPostoC + TEsperaUtente
                TTOcupacaoPostoC = TTOcupacaoPostoC + TAPostoC
                if (clock >= 0 and clock <= 7200):
                    TTOcupacaoPostoC0911 = TTOcupacaoPostoC0911 + TAPostoC
                    TTEsperaPostoC0911 = TTEsperaPostoC0911 + TEsperaUtente
                elif (clock > 7200 and clock <= 14400):
                    TTOcupacaoPostoC1113 = TTOcupacaoPostoC1113 + TAPostoC
                    TTEsperaPostoC1113 = TTEsperaPostoC1113 + TEsperaUtente
                elif (clock > 14400 and clock <= 21600):
                    TTOcupacaoPostoC1315 = TTOcupacaoPostoC1315 + TAPostoC
                    TTEsperaPostoC1315 = TTEsperaPostoC1315 + TEsperaUtente
                else:
                    TTOcupacaoPostoC1517 = TTOcupacaoPostoC1517 + TAPostoC
                    TTEsperaPostoC1517 = TTEsperaPostoC1517 + TEsperaUtente
            else:
                if (prioritariosExist2Vez):
                    indice = min(prioritarios2Vez)
                else:
                    indice = min(gerais2Vez)
                
                TChegada = filaPostoC2Vez[indice][1]
                TEsperaUtente = clock - TChegada
                TAPostoC = filaPostoC2Vez[indice][3]
                TPPostoC = clock + TAPostoC
                removerUtenteFilaPostoC2Vez(indice)
                TTEsperaPostoC = TTEsperaPostoC + TEsperaUtente
                TTOcupacaoPostoC = TTOcupacaoPostoC + TAPostoC
                if (clock >= 0 and clock <= 7200):
                    TTOcupacaoPostoC0911 = TTOcupacaoPostoC0911 + TAPostoC
                    TTEsperaPostoC0911 = TTEsperaPostoC0911 + TEsperaUtente
                elif (clock > 7200 and clock <= 14400):
                    TTOcupacaoPostoC1113 = TTOcupacaoPostoC1113 + TAPostoC
                    TTEsperaPostoC1113 = TTEsperaPostoC1113 + TEsperaUtente
                elif (clock > 14400 and clock <= 21600):
                    TTOcupacaoPostoC1315 = TTOcupacaoPostoC1315 + TAPostoC
                    TTEsperaPostoC1315 = TTEsperaPostoC1315 + TEsperaUtente
                else:
                    TTOcupacaoPostoC1517 = TTOcupacaoPostoC1517 + TAPostoC
                    TTEsperaPostoC1517 = TTEsperaPostoC1517 + TEsperaUtente
    
    if (utente3Fase != ''):
        for item in listaUtentes:
            if item.id.__contains__(utente3Fase):
                index = listaUtentes.index(item)

        if (listaUtentes[index].tatend3fase != 0):
            eventoChegadaTesouraria(index,clock)

#OBJETIVO: evento de chegada à Tesouraria
def eventoChegadaTesouraria(indexUtente,clock):
    #variáveis
    global ETesouraria
    global TUFTesouraria
    global TATesouraria
    global TPTesouraria
    global TTOcupacaoTesouraria
    global TTOcupacaoTesouraria0911
    global TTOcupacaoTesouraria1113
    global TTOcupacaoTesouraria1315
    global TTOcupacaoTesouraria1517
    global NUTesouraria
    global UtentesTesouraria

    if (ETesouraria == 1): #ocupado
        inserirUtenteFilaTesouraria(listaUtentes[indexUtente].id, clock, listaUtentes[indexUtente].tatend3fase)
        TUFTesouraria = TUFTesouraria + 1
    else:
        ETesouraria = 1 #ocupado
        NUTesouraria = NUTesouraria + 1
        UtentesTesouraria.append(listaUtentes[indexUtente].id)
        TATesouraria = listaUtentes[indexUtente].tatend3fase
        TPTesouraria = clock + TATesouraria
        TTOcupacaoTesouraria = TTOcupacaoTesouraria + TATesouraria
        if (clock >= 0 and clock <= 7200):
            TTOcupacaoTesouraria0911 = TTOcupacaoTesouraria0911 + TATesouraria
        elif (clock > 7200 and clock <= 14400):
            TTOcupacaoTesouraria1113 = TTOcupacaoTesouraria1113 + TATesouraria
        elif (clock > 14400 and clock <= 21600):
            TTOcupacaoTesouraria1315 = TTOcupacaoTesouraria1315 + TATesouraria
        else:
            TTOcupacaoTesouraria1517 = TTOcupacaoTesouraria1517 + TATesouraria

#OBJETIVO: evento de partida da Tesouraria
def eventoPartidaTesouraria(clock):
    #variáveis
    global ETesouraria
    global TPTesouraria
    global TATesouraria
    global TTEsperaTesouraria
    global TTEsperaTesouraria0911
    global TTEsperaTesouraria1113
    global TTEsperaTesouraria1315
    global TTEsperaTesouraria1517
    global TTOcupacaoTesouraria
    global TTOcupacaoTesouraria0911
    global TTOcupacaoTesouraria1113
    global TTOcupacaoTesouraria1315
    global TTOcupacaoTesouraria1517
    global NUTesouraria
    global UtentesTesouraria

    prioritarios = []
    gerais = []
    prioritariosExist = False

    utente2Fase2 = UtentesTesouraria[0]
    del UtentesTesouraria[0]

    if (filaTesouraria == []):
        ETesouraria = 0 #livre
        TPTesouraria = INFINITO
    else:
        for item in filaTesouraria:
            if item.__contains__("P"):
                prioritarios.append(filaTesouraria.index(item))
                prioritariosExist = True
            else:
                gerais.append(filaTesouraria.index(item))
        if (prioritariosExist): 
            indice = min(prioritarios) 
        else:
            indice = min(gerais)
        TChegada = filaTesouraria[indice][1]
        NUTesouraria = NUTesouraria + 1
        UtentesTesouraria.append(filaTesouraria[indice][0])
        TEsperaUtente = clock - TChegada
        TATesouraria = filaTesouraria[indice][3]
        TPTesouraria = clock + TATesouraria
        removerUtenteFilaTesouraria(indice)
        TTEsperaTesouraria = TTEsperaTesouraria + TEsperaUtente
        TTOcupacaoTesouraria = TTOcupacaoTesouraria + TATesouraria
        if (clock >= 0 and clock <= 7200):
            TTOcupacaoTesouraria0911 = TTOcupacaoTesouraria0911 + TATesouraria
            TTEsperaTesouraria0911 = TTEsperaTesouraria0911 + TEsperaUtente
        elif (clock > 7200 and clock <= 14400):
            TTOcupacaoTesouraria1113 = TTOcupacaoTesouraria1113 + TATesouraria
            TTEsperaTesouraria1113 = TTEsperaTesouraria1113 + TEsperaUtente
        elif (clock > 14400 and clock <= 21600):
            TTOcupacaoTesouraria1315 = TTOcupacaoTesouraria1315 + TATesouraria
            TTEsperaTesouraria1315 = TTEsperaTesouraria1315 + TEsperaUtente
        else:
            TTOcupacaoTesouraria1517 = TTOcupacaoTesouraria1517 + TATesouraria
            TTEsperaTesouraria1517 = TTEsperaTesouraria1517 + TEsperaUtente
    
    for item in listaUtentes:
        if item.id.__contains__(utente2Fase2):
            index = listaUtentes.index(item)
            tipoAssunto = listaUtentes[index].tipoassunto

    if (listaUtentes[index].tatend2fase2 != 0):
        if (tipoAssunto == 'A'):
            eventoChegadaPostoA(index,clock,2)
        elif (tipoAssunto == 'B'):
            eventoChegadaPostoB(index,clock,2)
        elif (tipoAssunto == 'C'):
            eventoChegadaPostoC(index,clock,2)

#///////////////////////////////////////////////////////////////////////////////////////////////////////////#

#////////////////////////////////////////////////// MAIN ///////////////////////////////////////////////////#
#Inicialização de variáveis
INFINITO = 999999999
filaTriagem = []
filaPostoA = []
filaPostoB = []
filaPostoC = []
filaTesouraria = []
clock = 0
NUtente = ''
ETriagem = 0 #livre
TUFTriagem = 0
TATriagem = 0
TPChegada = listaUtentes[0].tchegada
TPTriagem = INFINITO
NUSistema = 0
TTEsperaTriagem = 0
TTEsperaTriagem0911 = 0
TTEsperaTriagem1113 = 0
TTEsperaTriagem1315 = 0
TTEsperaTriagem1517 = 0
TTOcupacaoTriagem = 0
TTOcupacaoTriagem0911 = 0
TTOcupacaoTriagem1113 = 0
TTOcupacaoTriagem1315 = 0
TTOcupacaoTriagem1517 = 0
nUtentes = 0
terminar = 0
UtentesTriagem = []
EPostoA1 = 0 #livre
EPostoA2 = 0 #livre
TUFPostoA = 0
TAPostoA2 = 0
TPPostoA2 = INFINITO
TTOcupacaoPostoA2 = 0
TTOcupacaoPostoA20911 = 0
TTOcupacaoPostoA21113 = 0
TTOcupacaoPostoA21315 = 0
TTOcupacaoPostoA21517 = 0
TAPostoA1 = 0
TPPostoA1 = INFINITO
TTOcupacaoPostoA1 = 0
TTOcupacaoPostoA10911 = 0
TTOcupacaoPostoA11113 = 0
TTOcupacaoPostoA11315 = 0
TTOcupacaoPostoA11517 = 0
TTEsperaPostoA = 0
TTEsperaPostoA0911 = 0
TTEsperaPostoA1113 = 0
TTEsperaPostoA1315 = 0
TTEsperaPostoA1517 = 0
NUPostoA = 0
EPostoB1 = 0 #livre
EPostoB2 = 0 #livre
TUFPostoB = 0
TAPostoB2 = 0
TPPostoB2 = INFINITO
TTOcupacaoPostoB2 = 0
TTOcupacaoPostoB20911 = 0
TTOcupacaoPostoB21113 = 0
TTOcupacaoPostoB21315 = 0
TTOcupacaoPostoB21517 = 0
TAPostoB1 = 0
TPPostoB1 = INFINITO
TTOcupacaoPostoB1 = 0
TTOcupacaoPostoB10911 = 0
TTOcupacaoPostoB11113 = 0
TTOcupacaoPostoB11315 = 0
TTOcupacaoPostoB11517 = 0
NUPostoB = 0
TTEsperaPostoB = 0
TTEsperaPostoB0911 = 0
TTEsperaPostoB1113 = 0
TTEsperaPostoB1315 = 0
TTEsperaPostoB1517 = 0
EPostoC = 0 #livre
TUFPostoC = 0
TAPostoC = 0
TPPostoC = INFINITO
TTOcupacaoPostoC = 0
TTOcupacaoPostoC0911 = 0
TTOcupacaoPostoC1113 = 0
TTOcupacaoPostoC1315 = 0
TTOcupacaoPostoC1517 = 0
NUPostoC = 0
TTEsperaPostoC = 0
TTEsperaPostoC0911 = 0
TTEsperaPostoC1113 = 0
TTEsperaPostoC1315 = 0
TTEsperaPostoC1517 = 0
UtentesPostoC = []
UtentesPostoA1 = []
UtentesPostoA2 = []
UtentesPostoB1 = []
UtentesPostoB2 = []
TPTesouraria = INFINITO
ETesouraria = 0 #livre
TUFTesouraria = 0
TATesouraria = 0
TTOcupacaoTesouraria = 0
TTOcupacaoTesouraria0911 = 0
TTOcupacaoTesouraria1113 = 0
TTOcupacaoTesouraria1315 = 0
TTOcupacaoTesouraria1517 = 0
NUTesouraria = 0
UtentesTesouraria = []
TTEsperaTesouraria = 0
TTEsperaTesouraria0911 = 0
TTEsperaTesouraria1113 = 0
TTEsperaTesouraria1315 = 0
TTEsperaTesouraria1517 = 0
filaPostoC2Vez = []
filaPostoB2Vez = []
filaPostoA2Vez = []

while(True):
    getClockTipoEvento = gestaoTempo(TPChegada,TPTriagem,TPPostoA1,TPPostoA2,TPPostoB1,TPPostoB2,TPPostoC,TPTesouraria) #[0]-clock;[1]-tipoEvento

    if (getClockTipoEvento[1] == 0): #chegada
        nUtentes = nUtentes + 1
        eventoChegada(getClockTipoEvento[0],listaUtentes,nUtentes-1)
        if (nUtentes == len(listaUtentes)):
            TPChegada = INFINITO
    elif (getClockTipoEvento[1] == 1): #partida triagem
        eventoPartidaTriagem(getClockTipoEvento[0],listaUtentes)
    elif (getClockTipoEvento[1] == 2): #partida PostoA1
        eventoPartidaPostoA1(getClockTipoEvento[0])
    elif (getClockTipoEvento[1] == 3): #partida PostoA2
        eventoPartidaPostoA2(getClockTipoEvento[0])
    elif (getClockTipoEvento[1] == 4): #partida PostoB1
        eventoPartidaPostoB1(getClockTipoEvento[0])
    elif (getClockTipoEvento[1] == 5): #partida PostoB2
        eventoPartidaPostoB2(getClockTipoEvento[0])
    elif (getClockTipoEvento[1] == 6): #partida PostoC
        eventoPartidaPostoC(getClockTipoEvento[0])
    elif (getClockTipoEvento[1] == 7): #partida Tesouraria
        eventoPartidaTesouraria(getClockTipoEvento[0])
    else: #fim da simulação
        terminar = 1
        
    if (terminar == 1):
        break
#//////////////////////////////////////////////// END MAIN //////////////////////////////////////////////////#
    
# Print statistics
print('///////////// Serviço de Atendimento - FINANÇAS /////////////')
print('N.º Utentes Sistema: ',NUSistema)
print('Total Utentes Fila Triagem:',TUFTriagem)
print('Tempo Médio Espera Fila Triagem (h:mm:ss): ',str(datetime.timedelta(seconds=round(TTEsperaTriagem/NUSistema,0))))
print('Tempo Médio Espera Fila Triagem (09h-11h): ',str(datetime.timedelta(seconds=round(TTEsperaTriagem0911/NUSistema,0))))
print('Tempo Médio Espera Fila Triagem (11h-13h): ',str(datetime.timedelta(seconds=round(TTEsperaTriagem1113/NUSistema,0))))
print('Tempo Médio Espera Fila Triagem (13h-15h): ',str(datetime.timedelta(seconds=round(TTEsperaTriagem1315/NUSistema,0))))
print('Tempo Médio Espera Fila Triagem (15h-17h): ',str(datetime.timedelta(seconds=round(TTEsperaTriagem1517/NUSistema,0))))
print('Tempo Total Ocupação Posto Triagem: ',str(datetime.timedelta(seconds=TTOcupacaoTriagem)))
print('Tempo Total Ocupação Posto Triagem (09h-11h): ',str(datetime.timedelta(seconds=TTOcupacaoTriagem0911)))
print('Tempo Total Ocupação Posto Triagem (11h-13h): ',str(datetime.timedelta(seconds=TTOcupacaoTriagem1113)))
print('Tempo Total Ocupação Posto Triagem (13h-15h): ',str(datetime.timedelta(seconds=TTOcupacaoTriagem1315)))
print('Tempo Total Ocupação Posto Triagem (15h-17h): ',str(datetime.timedelta(seconds=TTOcupacaoTriagem1517)))
print('Total Utentes Posto A:',NUPostoA)
print('Total Utentes Fila Posto A:',TUFPostoA)
print('Tempo Médio Espera Fila Posto A:', str(datetime.timedelta(seconds=round(TTEsperaPostoA/NUPostoA,0))))
print('Tempo Médio Espera Fila Posto A (09h-11h): ',str(datetime.timedelta(seconds=round(TTEsperaPostoA0911/NUPostoA,0))))
print('Tempo Médio Espera Fila Posto A (11h-13h): ',str(datetime.timedelta(seconds=round(TTEsperaPostoA1113/NUPostoA,0))))
print('Tempo Médio Espera Fila Posto A (13h-15h): ',str(datetime.timedelta(seconds=round(TTEsperaPostoA1315/NUPostoA,0))))
print('Tempo Médio Espera Fila Posto A (15h-17h): ',str(datetime.timedelta(seconds=round(TTEsperaPostoA1517/NUPostoA,0))))
print('Tempo Total Ocupação Posto A1:', str(datetime.timedelta(seconds=TTOcupacaoPostoA1)))
print('Tempo Total Ocupação Posto A1 (09h-11h): ',str(datetime.timedelta(seconds=TTOcupacaoPostoA10911)))
print('Tempo Total Ocupação Posto A1 (11h-13h): ',str(datetime.timedelta(seconds=TTOcupacaoPostoA11113)))
print('Tempo Total Ocupação Posto A1 (13h-15h): ',str(datetime.timedelta(seconds=TTOcupacaoPostoA11315)))
print('Tempo Total Ocupação Posto A1 (15h-17h): ',str(datetime.timedelta(seconds=TTOcupacaoPostoA11517)))
print('Tempo Total Ocupação Posto A2:', str(datetime.timedelta(seconds=TTOcupacaoPostoA2)))
print('Tempo Total Ocupação Posto A2 (09h-11h): ',str(datetime.timedelta(seconds=TTOcupacaoPostoA20911)))
print('Tempo Total Ocupação Posto A2 (11h-13h): ',str(datetime.timedelta(seconds=TTOcupacaoPostoA21113)))
print('Tempo Total Ocupação Posto A2 (13h-15h): ',str(datetime.timedelta(seconds=TTOcupacaoPostoA21315)))
print('Tempo Total Ocupação Posto A2 (15h-17h): ',str(datetime.timedelta(seconds=TTOcupacaoPostoA21517)))
print('Total Utentes Posto B:',NUPostoB)
print('Total Utentes Fila Posto B:',TUFPostoB)
print('Tempo Médio Espera Fila Posto B:', str(datetime.timedelta(seconds=round(TTEsperaPostoB/NUPostoB,0))))
print('Tempo Médio Espera Fila Posto B (09h-11h): ',str(datetime.timedelta(seconds=round(TTEsperaPostoB0911/NUPostoB,0))))
print('Tempo Médio Espera Fila Posto B (11h-13h): ',str(datetime.timedelta(seconds=round(TTEsperaPostoB1113/NUPostoB,0))))
print('Tempo Médio Espera Fila Posto B (13h-15h): ',str(datetime.timedelta(seconds=round(TTEsperaPostoB1315/NUPostoB,0))))
print('Tempo Médio Espera Fila Posto B (15h-17h): ',str(datetime.timedelta(seconds=round(TTEsperaPostoB1517/NUPostoB,0))))
print('Tempo Total Ocupação Posto B1:', str(datetime.timedelta(seconds=TTOcupacaoPostoB1)))
print('Tempo Total Ocupação Posto B1 (09h-11h): ',str(datetime.timedelta(seconds=TTOcupacaoPostoB10911)))
print('Tempo Total Ocupação Posto B1 (11h-13h): ',str(datetime.timedelta(seconds=TTOcupacaoPostoB11113)))
print('Tempo Total Ocupação Posto B1 (13h-15h): ',str(datetime.timedelta(seconds=TTOcupacaoPostoB11315)))
print('Tempo Total Ocupação Posto B1 (15h-17h): ',str(datetime.timedelta(seconds=TTOcupacaoPostoB11517)))
print('Tempo Total Ocupação Posto B2:', str(datetime.timedelta(seconds=TTOcupacaoPostoB2)))
print('Tempo Total Ocupação Posto B2 (09h-11h): ',str(datetime.timedelta(seconds=TTOcupacaoPostoB20911)))
print('Tempo Total Ocupação Posto B2 (11h-13h): ',str(datetime.timedelta(seconds=TTOcupacaoPostoB21113)))
print('Tempo Total Ocupação Posto B2 (13h-15h): ',str(datetime.timedelta(seconds=TTOcupacaoPostoB21315)))
print('Tempo Total Ocupação Posto B2 (15h-17h): ',str(datetime.timedelta(seconds=TTOcupacaoPostoB21517)))
print('Total Utentes Posto C:',NUPostoC)
print('Total Utentes Fila Posto C:',TUFPostoC)
print('Tempo Médio Espera Fila Posto C:', str(datetime.timedelta(seconds=round(TTEsperaPostoC/NUPostoC,0))))
print('Tempo Médio Espera Fila Posto C (09h-11h): ',str(datetime.timedelta(seconds=round(TTEsperaPostoC0911/NUPostoC,0))))
print('Tempo Médio Espera Fila Posto C (11h-13h): ',str(datetime.timedelta(seconds=round(TTEsperaPostoC1113/NUPostoC,0))))
print('Tempo Médio Espera Fila Posto C (13h-15h): ',str(datetime.timedelta(seconds=round(TTEsperaPostoC1315/NUPostoC,0))))
print('Tempo Médio Espera Fila Posto C (15h-17h): ',str(datetime.timedelta(seconds=round(TTEsperaPostoC1517/NUPostoC,0))))
print('Tempo Total Ocupação Posto C:', str(datetime.timedelta(seconds=TTOcupacaoPostoC)))
print('Tempo Total Ocupação Posto C (09h-11h): ',str(datetime.timedelta(seconds=TTOcupacaoPostoC0911)))
print('Tempo Total Ocupação Posto C (11h-13h): ',str(datetime.timedelta(seconds=TTOcupacaoPostoC1113)))
print('Tempo Total Ocupação Posto C (13h-15h): ',str(datetime.timedelta(seconds=TTOcupacaoPostoC1315)))
print('Tempo Total Ocupação Posto C (15h-17h): ',str(datetime.timedelta(seconds=TTOcupacaoPostoC1517)))
print('Total Utentes Tesouraria:',NUTesouraria)
print('Total Utentes Fila Tesouraria:',TUFTesouraria)
print('Tempo Médio Espera Fila Tesouraria:', str(datetime.timedelta(seconds=round(TTEsperaTesouraria/NUTesouraria,0))))
print('Tempo Médio Espera Fila Tesouraria (09h-11h): ',str(datetime.timedelta(seconds=round(TTEsperaTesouraria0911/NUTesouraria,0))))
print('Tempo Médio Espera Fila Tesouraria (11h-13h): ',str(datetime.timedelta(seconds=round(TTEsperaTesouraria1113/NUTesouraria,0))))
print('Tempo Médio Espera Fila Tesouraria (13h-15h): ',str(datetime.timedelta(seconds=round(TTEsperaTesouraria1315/NUTesouraria,0))))
print('Tempo Médio Espera Fila Tesouraria (15h-17h): ',str(datetime.timedelta(seconds=round(TTEsperaTesouraria1517/NUTesouraria,0))))
print('Tempo Total Ocupação Tesouraria:', str(datetime.timedelta(seconds=TTOcupacaoTesouraria)))
print('Tempo Total Ocupação Tesouraria (09h-11h): ',str(datetime.timedelta(seconds=TTOcupacaoTesouraria0911)))
print('Tempo Total Ocupação Tesouraria (11h-13h): ',str(datetime.timedelta(seconds=TTOcupacaoTesouraria1113)))
print('Tempo Total Ocupação Tesouraria (13h-15h): ',str(datetime.timedelta(seconds=TTOcupacaoTesouraria1315)))
print('Tempo Total Ocupação Tesouraria (15h-17h): ',str(datetime.timedelta(seconds=TTOcupacaoTesouraria1517)))
print('/////////////////////////////////////////////////////////////')

# abrir o ficheiro p/ escrita (ficheiro de log que contém todas as variáveis do programa)
'''f = open("results.txt","a")

f.write('\n')
f.write('%s,' % NUSistema)
f.write('%s,' % TUFTriagem)
f.write('%s,' % round(TTEsperaTriagem/NUSistema,0))
f.write('%s,' % round(TTEsperaTriagem0911/NUSistema,0))
f.write('%s,' % round(TTEsperaTriagem1113/NUSistema,0))
f.write('%s,' % round(TTEsperaTriagem1315/NUSistema,0))
f.write('%s,' % round(TTEsperaTriagem1517/NUSistema,0))
f.write('%s,' % TTOcupacaoTriagem)
f.write('%s,' % TTOcupacaoTriagem0911)
f.write('%s,' % TTOcupacaoTriagem1113)
f.write('%s,' % TTOcupacaoTriagem1315)
f.write('%s,' % TTOcupacaoTriagem1517)
f.write('%s,' % NUPostoA)
f.write('%s,' % TUFPostoA)
f.write('%s,' % round(TTEsperaPostoA/NUPostoA,0))
f.write('%s,' % round(TTEsperaPostoA0911/NUPostoA,0))
f.write('%s,' % round(TTEsperaPostoA1113/NUPostoA,0))
f.write('%s,' % round(TTEsperaPostoA1315/NUPostoA,0))
f.write('%s,' % round(TTEsperaPostoA1517/NUPostoA,0))
f.write('%s,' % TTOcupacaoPostoA1)
f.write('%s,' % TTOcupacaoPostoA10911)
f.write('%s,' % TTOcupacaoPostoA11113)
f.write('%s,' % TTOcupacaoPostoA11315)
f.write('%s,' % TTOcupacaoPostoA11517)
f.write('%s,' % TTOcupacaoPostoA2)
f.write('%s,' % TTOcupacaoPostoA20911)
f.write('%s,' % TTOcupacaoPostoA21113)
f.write('%s,' % TTOcupacaoPostoA21315)
f.write('%s,' % TTOcupacaoPostoA21517)
f.write('%s,' % NUPostoB)
f.write('%s,' % TUFPostoB)
f.write('%s,' % round(TTEsperaPostoB/NUPostoB,0))
f.write('%s,' % round(TTEsperaPostoB0911/NUPostoB,0))
f.write('%s,' % round(TTEsperaPostoB1113/NUPostoB,0))
f.write('%s,' % round(TTEsperaPostoB1315/NUPostoB,0))
f.write('%s,' % round(TTEsperaPostoB1517/NUPostoB,0))
f.write('%s,' % TTOcupacaoPostoB1)
f.write('%s,' % TTOcupacaoPostoB10911)
f.write('%s,' % TTOcupacaoPostoB11113)
f.write('%s,' % TTOcupacaoPostoB11315)
f.write('%s,' % TTOcupacaoPostoB11517)
f.write('%s,' % TTOcupacaoPostoB2)
f.write('%s,' % TTOcupacaoPostoB20911)
f.write('%s,' % TTOcupacaoPostoB21113)
f.write('%s,' % TTOcupacaoPostoB21315)
f.write('%s,' % TTOcupacaoPostoB21517)
f.write('%s,' % NUPostoC)
f.write('%s,' % TUFPostoC)
f.write('%s,' % round(TTEsperaPostoC/NUPostoC,0))
f.write('%s,' % round(TTEsperaPostoC0911/NUPostoC,0))
f.write('%s,' % round(TTEsperaPostoC1113/NUPostoC,0))
f.write('%s,' % round(TTEsperaPostoC1315/NUPostoC,0))
f.write('%s,' % round(TTEsperaPostoC1517/NUPostoC,0))
f.write('%s,' % TTOcupacaoPostoC)
f.write('%s,' % TTOcupacaoPostoC0911)
f.write('%s,' % TTOcupacaoPostoC1113)
f.write('%s,' % TTOcupacaoPostoC1315)
f.write('%s,' % TTOcupacaoPostoC1517)
f.write('%s,' % NUTesouraria)
f.write('%s,' % TUFTesouraria)
f.write('%s,' % round(TTEsperaTesouraria/NUTesouraria,0))
f.write('%s,' % round(TTEsperaTesouraria0911/NUTesouraria,0))
f.write('%s,' % round(TTEsperaTesouraria1113/NUTesouraria,0))
f.write('%s,' % round(TTEsperaTesouraria1315/NUTesouraria,0))
f.write('%s,' % round(TTEsperaTesouraria1517/NUTesouraria,0))
f.write('%s,' % TTOcupacaoTesouraria)
f.write('%s,' % TTOcupacaoTesouraria0911)
f.write('%s,' % TTOcupacaoTesouraria1113)
f.write('%s,' % TTOcupacaoTesouraria1315)
f.write('%s' % TTOcupacaoTesouraria1517)'''