from flask import Flask, request, render_template_string

app = Flask(__name__)

def validate_credit_card(card_number):
    def luhn_check(num):
        digits = [int(d) for d in str(num)]
        digits.reverse()
        total_sum = 0
        for i, digit in enumerate(digits):
            if i % 2 == 1:
                digit *= 2
                if digit > 9:
                    digit -= 9
            total_sum += digit
        return total_sum % 10 == 0
    return luhn_check(card_number)

@app.route('/', methods=['GET', 'POST'])
def index():
    status = ''
    card_number = ''
    if request.method == 'POST':
        card_number = request.form['card_number']
        is_valid = validate_credit_card(card_number)
        status = "valid" if is_valid else "invalid"
        return render_template_string('''
            <html>
            <head>
                <title>Credit Card Validation Result</title>
                <script>
                    window.onload = function() {
                        alert("Credit card number is {{ status }}.");
                    };
                </script>
            </head>
            <body>
                <h1>Credit Card Validation Result</h1>
                <p>Card Number: {{ card_number }}</p>
                <p>Status: {{ status | capitalize }}</p>
                <a href="/">Check another card</a>
            </body>
            </html>
        ''', card_number=card_number, status=status)
    
    return '''
        <html>
        <head>
            <title>Credit Card Validator</title>
        </head>
        <body>
            <h1>Credit Card Validator</h1>
            <form method="post">
                <label for="card_number">Enter Credit Card Number:</label>
                <input type="text" id="card_number" name="card_number" required>
                <button type="submit">Validate</button>
            </form>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
    
