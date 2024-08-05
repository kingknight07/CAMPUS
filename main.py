from chatbot import generate_bot_response
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)




@app.route('/')
def dash():
    return render_template('dash.html')


@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')



@app.route('/chat_response')
def chat_response():
    message = "Sorry Unexpected Error"
    data = request.get_json()
    query = data.get('message')
    try:
      message = generate_bot_response(query)
    except Exception as e:
        print(str(e))


    return  message



if __name__ == '__main__':
    app.run(debug=True)
