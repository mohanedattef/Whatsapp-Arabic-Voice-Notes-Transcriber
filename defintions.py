import requests
from twilio.twiml.messaging_response import MessagingResponse
import io
from urllib.request import Request, urlopen
from pydub import AudioSegment
import json

def ExportAudio(url):
    req = Request(url=url, headers={'User-Agent': 'Mozilla/5.0'})
    file = urlopen(req).read()
    song = AudioSegment.from_file(io.BytesIO(file), format="ogg")
    song.export('voicenote.mp3')


def TranscripeAPI():
    headers = {'authorization': 'Bearer {token}'}
    tempFile=open('voicenote.mp3', 'rb')
    files = {'File': tempFile,'LanguageCode': (None, 'EG')}
    response = requests.post('https://px.kateb.ai:4040/api/recognize-file', headers=headers, files=files)
    output=json.loads(response.text)
    list=output['Text_String']
    transcript=[]
    i=0
    for entry in list:
        transcript.append(list[i]['text'])
        i+=1
    x=(' '.join(transcript))
    return x

