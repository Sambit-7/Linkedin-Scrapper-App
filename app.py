from flask import Flask, render_template, request, send_file, jsonify, redirect, url_for
from scraper import scrape_profiles
import threading
import time

app = Flask(__name__)

progress = {"current": 0, "total": 0, "status": "idle", "file": None}

def update_progress(current, total):
    progress["current"] = current
    progress["total"] = total
    progress["status"] = "running"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    urls_text = request.form.get('urls')
    urls = [url.strip() for url in urls_text.splitlines() if url.strip()]

    progress.update({"current": 0, "total": len(urls), "status": "running", "file": None})

    def run_scraper():
        csv_path = scrape_profiles(urls, progress_callback=update_progress)
        progress["status"] = "done"
        progress["file"] = csv_path

    threading.Thread(target=run_scraper).start()
    return redirect(url_for('progress_page'))

@app.route('/progress')
def progress_page():
    return render_template('progress.html')

@app.route('/progress_status')
def progress_status():
    return jsonify(progress)

@app.route('/result')
def result():
    if progress["status"] == "done":
        return render_template('result.html')
    return redirect(url_for('progress_page'))

@app.route('/download')
def download():
    if progress["file"]:
        return send_file(progress["file"], as_attachment=True)
    return "File not ready yet."

if __name__ == '__main__':
    app.run(debug=True)
