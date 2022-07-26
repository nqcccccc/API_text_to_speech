from typing import Union
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from uuid import uuid4
from app.generate_voice import generate_voice

class Item(BaseModel):
    text: str
    silence: float
    sample_rate:int

app = FastAPI()

app.mount("/public/audio", StaticFiles(directory="app/assets/audio/"), name="public")

@app.post('/generate-voice')
async def nude_detect(item: Item):
    filename = 'clip_'+str(uuid4())+'.wav'
    if generate_voice(item.text,'app/assets/audio/'+filename,item.sample_rate,item.silence,'app/assets/infore/lexicon.txt') != None:
        return {'status':200,'path':'public/audio/'+filename}
    else:
        return {'status':500,'path':None}