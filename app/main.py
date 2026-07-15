import os
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="DevOps Homework App", version="1.0.0")

# In-memory "adatbázis" a konfigurációk tárolására
in_memory_config = {}


# Pydantic modell a POST kérések validálására (ezt írja elő a feladat)
class ConfigItem(BaseModel):
    name: str
    value: str


# --- ALAP ENDPOINTOK ---

# GET /health
@app.get("/health", status_code=status.HTTP_200_OK)
def get_health():
    return {"status": "ok"}


# GET /version
@app.get("/version")
def get_version():
    version_value = os.getenv("APP_VERSION", "1.0.0")
    return {"version": version_value}


# GET /env
@app.get("/env")
def get_env():
    env_value = os.getenv("ENVIRONMENT", "development")
    return {"environment": env_value}


# --- KONFIGURÁCIÓS ENDPOINTOK (CRUD) ---

# POST /config
# Létrehozza vagy frissíti a konfigurációt
@app.post("/config", status_code=status.HTTP_200_OK)
def create_config(item: ConfigItem):
    in_memory_config[item.name] = item.value
    return {"name": item.name, "value": item.value}


# GET /config/{name}
# Lekéri az adott nevű konfigurációt
@app.get("/config/{name}")
def get_config(name: str):
    if name not in in_memory_config:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Config '{name}' not found"
        )
    return {"name": name, "value": in_memory_config[name]}


# DELETE /config/{name}
# Törli az adott konfigurációt
@app.delete("/config/{name}")
def delete_config(name: str):
    if name not in in_memory_config:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Config '{name}' not found"
        )
    del in_memory_config[name]
    return {"deleted": True}