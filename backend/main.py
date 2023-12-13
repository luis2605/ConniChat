#uvicorn main:app
#uvicorn main:app --reload

#main imports
from fastapi import FastAPI, File, UploadFile, HTTPException 
from fastapi.responses import StreamingResponse

from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai

#custom function imports
from functions.openai_request import convert_audio_to_text

# Get Environment Vars
openai.organization = config("OPEN_AI_ORG")
openai.api_key = config("OPEN_AI_KEY")

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
#CORS-Middleware 

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

#check health
@app.get("/health")
async def check_health():
    return {"message": "healthy"}

#get audio 
@app.get("/post-audio_get/")
async def get_audio():
#get saved audio
    audio_input= open("luis_voice","rb")

#decode audio

    message_decode = convert_audio_to_text(audio_input)


    print(message_decode)

    return "done"

#post bot response
#note : not playing in browser when using post request 

# @app.post("/post-audio/")
# async def post_audio(file:UploadFile = File(...)):
#     print("hello")