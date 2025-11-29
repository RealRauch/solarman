import json

# Read the config file
with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

# Update the URL
old_url = config.get('url', '')
new_url = 'globalapi.solarmanpv.com'

config['url'] = new_url

# Write back
with open('config.json', 'w', encoding='utf-8') as f:
    json.dump(config, f, indent=2, ensure_ascii=False)

print(f"✅ Updated URL in config.json")
print(f"   Old: {old_url}")
print(f"   New: {new_url}")
