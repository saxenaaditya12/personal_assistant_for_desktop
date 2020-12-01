from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

# def start():
app = Flask(__name__)

@app.route("/")
def hello():
    return "harshit"

@app.route("/sms", methods=['POST'])
def sms_reply():
    msg = request.form.get('Body')
    print("\n\nClient >>>>", msg, end="\n")

    resp = MessagingResponse()
    reply = input("\nReply>>> ")

    resp.message(reply)
    print("sent :) ", end="\n")
    print("Waiting.......")

    return str(resp)

# if __name__ == "__main__":
#     app.run(debug=True)