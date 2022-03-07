import controlador
import pandas as pd
import xlsxwriter

"""
df = controlador.cargar_info("20220131_candidatos-congreso_18012022.xlsx","Candidatos")
df = controlador.cortarDF(926, 2820, df)
lista = controlador.obtenerLista_NombrePartido(df)
lista_usernames = controlador.buscarUsernames(lista)

df2 = pd.DataFrame(lista_usernames)
writer = pd.ExcelWriter('test4.xlsx', engine='xlsxwriter')
df2.to_excel(writer, sheet_name='nombresCandidatos', index=False)
writer.save()
"""

"""
Juntemos los xlsx
"""

"""
df = controlador.cargar_info("20220131_candidatos-congreso_18012022.xlsx","Candidatos")
df2 = controlador.cargar_info("test4.xlsx","nombresCandidatos")
df = controlador.cortarDF(926, 1884, df)
df["Test1"] = df2["usernames"].str[1:]

print("A")

writer = pd.ExcelWriter('nuevocompleto.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='nombresCandidatos', index=False)
writer.save()
"""