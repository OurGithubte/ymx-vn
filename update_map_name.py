import os
import re

base_dir = r"e:\YMX Websile"
langs = ["vi", "en", "zh"]
# Using the exact company name for the search query in the embed map
embed_url = "https://www.google.com/maps?q=C%C3%94NG+TY+TNHH+ELECTRONIC+TECHNOLOGY+YMX+VI%E1%BB%86T+NAM&output=embed"

for lang in langs:
    filepath = os.path.join(base_dir, lang, "contact.html")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replacing the previous coordinates embed with the company name embed
    new_content = re.sub(r'src="https://www\.google\.com/maps\?q=[^"]+"', f'src="{embed_url}"', content)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Updated {filepath}")
