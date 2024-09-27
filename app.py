from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    strike_rate = None
    if request.method == 'POST':
        try:
            runs_scored = float(request.form['runs_scored'])
            balls_faced = float(request.form['balls_faced'])
            if balls_faced <= 0:
                raise ValueError("Balls faced must be greater than 0.")
            strike_rate = (runs_scored / balls_faced) * 100
        except ValueError:
            strike_rate = "Invalid input. Please enter valid numbers."

    return render_template('index.html', strike_rate=strike_rate)

if __name__ == '__main__':
    app.run(debug=True)
