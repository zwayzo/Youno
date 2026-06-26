import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    if not url.startswith('http'):
        url = 'https://' + url

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    response = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.title.string if soup.title else ''
    description = ''
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    if meta_desc:
        description = meta_desc.get('content', '')

    # Scripts chargés (pour détecter les techs)
    scripts = [s.get('src', '') for s in soup.find_all('script') if s.get('src')]

    # Liens sociaux
    links = [a.get('href', '') for a in soup.find_all('a', href=True)]
    social_links = [l for l in links if any(s in l for s in ['linkedin', 'twitter', 'github'])]

    # Pages importantes
    has_pricing = any('/pricing' in l for l in links)
    has_careers = any('/careers' in l or '/jobs' in l for l in links)
    has_blog = any('/blog' in l for l in links)

    return {
        'url': url,
        'title': title,
        'description': description,
        'scripts': scripts,
        'social_links': social_links,
        'has_pricing': has_pricing,
        'has_careers': has_careers,
        'has_blog': has_blog
    }