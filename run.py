from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)
 
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Say a caller's name, and play an MP3 for them."""
 
    resp = twilio.twiml.Response()
    # Greet the caller by name
    resp.say("Hello")
    # Play an MP3
    resp.play("http://attwoodthomas.bugs3.com/starwars.mp3")
 
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)

