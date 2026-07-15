import os
import re

base_dir = r"e:\YMX Websile"
langs = ["vi", "en", "zh"]
embed_url = "https://www.google.com/maps?q=10.871586,106.944344&output=embed"

for lang in langs:
    filepath = os.path.join(base_dir, lang, "contact.html")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content = re.sub(r'src="https://www\.google\.com/maps\?q=[^"]+"', f'src="{embed_url}"', content)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Updated {filepath}")
