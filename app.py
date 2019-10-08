import os
from flask import Flask, render_template, request, send_file, flash
from flask_uploads import UploadSet, configure_uploads, IMAGES
from mosaic import get_result_image

app = Flask(__name__)
photos = UploadSet('photos', IMAGES)
app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1
app.secret_key = "super secret key"
configure_uploads(app, photos)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    filename = photos.save(request.files['photo'])
    full_filename = os.path.join(app.config['UPLOADED_PHOTOS_DEST'], filename)
    return send_file(get_result_image(full_filename), as_attachment=True)

if __name__ == '__main__':
	app.run(debug=True)
    