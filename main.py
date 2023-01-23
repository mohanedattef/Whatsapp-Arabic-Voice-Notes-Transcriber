from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import functions as func
from twilio.rest import Client

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    sender=request.values.get('From', '')
    incoming_msg =request.values.get('MediaUrl0', '')
    client = func.create_client()
    message = client.messages.create(
                     body="Audio Exported",
                     from_='whatsapp:+14155238886',
                     to=sender
                 )
    func.ExportAudio(incoming_msg)
    message = client.messages.create(
                     body="Transcriping began",
                     from_='whatsapp:+14155238886',
                     to=sender
                 )
    output=func.TranscribeAPI()
    message = client.messages.create(
                     body=output[0],
                     from_='whatsapp:+14155238886',
                     to=sender
                 )
    message = client.messages.create(
                     body="Accuracy is: "+str(output[1]),
                     from_='whatsapp:+14155238886',
                     to=sender
                 )
    resp = MessagingResponse()
    msg = resp.message()
    msg.body("done")
    return '', 204

if __name__ == '__main__':
    app.run(port=4000)

