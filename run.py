from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)
 
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Say a caller's name, and play an MP3 for them."""
    return """
    <?xml version="1.0" encoding="UTF-8"?>
    <Response>
        <Say>Hello Curious George</Say>
        <Play>http://demo.twilio.com/hellomonkey/monkey.mp3</Play>
    </Response>
    """
 
if __name__ == "__main__":
    app.run(debug=True)