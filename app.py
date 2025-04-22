from flask import Flask, request, jsonify
from readability import Document
import requests

app = Flask(__name__)

def extract_content(url):
    response = requests.get(url, timeout=10)
    doc = Document(response.text)
    return doc.summary()

@app.route('/extract', methods=['POST'])
def extract_content_endpoint():
    url = request.json.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    try:
        content = extract_content(url)
        return jsonify({'content': content})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
