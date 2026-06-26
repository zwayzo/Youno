def score_company(analyzed_data):
    score = 0
    reasons = []

    # Business model B2B
    if analyzed_data.get('business_model') == 'B2B':
        score += 30
        reasons.append('✅ Business model B2B')

    # Page pricing
    if analyzed_data.get('has_pricing'):
        score += 20
        reasons.append('✅ Page pricing présente')

    # Tech stack moderne
    modern_techs = ['react', 'next.js', 'vue', 'angular', 'typescript', 'django', 'flask', 'node.js', 'express', 'graphql', 'docker', 'kubernetes']
    tech_stack = [t.lower() for t in analyzed_data.get('tech_stack', [])]
    if any(t in tech_stack for t in modern_techs):
        score += 20
        reasons.append('✅ Tech stack moderne')

    # Page careers
    if analyzed_data.get('has_careers'):
        score += 15
        reasons.append('✅ Page careers présente (entreprise en croissance)')

    # Blog
    if analyzed_data.get('has_blog'):
        score += 10
        reasons.append('✅ Blog présent (maturité GTM)')

    # Taille
    if analyzed_data.get('estimated_size') in ['scaleup', 'enterprise']:
        score += 5
        reasons.append('✅ Taille suffisante')

    # Label final
    if score >= 80:
        label = '🟢 Excellent fit'
    elif score >= 50:
        label = '🟡 Bon fit'
    else:
        label = '🔴 Fit faible'

    return {
        'score': score,
        'label': label,
        'reasons': reasons
    }