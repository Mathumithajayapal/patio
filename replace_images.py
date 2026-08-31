import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
images = [f"patio ({i}).jpg" for i in range(1, 15)]
img_count = len(images)
img_index = 0

def replacer(match):
    global img_index
    img_name = images[img_index % img_count]
    img_index += 1
    return match.group(1) + "images/" + img_name + match.group(3)

pattern = re.compile(r'(<img[^>]*?src=["\'])(https?://[^"\']+)(["\'][^>]*?>)', re.IGNORECASE)

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = pattern.sub(replacer, content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {file}")
