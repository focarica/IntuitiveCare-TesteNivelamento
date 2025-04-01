from bs4 import BeautifulSoup
from urllib.parse import urljoin
from utils import zipFiles
import requests
import os

URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

class Scraper:
    def __init__(self):
        self.downloadsFolder = "Downloads"
        
        self.response = requests.get(URL)
        self.soup = BeautifulSoup(self.response.text, "html.parser")

    
    def donwloadFiles(self):
        paths = []
        
        if not os.path.exists(self.downloadsFolder):            
            os.mkdir(self.downloadsFolder)
                        
        if not os.path.isfile("Downloads/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"):
            for link in self.soup.find_all("a", attrs={"class":"internal-link"}):
                if(link.text in ["Anexo I.", "Anexo II."]):
                    filename = os.path.join(self.downloadsFolder, link['href'].split('/')[-1])
                    paths.append(filename)
                    
                    with open(filename, 'wb') as file:
                        file.write(requests.get(urljoin(URL, link['href'])).content)
        
            zipFiles(paths, "../RolsProcedimento.zip")        
            
    
Scraper().donwloadFiles()