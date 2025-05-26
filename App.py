from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def parse_lines(filepath):
    accounts = []
    with open(filepath, 'r') as f:
        for line in f:
            if ':' in line:
                email_pass, *rest = line.strip().split(' | ')
                email, password = email_pass.split(':', 1)
                accounts.append({
                    'email': email,
                    'password': password,
                    'full': line.strip(),
                    'checked': False
                })
    return accounts

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            accounts = parse_lines(filepath)
            return render_template('results.html', accounts=accounts)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
  
