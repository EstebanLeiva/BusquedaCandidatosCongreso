import pandas as pd
import modelo
def cargar_info(nombre, sheet):
    df=pd.read_excel(nombre, sheet_name=sheet)   
    return df

def cortarDF(inicio,final,df):
    df = df.iloc[inicio:final+1]
    return df

def obtenerLista_NombrePartido(df):
    lista = modelo.lista_NombrePartido2(df)
    return lista

def buscarUsernames(lista):
    lista_usernames = []
    for nombre in lista:
        print(nombre)
        username = modelo.identify_twitter(nombre)
        partido = nombre.split()[2]
        #check = modelo.revisarPartido(username, partido)
        lista_usernames.append(username)
        print(username)

        """"
        if check == True:
            lista_usernames.append(username)
        else:
            lista_usernames.append("NA")
    """

    return lista_usernames

