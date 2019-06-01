# @Author Danja Verburg
# flask app met app.routes die worden verwerkt in GUI

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("test.html")


@app.route('/tallyAAN=<tallyAAN>')
def tallyAAN(tallyAAN):
    lengte = tallyAAN.split("\\")[0]
    print(len(lengte))
    return lengte


@app.route('/tally=<tally>')
def tally(tally):
    print(tally)
    if tally == "0":
        print("taart")
    elif tally == "1":
        print("taart is")
    elif tally == "2":
        print("taart is lekker")

    return render_template("test.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
