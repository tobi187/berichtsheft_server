from flask import Flask, request, make_response
from services.edit_doc import fill_doc
from services.email_sender import send_mail
import os

app = Flask(__name__)


@app.route('/api/v1/word', methods=["GET", "POST"])  # type: ignore
def create_word():
    key_code = request.headers.get("API_KEY")

    if key_code != os.getenv("WORD_KEY_CODE"):
        return make_response("", 301)

    if request.method == "POST":
        data = request.get_json()
        word_doc = fill_doc(data)
        send_mail(data, word_doc)
        print("ready")
        return make_response("", 200)

    return make_response("", 201)


if __name__ == "__main__":
    app.run(debug=True)
