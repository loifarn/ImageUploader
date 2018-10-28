from flask import Flask, render_template, request, flash
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from werkzeug.utils import secure_filename
from helper import get_extension, generate_filename, get_path, get_storage_filecount


app = Flask(__name__, static_url_path='/static/')
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


@app.route('/')
@app.route('/upload')
def index():
   return render_template('index.html')
	

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        file = request.files['file']
        original = file.filename
        ext = get_extension(file.filename)

        file.filename = generate_filename()

        file.save(get_path(secure_filename(file.filename)+ext))

        print(secure_filename(file.filename))
        flash('File: \'{}\' uploaded'.format(original))
        return render_template('index.html')


if __name__ == '__main__':
   app.run(debug = True)