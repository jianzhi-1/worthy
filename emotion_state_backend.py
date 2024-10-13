from flask import Flask, request, jsonify
from openai import OpenAI
import json

app = Flask(__name__)
client = OpenAI(api_key="<API_KEY>")
state = "NORMAL"

@app.route("/getEmotion", methods=['GET'])
def getEmotion():
    resp = jsonify({
        "emotion": state
    })
    return resp

@app.route('/setEmotion', methods = ['POST'])
def setEmotion():

    data = request.json
    data = json.loads(request.data)
    app.logger.info(f"TRANSCRIPT: {data['transcript']}")
    if "transcript" not in data:
        # throw error
        pass
    resp = jsonify(success=True)
    resp.headers.add("Access-Control-Allow-Origin", "*")

    response = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[
            {
                "role": "system", 
                "content": "Given a text, you classify the emotion of the speaker into one of SHOCKED, THANKFUL, NORMAL, THINKING, DETERMINED. Only use the information give. Give only one of the above."
            },
            {
                "role": "user", 
                "content": data["transcript"] # TEXT
            }
        ]
    )

    global state
    state = response.choices[0].message.content
    if state not in ["SHOCKED", "THANKFUL", "NORMAL", "THINKING", "DETERMINED"]:
        state = "NORMAL"
    app.logger.info(f"NEW STATE: {state}")

    resp = jsonify({
        "emotion": state
    })

    return resp

@app.route('/demote', methods = ['GET'])
def demote():
    global state
    if state == 4: state = 3
    elif state == 2: state = 1
    elif state == 6: state = 5

    resp = jsonify(success=True)
    resp.headers.add("Access-Control-Allow-Origin", "*")
    return resp
     
if __name__ == '__main__':
    app.run(debug=True)
    