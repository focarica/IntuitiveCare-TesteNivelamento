import pdfplumber
import pandas as pd
import csv

from utils import zipFiles
    
def transform():
    with pdfplumber.open("Downloads/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf") as pdf:
        tables = []
        
        for page in pdf.pages[2:]:
            extractedTable = page.extract_table()
            
            if extractedTable:
                if(len(tables) == 0):
                    tables.extend(extractedTable)
                else:
                    tables.extend(extractedTable[1:])
                
                
    df = pd.DataFrame(tables)
    df.replace(["", "", None], None, inplace=True)
    df.replace("OD", "Seg. Odontológica", inplace=True)
    df.replace("AMB", "Seg. Ambulatorial", inplace=True)
    
    df.to_csv("../tabelas.csv",
              index=False, 
              quoting=csv.QUOTE_ALL, 
              encoding="utf-8"
              )
    
    zipFiles(["../tabelas.csv"], "../Teste_Artur_Vinicius_Silva_Sousa.zip")

transform()