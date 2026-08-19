import csv
import re
import os

def make_citekey(titulo, ano):
    first_word = titulo.split()[0] if titulo.split() else "unknown"
    clean = re.sub(r'[^a-zA-Z]', '', first_word).lower()
    return f"{clean}{ano}" if clean else f"ref{ano}"

def escape_bib(value):
    return value.replace('{', '\\{').replace('}', '\\}')

csv_path = os.path.join(os.path.dirname(__file__), '..', 'matriz_estado_arte_ia_generativa.csv')
bib_path = os.path.join(os.path.dirname(__file__), '..', 'content', 'referencias', 'biblioteca.bib')

os.makedirs(os.path.dirname(bib_path), exist_ok=True)

seen_keys = {}
entries = []

with open(csv_path, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        base_key = make_citekey(row['Titulo'], row['Ano'])
        citekey = base_key
        if citekey in seen_keys:
            seen_keys[base_key] += 1
            citekey = f"{base_key}{chr(96 + seen_keys[base_key])}"
        else:
            seen_keys[base_key] = 1

        doc_type = row.get('Tipo_documento', '').lower()
        bib_type = 'article' if 'revista' in doc_type or 'artículo' in doc_type else 'misc'

        entry = f"""@{bib_type}{{{citekey},
  title     = {{{escape_bib(row['Titulo'])}}},
  author    = {{{escape_bib(row['Autores'])}}},
  year      = {{{row['Ano']}}},
  note      = {{Relevancia: {row['Relevancia_TG']}. Contexto: {escape_bib(row['Pais_Contexto'])}}},
  url       = {{{row['URL']}}},
  keywords  = {{{escape_bib(row['Herramienta_IA'])}, {escape_bib(row['Enfoque_metodologico'])}}},
  annote    = {{{escape_bib(row['Hallazgos_clave'][:200] if row['Hallazgos_clave'] else '')}}}
}}"""
        entries.append(entry)

with open(bib_path, 'w', encoding='utf-8') as out:
    out.write('\n\n'.join(entries))

print(f"Exportadas {len(entries)} referencias → {bib_path}")
