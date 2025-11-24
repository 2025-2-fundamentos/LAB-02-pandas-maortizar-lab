"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_10():
    import pandas as pd

    df = pd.read_csv("files/input/tbl0.tsv", sep="\t")

    # Agrupar por c1, ordenar c2 y unirlos con ':'
    salida = (
        df.groupby("c1")["c2"]
        .apply(lambda x: ":".join(str(v) for v in sorted(x.tolist())))
        .to_frame()
    )

    return salida
