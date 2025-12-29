import os
import re

# Directory containing HTML files
templates_dir = 'frontend/templates'

# Mapping of old links to new Flask routes
link_mappings = {
    r'href="index\.html"': 'href="/"',
    r'href="login\.html"': 'href="/login"',
    r'href="cadastro\.html"': 'href="/cadastro"',
    r'href="dashboard\.html"': 'href="/dashboard"',
    r'href="negocios\.html"': 'href="/negocios"',
    r'href="despesas\.html"': 'href="/despesas"',
    r'href="funcionarios\.html"': 'href="/funcionarios"',
    r'href="relatorios\.html"': 'href="/relatorios"',
    r'href="integracao\.html"': 'href="/integracao"',
    r'href="configuracoes\.html"': 'href="/configuracoes"',
    r'href="recuperar-senha\.html"': 'href="/recuperar-senha"',
    r"window\.location\.href = 'dashboard\.html'": "window.location.href = '/dashboard'",
    r"window\.location\.href = 'negocios\.html'": "window.location.href = '/negocios'",
    r"window\.location\.href = 'login\.html'": "window.location.href = '/login'",
    r"window\.location\.href = 'cadastro\.html'": "window.location.href = '/cadastro'",
}

def fix_links_in_file(filepath):
    """Fix all HTML and JavaScript links in a file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Apply all link replacements
    for old_pattern, new_value in link_mappings.items():
        content = re.sub(old_pattern, new_value, content)
    
    # Only write if changes were made
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Fixed links in: {filepath}")
        return True
    else:
        print(f"- No changes needed: {filepath}")
        return False

def main():
    """Process all HTML files in the templates directory"""
    print("Starting link replacement...\n")
    
    files_processed = 0
    files_changed = 0
    
    for filename in os.listdir(templates_dir):
        if filename.endswith('.html'):
            filepath = os.path.join(templates_dir, filename)
            files_processed += 1
            if fix_links_in_file(filepath):
                files_changed += 1
    
    print(f"\n{'='*50}")
    print(f"Summary:")
    print(f"Files processed: {files_processed}")
    print(f"Files changed: {files_changed}")
    print(f"{'='*50}")

if __name__ == '__main__':
    main()
