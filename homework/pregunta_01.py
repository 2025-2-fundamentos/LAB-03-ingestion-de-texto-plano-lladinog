"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    import pandas as pd
    df = pd.read_fwf(
        "files/input/clusters_report.txt",
        widths=[9, 16, 16, 80],
        header=None,
        names=[
            "cluster", 
            "cantidad_de_palabras_clave", 
            "porcentaje_de_palabras_clave", 
            "principales_palabras_clave"
        ],
        skiprows=4 
    )

    col_agrupacion = ["cluster", "cantidad_de_palabras_clave", "porcentaje_de_palabras_clave"]
    df[col_agrupacion] = df[col_agrupacion].ffill()

    df = df.groupby(col_agrupacion)["principales_palabras_clave"].apply(lambda x: " ".join(x)).reset_index()

    df["principales_palabras_clave"] = df["principales_palabras_clave"].str.replace(r"\s+", " ", regex=True).str.strip()
    df["principales_palabras_clave"] = df["principales_palabras_clave"].str.replace(r"\.$", "", regex=True)

    df["cluster"] = df["cluster"].astype(int)
    df["cantidad_de_palabras_clave"] = df["cantidad_de_palabras_clave"].astype(int)
    
    df["porcentaje_de_palabras_clave"] = df["porcentaje_de_palabras_clave"].astype(str).str.replace("%", "").str.replace(",", ".").str.strip().astype(float)

    return df
