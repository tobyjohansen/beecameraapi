import uuid
from typing import List, Dict

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/V1/camera/setup/")
async def camera_setup(user_id: str, hive_id: str, ipadress: str):
    camera_id = uuid.uuid4()

    # Return Json response
    return {"UserID": user_id, "hive_id": hive_id, "camera_id": camera_id}


@app.get("/V1/camera/status/")
async def camera_status(hive_id: str):
    # Return Json response
    return {"hive_id": "Hive_ID", "status": "responsive"}



# Mock data for demonstration
hive_data = [
    {"hive_id": "Hive_ID1", "mite_amount": 25},
    {"hive_id": "Hive_ID2", "mite_amount": 20},
    {"hive_id": "Hive_ID3", "mite_amount": 30}
]

class HiveData(BaseModel):
    hive_id: str
    mite_amount: int

@app.get("/V1/camera/healtstatus", response_model=List[HiveData])
async def camera_healtstatus(user_id: str):
    # Return Json response
    return hive_data


if __name__ == '__main__':
    uvicorn.run(app, port=8007, host="0.0.0.0")
