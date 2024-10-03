import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory, flash
from werkzeug.utils import secure_filename
from PIL import Image
import pyheif

UPLOAD_FOLDER = 'uploads'
CONVERTED_FOLDER = 'converted'
ALLOWED_EXTENSIONS = {'heif', 'heic'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CONVERTED_FOLDER'] = CONVERTED_FOLDER
app.secret_key = 'supersecretkey'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
if not os.path.exists(CONVERTED_FOLDER):
    os.makedirs(CONVERTED_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def heif_to_jpg(heif_path, jpg_path):
    heif_file = pyheif.read(heif_path)
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )
    image.save(jpg_path, "JPEG")

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'files' not in request.files:
            flash('No file part')
            return redirect(request.url)
        files = request.files.getlist('files')
        converted_files = []
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                heif_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(heif_path)
                jpg_filename = os.path.splitext(filename)[0] + '.jpg'
                jpg_path = os.path.join(app.config['CONVERTED_FOLDER'], jpg_filename)
                try:
                    heif_to_jpg(heif_path, jpg_path)
                    converted_files.append(jpg_filename)
                except Exception as e:
                    flash(f'Conversion failed for {filename}: {e}')
                    return redirect(request.url)
        flash('Files successfully converted')
        return redirect(url_for('show_converted_files', filenames=converted_files))
    return render_template('upload.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/converted/<filename>')
def converted_file(filename):
    return send_from_directory(app.config['CONVERTED_FOLDER'], filename)

@app.route('/converted_files')
def show_converted_files():
    filenames = request.args.getlist('filenames')
    return render_template('converted_files.html', filenames=filenames)

@app.route('/home/')
def home():
    return render_template('home.html')

@app.route('/admin_page/')
def home():
    return render_template('admin.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
