import pandas as pd
import matplotlib.pyplot as pyplot
import time
from Local import Local

def ler_dados():
    dados = pd.read_csv ('./Enunciado/OD_2017.csv')

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

def executar():
#use dict

if __name__ == "__main__":
    tempo_para_inicio = time.time()
    executar()
    print("Tempo de processamento: %s segundos" % (time.time() - tempo_para_inicio))