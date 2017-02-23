from flask import Flask, render_template
app = Flask (__name__)

@app.route('/')
def index():
    entries = list(range(10))
    return render_template('first.html', entries=entries)

if __name__ == '__main__':
    app.run(debug=True)
