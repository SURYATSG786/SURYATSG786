from flask import Flask, render_template, request

app = Flask(__name__)

# Flat rate for simplicity
amount = 5.0  # ₹5.0 per unit

def calculate_bill(units):
    return units * amount

@app.route('/', methods=['GET', 'POST'])
def index():
    bill_amount = None
    if request.method == 'POST':
        try:
            units = int(request.form['units'])
            if units < 0:
                bill_amount = "Number of units cannot be negative."
            else:
                bill_amount = calculate_bill(units)
        except ValueError:
            bill_amount = "Please enter a valid number."
    # Ensure bill_amount is a string when passing to the template
    if isinstance(bill_amount, (int, float)):
        bill_amount = "{:.2f}".format(bill_amount)
    return render_template('index.html', bill_amount=bill_amount)

if __name__ == '__main__':
    app.run(debug=True)


