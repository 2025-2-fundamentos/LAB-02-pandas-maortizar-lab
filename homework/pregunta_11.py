"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import pandas as pd

def pregunta_11():
    # Leer el archivo TSV
    df = pd.read_csv("files/input/tbl1.tsv", sep="\t")
    
    # Agrupar por 'c0' y unir los valores de 'c4' como una cadena separada por comas
    result = df.groupby('c0')['c4'].apply(lambda x: ','.join(sorted(x.unique()))).reset_index()
    
    return result
