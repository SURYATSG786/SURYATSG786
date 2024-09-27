from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length):
    characters = string.ascii_letters + string.digits 
    return ''.join(random.choice(characters) for i in range(length))

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ''
    if request.method == 'POST':
        try:
            length = int(request.form.get('length',))
            password = generate_password(length)
        except ValueError:
            password = 'Invalid length'
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
