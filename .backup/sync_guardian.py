import time
import shutil
import os

WATCH_CONFIG = [
    ("index.html", ".backup/root_index.html", 30000, ["id=\"faq\"", "id=\"site-footer\"", "header-market-switch", "wa.me/393313882760"]),
    ("pt/index.html", ".backup/pt_index.html", 30000, ["id=\"faq\"", "id=\"site-footer\"", "header-market-switch", "wa.me/393313882760"]),
    ("br/index.html", ".backup/br_index.html", 30000, ["id=\"faq\"", "id=\"site-footer\"", "header-market-switch", "wa.me/5544998018242"]),
    ("it/index.html", ".backup/it_index.html", 30000, ["id=\"faq\"", "id=\"site-footer\"", "header-market-switch", "wa.me/393313882760"]),
    ("css/header.css", ".backup/header.css", 2000, [".header-market-switch", ".btn-cta"]),
    ("css/responsive.css", ".backup/responsive.css", 2000, [".header-market-switch"]),
    ("css/footer.css", ".backup/footer.css", 2000, [".site-footer", ".footer-container"]),
    ("css/cta.css", ".backup/cta.css", 2000, [".cta-section", ".cta-banner"]),
    ("css/faq.css", ".backup/faq.css", 2000, [".faq-section", ".faq-item"]),
    ("js/faq.js", ".backup/faq.js", 1000, ["faq-section", "faq-item"]),
    ("js/main.js", ".backup/main.js", 500, ["WHATSAPP_CONTACTS"]),
    ("css/hero.css", ".backup/hero.css", 3000, ["hero"]),
    ("css/process.css", ".backup/process.css", 3000, ["process"]),
]

def check_file_healthy(path, min_size, required_strings):
    if not os.path.exists(path):
        return False
    size = os.path.getsize(path)
    if size < min_size:
        return False
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            for req in required_strings:
                if req not in content:
                    return False
    except Exception:
        return False
    return True

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(os.path.join(base_dir, ".backup"), exist_ok=True)
    
    print("[sync_guardian] Active and watching project integrity with WhatsApp links...")
    while True:
        try:
            for rel_src, rel_bak, min_size, req_tokens in WATCH_CONFIG:
                src_path = os.path.join(base_dir, rel_src)
                bak_path = os.path.join(base_dir, rel_bak)

                src_healthy = check_file_healthy(src_path, min_size, req_tokens)
                bak_healthy = check_file_healthy(bak_path, min_size, req_tokens)

                if not src_healthy and bak_healthy:
                    print(f"[sync_guardian] Corruption or rollback detected in {rel_src}! Restoring from backup...")
                    shutil.copyfile(bak_path, src_path)
                elif src_healthy:
                    # Update backup if src is healthy and newer
                    if not bak_healthy or os.path.getmtime(src_path) > os.path.getmtime(bak_path) + 1:
                        shutil.copyfile(src_path, bak_path)
        except Exception as e:
            print(f"[sync_guardian] Error: {e}")
        time.sleep(1)

if __name__ == "__main__":
    main()
