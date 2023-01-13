from flask import Flask, render_template

app = Flask(__name__)

@app.route('/',methods=['GET',' POST'])

def homepage():
    return render_template('homepage.html')

@app.route('/curriculo')

def open_pdf():
    return render_template('pdf.html')

if __name__ == '__main__':
    app.run(debug=True)