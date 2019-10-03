import os
from flask import Flask, render_template, request, send_file
from flask_uploads import UploadSet, configure_uploads, IMAGES
from mosaic import create_mosaic

app = Flask(__name__)
photos = UploadSet('photos', IMAGES)
app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'
configure_uploads(app, photos)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        full_filename = os.path.join(app.config['UPLOADED_PHOTOS_DEST'], filename)
        return  render_template("image.html", filename=create_mosaic(full_filename))
    return render_template('index.html')
    

if __name__ == '__main__':
	app.run(debug=True)
    