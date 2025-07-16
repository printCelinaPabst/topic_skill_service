from flask import Flask

app = Flask(__name__) #flaskanwendung erstellt

@app.route('/')
def hello_world():
    return "Hello from Topic and Skill Services!"

if __name__ == "__main__":
    app.run(debug=True, port=5000)