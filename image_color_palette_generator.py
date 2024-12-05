from flask import Flask, redirect, request, render_template, url_for
import os
from PIL import Image
import numpy as np
from collections import Counter
from flask_bootstrap import Bootstrap5
from werkzeug.utils import secure_filename

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'bmp', 'webp', 'svg'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)


def get_top_colors(image_path, top_n=10):
    img = Image.open(image_path).convert('RGB')
    img_array = np.array(img)
    pixels = img_array.reshape(-1, 3)
    color_counts = Counter(tuple(color) for color in pixels)
    most_common_colors = color_counts.most_common(top_n)

    return [(color, rgb_to_hex(color), count) for color, count in most_common_colors]


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        top_colors = get_top_colors(file_path)
        return render_template('results.html', image_path=file_path, colors=top_colors)
    return redirect(request.url)


if __name__ == '__main__':
    app.run(debug=True)
