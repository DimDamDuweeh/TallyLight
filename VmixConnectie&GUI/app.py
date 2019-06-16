# @Author Danja Verburg
# flask app met app.routes die worden verwerkt in GUI

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/tally/value')
def send_tally_value():
    print(tally_value)
    #checkt of data is binnen gekomen en stuurt door naar GUI.py
    if tally_value is None:
        print("No Value")
        return jsonify({'status': False})
    else:
        #stuurt door welke tally live is
        print("Value Send")
        return jsonify({'status': True, 'tally_value': tally_value})


@app.route('/tally=<tally>')
def tally(tally):
    global tally_value
    tally_value = tally
    print(tally_value)
    #stuurt door hoeveel tally's zijn aangesloten
    return jsonify({'slider': tally_value})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

