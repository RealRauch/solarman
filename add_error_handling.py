import re

# Read the file
with open('solarman.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find and replace lines 64-66
new_lines = []
i = 0
while i < len(lines):
    if i == 63:  # Line 64 (0-indexed)
        # Replace the old token handling code with new improved version
        new_lines.append('        print(f"{time_stamp()}: 🔥 Token response received")\r\n')
        new_lines.append('        print(f"{time_stamp()}: 🔍 API Response: {json.dumps(data, indent=2)}")\r\n')
        new_lines.append('        \r\n')
        new_lines.append('        # Check if authentication was successful\r\n')
        new_lines.append('        if "success" in data and data["success"] == False:\r\n')
        new_lines.append('            print(f"{time_stamp()}: ❌ Authentication failed!")\r\n')
        new_lines.append('            print(f"{time_stamp()}: 📋 Error Code: {data.get(\'code\', \'unknown\')}")\r\n')
        new_lines.append('            print(f"{time_stamp()}: 📋 Error Message: {data.get(\'msg\', \'unknown\')}")\r\n')
        new_lines.append('            print(f"{time_stamp()}: 💡 Please check your credentials in config.json (username, password, appid, secret, orgId)")\r\n')
        new_lines.append('            return None\r\n')
        new_lines.append('        \r\n')
        new_lines.append('        # Extract access token\r\n')
        new_lines.append('        if "access_token" in data and data["access_token"] is not None:\r\n')
        new_lines.append('            return data["access_token"]\r\n')
        new_lines.append('        elif "data" in data and isinstance(data["data"], dict) and "access_token" in data["data"]:\r\n')
        new_lines.append('            return data["data"]["access_token"]\r\n')
        new_lines.append('        else:\r\n')
        new_lines.append('            print(f"{time_stamp()}: 😡 Token not found in response. Available keys: {list(data.keys())}")\r\n')
        new_lines.append('            return None\r\n')
        # Skip the original lines 64, 65, 66
        i += 3
    else:
        new_lines.append(lines[i])
        i += 1

# Write back
with open('solarman.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("✅ Added better error handling for authentication failures")
