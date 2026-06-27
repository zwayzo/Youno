from flask import Flask, request, jsonify, send_from_directory
from dotenv import load_dotenv
import os
from services.scraper import scrape_website
from services.analyzer import analyze_company
from services.scorer import score_company
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
    
   
    try:
        scraped_data = scrape_website(url)
        analyzed_data = analyze_company(scraped_data)
        print(analyzed_data)  # Affiche les données analysées dans la console pour le débogage
        scored_data = score_company({**analyzed_data, **scraped_data})
        print(scored_data)  # Affiche les données analysées dans la console pour le
        return jsonify({
            "company": analyzed_data,
            "score": scored_data
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)