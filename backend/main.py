#uvicorn main:app
#uvicorn main:app --reload

#main imports
from fastapi import FastAPI, File, UploadFile, HTTPException 
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai 

#custom function imports



#initiate app
app = FastAPI()

#CORS -origins

origins =[
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:4174",
    "http://localhost:3000",
]


@app.get("/")
async def root():
    return {"message": "Hello World"}