import pandas as pd
from dbfread import DBF

dbf_conuc:DBF = DBF('fonte/ucs.dbf')
tabela_01:str = "fonte/Tabela_de_resultado_02.xlsx"
df_ibge:pd.DataFrame = pd.read_excel(tabela_01)
df_conuc:pd.DataFrame = pd.DataFrame(iter(dbf_conuc))

print(df_ibge.iloc[5])
print(df_conuc)