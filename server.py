from flask import Flask, render_template, request
from typograph import typograph


app = Flask(__name__)


@app.route('/typograph', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        source_text = request.form['text']
        result_text = typograph(request.form['text'])
    else:
        source_text = ''
        result_text = ''
    return render_template(
        'form.html',
        source_text=source_text,
        result_text=result_text
    )


if __name__ == "__main__":
    app.debug = True
    app.run()
