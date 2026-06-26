async function analyze() {
    const url = document.getElementById('url-input').value.trim();
    if (!url) return;

    // Reset
    document.getElementById('results').classList.add('hidden');
    document.getElementById('error').classList.add('hidden');
    document.getElementById('loading').classList.remove('hidden');
    document.getElementById('analyze-btn').disabled = true;

    try {
        const response = await fetch('/api/analyze', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url })
        });

        const data = await response.json();

        if (data.error) {
            throw new Error(data.error);
        }

        // Remplir les données company
        document.getElementById('company-name').textContent = data.company.company_name;
        document.getElementById('company-description').textContent = data.company.description;
        document.getElementById('sector').textContent = data.company.sector;
        document.getElementById('business-model').textContent = data.company.business_model;
        document.getElementById('estimated-size').textContent = data.company.estimated_size;

        // Tech stack
        const techStack = document.getElementById('tech-stack');
        techStack.innerHTML = data.company.tech_stack
            .map(t => `<span class="tag tech">${t}</span>`)
            .join('');

        // GTM signals
        const gtmSignals = document.getElementById('gtm-signals');
        gtmSignals.innerHTML = data.company.gtm_signals
            .map(s => `<li>${s}</li>`)
            .join('');

        // Scoring
        document.getElementById('score-label').textContent = data.score.label;
        document.getElementById('score-value').textContent = `${data.score.score} / 100`;
        const scoreReasons = document.getElementById('score-reasons');
        scoreReasons.innerHTML = data.score.reasons
            .map(r => `<li>${r}</li>`)
            .join('');

        document.getElementById('results').classList.remove('hidden');

    } catch (err) {
        document.getElementById('error').textContent = `Erreur: ${err.message}`;
        document.getElementById('error').classList.remove('hidden');
    } finally {
        document.getElementById('loading').classList.add('hidden');
        document.getElementById('analyze-btn').disabled = false;
    }
}