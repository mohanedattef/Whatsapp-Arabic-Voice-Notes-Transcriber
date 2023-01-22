from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import defintions as func
app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg =request.values.get('MediaUrl0', '')
    print("process started")
    func.ExportAudio(incoming_msg)
    print("transcriping began")
    output=func.TranscripeAPI()
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(output)
    print(output)
    return str(resp)

if __name__ == '__main__':
    app.run(port=4000)

