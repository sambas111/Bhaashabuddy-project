import json, re, copy

BASE = 'lessons_structure_maithili.json'
base = json.load(open(BASE, 'r', encoding='utf-8'))

LANGS = {
    'odia': {
        'name': 'Odia',
        'script_name': 'Odia Script',
        'devanagari_replace': [
            ('Maithili', 'Odia'), ('मैथिली', 'ଓଡ଼ିଆ'),
            ('Devanagari', 'Odia Script'),
            ('देवनागरी', 'ଓଡ଼ିଆ ଲିପି'),
        ]
    },
    'dogri': {
        'name': 'Dogri',
        'script_name': 'Devanagari Script',
        'devanagari_replace': [
            ('Maithili', 'Dogri'), ('मैथिली', 'डोगरी'),
        ]
    },
    'sanskrit': {
        'name': 'Sanskrit',
        'script_name': 'Devanagari Script',
        'devanagari_replace': [
            ('Maithili', 'Sanskrit'), ('मैथिली', 'संस्कृत'),
        ]
    },
    'bodo': {
        'name': 'Bodo',
        'script_name': 'Devanagari Script',
        'devanagari_replace': [
            ('Maithili', 'Bodo'), ('मैथिली', 'बर\''),
        ]
    },
    'urdu': {
        'name': 'Urdu',
        'script_name': 'Urdu Script',
        'devanagari_replace': [
            ('Maithili', 'Urdu'), ('मैथिली', 'اردو'),
            ('Devanagari', 'Urdu Script'),
            ('देवनागरी', 'اردو رسم الخط'),
        ]
    },
    'konkani': {
        'name': 'Konkani',
        'script_name': 'Devanagari Script',
        'devanagari_replace': [
            ('Maithili', 'Konkani'), ('मैथिली', 'कोंकणी'),
        ]
    },
}

for lang_key, info in LANGS.items():
    # 1. Create lessons_structure
    text = json.dumps(base, ensure_ascii=False, indent=2)
    for old, new in info['devanagari_replace']:
        text = text.replace(old, new)
    struct = json.loads(text)
    out_struct = f'lessons_structure_{lang_key}.json'
    open(out_struct, 'w', encoding='utf-8').write(json.dumps(struct, ensure_ascii=False, indent=2) + '\n')
    print(f'Created {out_struct}')

    # 2. Create scaffold data JSON
    title_map = {}
    for ml in struct.get('majorLessons', []):
        for sub in ml.get('sublessons', []):
            cid = sub.get('chapterId')
            if cid:
                title_map[cid] = sub.get('title', f'Lesson {cid}')
    data_scaffold = []
    for i in range(501, 663):
        data_scaffold.append({
            "id": i,
            "url": title_map.get(i, f"Lesson {i}"),
            "blocks": []
        })
    out_data = f'data_{lang_key}.json'
    open(out_data, 'w', encoding='utf-8').write(json.dumps(data_scaffold, ensure_ascii=False, indent=2) + '\n')
    print(f'Created {out_data} with {len(data_scaffold)} lessons')

print('\nAll structure and scaffold files created!')
