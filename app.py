from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/ ', methods=['POST'])
def hello_world(value):
    btn1 = False

    if request.method == 'POST':
        if value == "0":
            btn1 = True


    if request.method == 'POST':
        if request.form['lamp'] == 'on':
            btn1 = True
        elif request.form['value'] == 'off':
            btn1 = False
    return render_template("UserInterface.html")


@app.route('/tallyAAN=<tallyAAN>')
def tallyAAN(tallyAAN):
    lengte = len(tallyAAN)
    lengte = lengte - 2
    print(lengte)
    return str(lengte)


@app.route('/tally=<tally>')
def tally(tally):
    tally1 = False
    tally2 = False
    tally3 = False

    if tally == "0":
        tally1 = True
        print("taart")
    elif tally == "1":
        tally2 = True
        print("taart is")
    elif tally == "2":
        tally3 = True
        print("taart is lekker")

        return render_template("index.html", tally1=tally1, tally2=tally2, tally3=tally3)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)