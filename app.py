from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    if request.method == 'POST':
        try:
            weight = float(request.form['weight'])
            height = float(request.form['height'])
            if height > 0:
                bmi = weight / (height ** 2)
                bmi = round(bmi, 2)
            else:
                bmi = "Height must be greater than zero."
        except ValueError:
            bmi = "Invalid input. Please enter numerical values."
    
    return render_template('index.html', bmi=bmi)

if __name__ == '__main__':
    app.run(debug=True)

