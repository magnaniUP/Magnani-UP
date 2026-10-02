import os
import re

GTM_HEAD = """  <!-- Google Tag Manager -->
  <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
  new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
  j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
  'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
  })(window,document,'script','dataLayer','GTM-KDB6M7XW');</script>
  <!-- End Google Tag Manager -->"""

GTM_BODY = """  <!-- Google Tag Manager (noscript) -->
  <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-KDB6M7XW"
  height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
  <!-- End Google Tag Manager (noscript) -->"""

def inject_gtm(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip partial snippets
    if '<head>' not in content or '<body' not in content:
        return False, "Not a full HTML page"

    if 'GTM-KDB6M7XW' in content:
        return False, "GTM already present"

    # Inject in head after viewport meta or charset meta
    if '<meta name="viewport"' in content:
        content = re.sub(
            r'(<meta name="viewport"[^>]*>)',
            r'\1\n' + GTM_HEAD,
            content,
            count=1
        )
    elif '<meta charset="UTF-8">' in content:
        content = re.sub(
            r'(<meta charset="UTF-8">)',
            r'\1\n' + GTM_HEAD,
            content,
            count=1
        )
    else:
        content = re.sub(
            r'(<head[^>]*>)',
            r'\1\n' + GTM_HEAD,
            content,
            count=1
        )

    # Inject in body immediately after <body...>
    content = re.sub(
        r'(<body[^>]*>)',
        r'\1\n' + GTM_BODY,
        content,
        count=1
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return True, "GTM injected"

def main():
    target_files = []
    for root, dirs, files in os.walk('.'):
        if 'components' in root:
            continue
        for f in files:
            if f.endswith('.html'):
                target_files.append(os.path.normpath(os.path.join(root, f)))

    print(f"Auditing {len(target_files)} HTML files for GTM injection...")
    success_count = 0
    for path in sorted(target_files):
        success, msg = inject_gtm(path)
        if success:
            success_count += 1
            print(f"[OK] {path}: {msg}")
        else:
            print(f"[SKIP] {path}: {msg}")

    print(f"\nTotal pages updated with Google Tag Manager: {success_count}/{len(target_files)}")

if __name__ == '__main__':
    main()
