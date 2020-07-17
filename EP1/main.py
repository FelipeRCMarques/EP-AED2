import pandas as pd
import matplotlib.pyplot as pyplot
import time
from Local import Local

def ler_dados():
    dados = pd.read_csv ('./Enunciado/OD_2017.csv')

    # retorna um pandas DataFrame com somente as colunas que eu quero
    return dados[
        ['CO_DOM_X', 'CO_DOM_Y',
        'CO_ESC_X','CO_ESC_Y',
        'CO_TR1_X','CO_TR1_Y',
        'CO_TR2_X','CO_TR2_Y',
        'CO_O_X', 'CO_O_Y',
        'CO_D_X', 'CO_D_Y',
        'CO_T1_X', 'CO_T1_Y',
        'CO_T2_X', 'CO_T2_Y',
        'CO_T3_X', 'CO_T3_Y',
        'ID_PESS']
    ]

def colocarDicio(dicio: 'dict', x: 'int', y: 'int', id_pess: 'int'):
    # verifica primeiro se x ja foi inserido. 
    # Se nao, cria uma nova chave x com valores y e id_pess. Se sim, verifica se y ja foi inserido. Caso nao tenha sido inserido, a chave x, y ganha o valor id_pess. 
    # Se ja foi inserido, verifica se id_pess ja existe nessa chave x,y. Se ja existir, nao faz nada, caso contrario insere esse valor id_pess

    if x in dicio.keys():
        if y in dicio[x].keys():
            if id_pess not in dicio[x][y]: dicio[x][y].append(id_pess)
        else: dicio[x][y] = [id_pess]
    else: dicio[x] = {y: [id_pess]}

def executar():
    dicio = {}

    dados = ler_dados()

    for index, row in dados.iterrows():
        id_pess = row["ID_PESS"]

        # 0 é uma linha em branco, ou seja, sem coordenada. Se X é 0, logo, Y é 0 também
        if row["CO_DOM_X"] != 0: colocarDicio(dicio, row["CO_DOM_X"], row["CO_DOM_Y"], id_pess)

        if row["CO_ESC_X"] != 0: colocarDicio(dicio, row["CO_ESC_X"], row["CO_ESC_Y"], id_pess)

        if row["CO_TR1_X"] != 0: colocarDicio(dicio, row["CO_TR1_X"], row["CO_TR1_Y"], id_pess)

        if row["CO_TR2_X"] != 0: colocarDicio(dicio, row["CO_TR2_X"], row["CO_TR2_Y"], id_pess)

        if row["CO_O_X"] != 0: colocarDicio(dicio, row["CO_O_X"], row["CO_O_Y"], id_pess)

        if row["CO_D_X"] != 0: colocarDicio(dicio, row["CO_D_X"], row["CO_D_Y"], id_pess)

        if row["CO_T1_X"] != 0: colocarDicio(dicio, row["CO_T1_X"], row["CO_T1_Y"], id_pess)

        if row["CO_T2_X"] != 0: colocarDicio(dicio, row["CO_T2_X"], row["CO_T2_Y"], id_pess)

        if row["CO_T3_X"] != 0: colocarDicio(dicio, row["CO_T3_X"], row["CO_T3_Y"], id_pess)

    # array com todos os objetos Local
    objs_locais = []
    max_freq = 0

    # cria um objeto Local para cada local e atualiza qual o valor maximo de frequentadores para um unico local
    for x in dicio.keys():
        for y in dicio[x].keys():
            obj_local = Local(x, y, dicio[x][y])
            objs_locais.append(obj_local)

            if len(obj_local.getFrequentadores()) > max_freq:
                max_freq = len(obj_local.getFrequentadores())

    total_freq = []
    i = 0
    while i <= max_freq+1:
        x = 0
        total_freq.append(x)

        i += 1


    for obj_local in objs_locais:
        num_freq = len(obj_local.getFrequentadores())
        total_freq[num_freq] += 1

    print(total_freq)




if __name__ == "__main__":
    tempo_para_inicio = time.time()
    dados = ler_dados()

    executar()
    #print(dicio)


    #executar()
    print("Tempo de processamento: %s segundos" % (time.time() - tempo_para_inicio))