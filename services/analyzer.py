from groq import Groq
import os
import json
from dotenv import load_dotenv


load_dotenv()

def analyze_company(scraped_data):
    client = Groq(api_key=os.getenv('GROQ_API_KEY'))

    prompt = f"""
    Analyse ces données extraites du site web d'une entreprise et retourne un JSON structuré.

    Données brutes :
    - URL: {scraped_data['url']}
    - Titre: {scraped_data['title']}
    - Description: {scraped_data['description']}
    - Scripts chargés: {scraped_data['scripts']}
    - Liens sociaux: {scraped_data['social_links']}
    - Page pricing: {scraped_data['has_pricing']}
    - Page careers: {scraped_data['has_careers']}
    - Page blog: {scraped_data['has_blog']}

    Retourne UNIQUEMENT un JSON avec ces champs, sans texte autour, sans backticks :
    {{
        "company_name": "nom de l'entreprise",
        "description": "description courte en 1-2 phrases",
        "sector": "secteur d'activité",
        "business_model": "B2B / B2C / B2B2C",
        "estimated_size": "startup / scaleup / enterprise",
        "tech_stack": ["liste", "des", "techs", "détectées"],
        "gtm_signals": ["signaux", "go-to-market", "détectés"]
    }}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    response_text = response.choices[0].message.content
    return json.loads(response_text)