from fastapi import FastAPI, UploadFile, HTTPException
import pandas as pd
import json
from converter import flatten_json

app = FastAPI()

@app.post("/convert/")
async def convert_json_to_csv(file: UploadFile):
    try:
        # Leggi il file JSON in memoria
        content = await file.read()
        data = json.loads(content)

        # Se il dato è un dizionario, avvolgilo in una lista
        if isinstance(data, dict):
            data = [data]

        # Appiattisci i dati
        flattened_data = [flatten_json(item) for item in data]

        # Crea un DataFrame
        df = pd.DataFrame(flattened_data)

        # Salva il CSV come stringa
        csv_content = df.to_csv(index=False)

        return {"csv": csv_content}
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON file")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
