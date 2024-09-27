from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_emi(principal, rate, term):
    monthly_rate = rate / 12 / 100
    num_payments = term * 12
    emi = principal * monthly_rate * (1 + monthly_rate) ** num_payments / ((1 + monthly_rate) ** num_payments - 1)
    return emi

@app.route('/', methods=['GET', 'POST'])
def index():
    emi = None
    if request.method == 'POST':
        principal = float(request.form['principal'])
        rate = float(request.form['rate'])
        term = int(request.form['term'])
        emi = calculate_emi(principal, rate, term)
    return render_template('index.html', emi=emi)

if __name__ == '__main__':
    app.run(debug=True)

