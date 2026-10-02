import os
import re
import json

HTML_FILES = []
for root, dirs, files in os.walk('.'):
    if '.backup' in root or '.git' in root or '__pycache__' in root or 'components' in root:
        continue
    for f in files:
        if f.endswith('.html'):
            HTML_FILES.append(os.path.normpath(os.path.join(root, f)))

errors = []
warnings = []
stats = {
    'total_files': len(HTML_FILES),
    'indexable_pages': 0,
    'noindex_utility_pages': 0,
    'valid_h1': 0,
    'valid_json_ld': 0,
    'valid_canonical': 0,
    'valid_hreflang': 0,
    'valid_robots': 0,
    'valid_og': 0,
    'valid_twitter': 0
}

for fpath in HTML_FILES:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. H1 audit (all pages must have exactly 1 H1)
    h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', content, re.DOTALL)
    if len(h1s) != 1:
        errors.append(f"[{fpath}] Expected exactly 1 H1, found {len(h1s)}")
    else:
        stats['valid_h1'] += 1

    # 2. Robots meta audit
    robots = re.findall(r'<meta\s+name=[\"\']robots[\"\']\s+content=[\"\'](.*?)[\"\']', content)
    if len(robots) != 1:
        errors.append(f"[{fpath}] Missing or multiple robots meta")
        is_indexable = False
    else:
        stats['valid_robots'] += 1
        is_indexable = "index" in robots[0] and "noindex" not in robots[0]

    if is_indexable:
        stats['indexable_pages'] += 1
        
        # Canonical audit
        canon = re.findall(r'<link\s+rel=[\"\']canonical[\"\']\s+href=[\"\'](.*?)[\"\']', content)
        if len(canon) != 1:
            errors.append(f"[{fpath}] Missing or multiple canonical: {canon}")
        else:
            stats['valid_canonical'] += 1

        # Hreflang audit
        hreflangs = re.findall(r'<link\s+rel=[\"\']alternate[\"\']\s+hreflang=[\"\'](.*?)[\"\']\s+href=[\"\'](.*?)[\"\']', content)
        langs = [hl[0] for hl in hreflangs]
        if not all(k in langs for k in ['pt-PT', 'pt-BR', 'it-IT', 'x-default']):
            errors.append(f"[{fpath}] Incomplete hreflang set: {langs}")
        else:
            stats['valid_hreflang'] += 1

        # Open Graph & Twitter
        if 'og:title' in content and 'og:description' in content and 'og:image' in content and 'og:url' in content:
            stats['valid_og'] += 1
        else:
            warnings.append(f"[{fpath}] Missing some Open Graph tags")
            
        if 'twitter:card' in content and 'twitter:title' in content and 'twitter:image' in content:
            stats['valid_twitter'] += 1
        else:
            warnings.append(f"[{fpath}] Missing some Twitter card tags")

        # JSON-LD Structured Data
        ld_blocks = re.findall(r'<script\s+type=[\"\']application/ld\+json[\"\']>(.*?)</script>', content, re.DOTALL)
        if not ld_blocks:
            warnings.append(f"[{fpath}] No JSON-LD structured data block")
        else:
            valid_block = True
            for block in ld_blocks:
                try:
                    data = json.loads(block.strip())
                    if '@context' not in data:
                        errors.append(f"[{fpath}] JSON-LD missing @context")
                        valid_block = False
                except Exception as e:
                    errors.append(f"[{fpath}] Invalid JSON-LD syntax: {e}")
                    valid_block = False
            if valid_block:
                stats['valid_json_ld'] += 1

    else:
        stats['noindex_utility_pages'] += 1

    # Images alt audit
    imgs = re.findall(r'<img\s+([^>]*?)>', content)
    for img in imgs:
        if 'alt=' not in img:
            errors.append(f"[{fpath}] Image missing alt attribute: <img {img}>")

    # WhatsApp phone number consistency
    if fpath.startswith('br/') or '/br/' in fpath:
        if 'wa.me/393313882760' in content:
            errors.append(f"[{fpath}] Brazilian page has PT/IT phone number wa.me/393313882760")
    elif fpath.startswith('pt/') or fpath.startswith('it/') or '/pt/' in fpath or '/it/' in fpath:
        if 'wa.me/5544998018242' in content:
            errors.append(f"[{fpath}] PT/IT page has Brazilian phone number wa.me/5544998018242")

print("\n" + "="*50)
print("AUDIT RESULTS SUMMARY:")
print("="*50)
for k, v in stats.items():
    print(f"  {k}: {v}")

print(f"\nErrors: {len(errors)}")
for err in errors:
    print("  - ERROR:", err)

print(f"\nWarnings: {len(warnings)}")
for w in warnings:
    print("  - WARNING:", w)

if len(errors) == 0:
    print("\n>>> ALL PAGES PASSED COMPREHENSIVE SEO AUDIT WITH 0 ERRORS! <<<")
else:
    print(f"\n>>> AUDIT FAILED WITH {len(errors)} ERRORS <<<")
