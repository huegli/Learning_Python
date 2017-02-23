from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask (__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    entries = list(range(10))
    return render_template('first-bs.html', entries=entries)

@app.route('/history/<prev>')
def history(prev):
    if prev.isdigit():
        first_entry = int(prev)
    else:
        first_entry = 0
    entries = list(range(first_entry,first_entry+10))
    return render_template('first-bs.html', entries=entries)

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)
