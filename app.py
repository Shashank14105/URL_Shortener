from flask import Flask, render_template, request, redirect, url_for, abort

import storage
from shortener import is_valid_url, generate_short_code, normalize_url

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    all_urls = storage.load_all()
    # Show most recently added first
    items = list(all_urls.items())[::-1]
    return render_template("index.html", urls=items, error=None, short_url=None)


@app.route("/shorten", methods=["POST"])
def shorten():
    long_url = request.form.get("long_url", "")
    long_url = normalize_url(long_url)

    if not is_valid_url(long_url):
        all_urls = storage.load_all()
        items = list(all_urls.items())[::-1]
        error = (
            "Please enter a valid URL that starts with http:// or https:// "
            "(the field cannot be empty)."
        )
        return render_template("index.html", urls=items, error=error, short_url=None)

    existing_codes = storage.load_all().keys()
    short_code = generate_short_code(existing_codes)
    storage.add_url(short_code, long_url)

    short_url = url_for("redirect_to_original", code=short_code, _external=True)

    all_urls = storage.load_all()
    items = list(all_urls.items())[::-1]
    return render_template("index.html", urls=items, error=None, short_url=short_url)


@app.route("/<code>", methods=["GET"])
def redirect_to_original(code):
    record = storage.get_url(code)
    if record is None:
        abort(404)

    storage.increment_clicks(code)
    return redirect(record["original_url"])


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, port=5000)
