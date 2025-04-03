from dotenv import load_dotenv
import os

from fastapi import FastAPI, HTTPException, Query
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


load_dotenv()
engine = create_engine(os.getenv('DB_CONNECTION'))


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
app = FastAPI()

@app.get("/operadora/{cnpj}")
def getDetails(cnpj: str):
    try:
        with SessionLocal() as session:
            result = session.execute(text("SELECT (razao_social, nome_fantasia, modalidade, logradouro, numero, complemento, bairro, cidade, endereco_eletronico, representante) FROM public.operadoras_saude WHERE cnpj = :cnp"), {"cnpj":cnpj})
            operadora = [dict(row) for row in result.mappings()]
            return {"data": operadora}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("operadoras/modalidade/{modalidade}")
def getOperadorasModalidades(modalidade: str):
    try:
        with SessionLocal() as session:
            result = session.execute(text("SELECT (razao_social, nome_fantasia, modalidade, logradouro, numero, complemento, bairro, cidade, endereco_eletronico, representante) FROM public.operadoras_saude WHERE cnpj = :cnp"), {"cnpj":cnpj})
            operadora = [dict(row) for row in result.mappings()]
            return {"data": operadora}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# ....