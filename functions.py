import requests
from twilio.twiml.messaging_response import MessagingResponse
import io
from urllib.request import Request, urlopen
from pydub import AudioSegment
import json
import os
from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv()


def create_client():
    sid=os.environ.get("TWILIO_ACCOUNT_SID")
    authtoken=os.environ.get("TWILIO_AUTH_TOKEN")
    return Client(sid, authtoken)

def ExportAudio(url):
    req = Request(url=url, headers={'User-Agent': 'Mozilla/5.0'})
    file = urlopen(req).read()
    song = AudioSegment.from_file(io.BytesIO(file), format="ogg")
    song.export('voicenote.mp3')




def TranscribeAPI():
    token=os.environ.get("KATEB_TOKEN")
    headers = {'authorization': 'Bearer {}'.format(token)}
    tempFile=open('voicenote.mp3', 'rb')
    files = {'File': tempFile,'LanguageCode': (None, 'EG')}
    response = requests.post('https://px.kateb.ai:4040/api/recognize-file', headers=headers, files=files)
    output=json.loads(response.text)
    list=output['Text_String']
    transcript=[]
    confidence=0
    i=0
    for entry in list:
        transcript.append(list[i]['text'])
        percentage=(list[i]['confidence'])*100
        confidence+=percentage
        i+=1
    accuracy=(confidence/(i*100))*100
    sentence=(' '.join(transcript))
    return sentence,accuracy

