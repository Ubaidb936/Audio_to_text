from flask import Flask, request
from audio_to_speech import upload, translate_data

app = Flask(__name__)


@app.route("/upload_video", methods=["POST"])
def upload_video():
    video_file = request.files["video"]
    lang = request.form.get("lang", "ES")
    res = upload(video_file)
    data = translate_data(res, lang)
    return {"data": data}, 200


if __name__ == "__main__":
    app.run()
