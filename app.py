from flask import Flask, request, jsonify, send_from_directory
from dotenv import load_dotenv
import os
from services.scraper import scrape_website
from services.analyzer import analyze_company
load_dotenv()

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    url = data.get('url')
    
    if not url:
        return jsonify({'error': 'URL manquante'}), 400
    
    # TODO: appeler les services

    scraped_data = scrape_website(url)
    # print(scraped_data)  # Affiche les données extraites dans la console pour le débogage
    analyzed_data = analyze_company(scraped_data)
    print(analyzed_data)  # Affiche les données analysées dans la console pour le
    return jsonify(analyzed_data)

if __name__ == '__main__':
    app.run(debug=True)