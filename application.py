from flask import Flask, request, render_template, redirect, url_for
from flask_uploads import UploadSet, configure_uploads, VIDEO
from video_processor import process_video

app = Flask(__name__)

# Configure upload set
videos = UploadSet('videos', VIDEO)
app.config['UPLOADED_VIDEOS_DEST'] = 'static/videos'  # Folder where videos will be stored
configure_uploads(app, videos)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'video' in request.files:
        filename = videos.save(request.files['video'])
        # Process video for anomaly detection here
        # For example, call your anomaly detection function
        return redirect(url_for('index'))
    return 'Error uploading file', 400

if __name__ == '__main__':
    app.run(debug=True)
