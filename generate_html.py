#!/usr/bin/env python3
"""
Generate index.html from lies.json
Run this whenever you update lies.json to regenerate the website
"""

import json
from datetime import datetime

# Read lies.json
with open('data/lies.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

lies = data['lies']
contradictions = data['contradictions']
scandals = data['scandals']

# Count stats
total_lies = len(lies)
total_contradictions = len(contradictions)
total_scandals = len(scandals)

# Generate lie cards HTML
lies_html = ""
for lie in lies:
    lies_html += f"""
        <div class="lie-card">
            <span class="category">{lie['category']}</span>
            <span class="date">{lie['date']}</span>
            <h3>{lie['title']}</h3>
            <div class="quote-text">{lie['quote']}</div>
            <div class="reality">
                {lie['reality']}
            </div>
        </div>
    """

# Generate contradiction cards
contradictions_html = ""
for contra in contradictions:
    parts = contra['title'].split(' vs. ')
    contradictions_html += f"""
        <div class="lie-card">
            <h3>🗣️ {parts[0]}</h3>
            <h3 style="color: #ff8888; margin-top: 20px;">VS</h3>
            <h3>{parts[1]}</h3>
            <div class="reality">
                {contra['explanation']}
            </div>
        </div>
    """

# Generate scandal cards
scandals_html = ""
for scandal in scandals:
    scandals_html += f"""
        <div class="lie-card">
            <h3>{scandal['title']}</h3>
            <div class="reality">
                {scandal['description']}
            </div>
        </div>
    """

# Full HTML template
html_template = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mentirómetro Flávio Bolsonaro</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: #0a0e27;
            color: #e0e6ed;
            line-height: 1.6;
        }}
        
        header {{
            background: linear-gradient(135deg, #1a1f3a 0%, #2d2e5f 100%);
            padding: 60px 20px;
            text-align: center;
            border-bottom: 3px solid #ff4444;
        }}
        
        header h1 {{
            font-size: 3em;
            margin-bottom: 10px;
            color: #ff4444;
        }}
        
        header .tagline {{
            font-size: 1.2em;
            color: #888;
            font-style: italic;
        }}
        
        .stats {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            margin: 40px auto;
            max-width: 900px;
            padding: 0 20px;
        }}
        
        .stat-box {{
            background: rgba(255, 68, 68, 0.1);
            border: 2px solid #ff4444;
            padding: 30px;
            border-radius: 8px;
            text-align: center;
        }}
        
        .stat-number {{
            font-size: 2.5em;
            font-weight: bold;
            color: #ff4444;
        }}
        
        .stat-label {{
            color: #888;
            margin-top: 10px;
            font-size: 0.9em;
        }}
        
        .quote {{
            background: rgba(100, 100, 150, 0.2);
            border-left: 4px solid #ff4444;
            padding: 20px;
            margin: 30px auto;
            max-width: 800px;
            font-size: 1.1em;
            font-style: italic;
            color: #ccc;
        }}
        
        .container {{
            max-width: 1000px;
            margin: 0 auto;
            padding: 40px 20px;
        }}
        
        .section-title {{
            font-size: 2em;
            margin-top: 50px;
            margin-bottom: 30px;
            color: #ff4444;
            border-bottom: 2px solid #ff4444;
            padding-bottom: 10px;
        }}
        
        .lie-card {{
            background: rgba(255, 68, 68, 0.05);
            border: 1px solid rgba(255, 68, 68, 0.3);
            padding: 30px;
            margin-bottom: 25px;
            border-radius: 8px;
            transition: all 0.3s ease;
        }}
        
        .lie-card:hover {{
            border-color: #ff4444;
            background: rgba(255, 68, 68, 0.1);
        }}
        
        .lie-card .category {{
            display: inline-block;
            background: #ff4444;
            color: white;
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 0.85em;
            font-weight: bold;
            margin-bottom: 15px;
        }}
        
        .lie-card .date {{
            color: #888;
            font-size: 0.9em;
            margin-left: 10px;
        }}
        
        .lie-card h3 {{
            font-size: 1.3em;
            margin: 15px 0;
            color: #fff;
        }}
        
        .lie-card .quote-text {{
            background: rgba(0, 0, 0, 0.3);
            border-left: 3px solid #ff4444;
            padding: 15px;
            margin: 15px 0;
            font-style: italic;
            color: #ccc;
        }}
        
        .lie-card .reality {{
            background: rgba(100, 200, 100, 0.1);
            border-left: 3px solid #66cc66;
            padding: 15px;
            margin-top: 15px;
            color: #ccc;
        }}
        
        .lie-card .reality::before {{
            content: "✓ REALIDADE: ";
            color: #66cc66;
            font-weight: bold;
        }}
        
        footer {{
            background: #1a1f3a;
            border-top: 2px solid #ff4444;
            padding: 30px;
            text-align: center;
            color: #888;
            margin-top: 60px;
        }}
        
        @media (max-width: 768px) {{
            header h1 {{
                font-size: 2em;
            }}
            
            .stats {{
                grid-template-columns: repeat(2, 1fr);
            }}
        }}
    </style>
</head>
<body>
    <header>
        <h1>🔥 Mentirómetro Flávio</h1>
        <p class="tagline">Fact-Check de Flávio Bolsonaro para a Presidência 2026</p>
        <p class="tagline" style="margin-top: 20px; font-size: 0.9em;">Candidato sabichão, fatos nem tanto</p>
    </header>
    
    <div class="stats">
        <div class="stat-box">
            <div class="stat-number">{total_lies}</div>
            <div class="stat-label">Mentiras Desmascaradas</div>
        </div>
        <div class="stat-box">
            <div class="stat-number">{total_contradictions}</div>
            <div class="stat-label">Contradições Flagrantes</div>
        </div>
        <div class="stat-box">
            <div class="stat-number">{total_scandals}</div>
            <div class="stat-label">Escândalos Documentados</div>
        </div>
        <div class="stat-box">
            <div class="stat-number">0</div>
            <div class="stat-label">Pedidos de Desculpa</div>
        </div>
    </div>
    
    <div class="quote">
        "Sou moderado, não sou como meu pai, vou salvar o Brasil com economia"
        — Flávio Bolsonaro, 2025
        <br><br>
        <em style="color: #888;">(Enquanto toca campanha "em nome do pai" e defende o mesmo que Bolsonaro defendia)</em>
    </div>
    
    <div class="container">
        <h2 class="section-title">🔥 Mentiras Desmascaradas</h2>
        {lies_html}
    </div>
    
    <div class="container">
        <h2 class="section-title">🔄 Contradições Flagrantes</h2>
        {contradictions_html}
    </div>
    
    <div class="container">
        <h2 class="section-title">💣 Escândalos</h2>
        {scandals_html}
    </div>
    
    <footer>
        <p><strong>Mentirómetro Flávio Bolsonaro</strong> — Fact-checking para cidadania informada 🇧🇷</p>
        <p style="margin-top: 15px; font-size: 0.9em;">Todas as informações aqui são baseadas em verificações de órgãos como IBGE, CAGED, Polígrafo e cobertura jornalística.</p>
        <p style="margin-top: 10px; font-size: 0.85em;">Atualizado: {datetime.now().strftime('%B %Y')}</p>
    </footer>
</body>
</html>"""

# Write to file
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print("✅ index.html gerado com sucesso!")
print(f"   - {total_lies} mentiras")
print(f"   - {total_contradictions} contradições")
print(f"   - {total_scandals} escândalos")
