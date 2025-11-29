import re

# Read the file
with open('solarman.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the API paths
content = content.replace('"//account/v1.0/token', '"/account/v1.0/token')
content = content.replace('"//station/v1.0/realTime', '"/station/v1.0/realTime')  
content = content.replace('"//device/v1.0/currentData', '"/device/v1.0/currentData')

# Write back
with open('solarman.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Fixed API paths from // to /")
