import requests

# API bazasi URL'ni o'rnating
base_url = "https://dash.testvpn.pro/api/users/"
api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0IiwiYWNjZXNzIjoic3VkbyIsImlhdCI6MTczMDEyNDkwOCwiZXhwIjoxNzMwMjExMzA4fQ.-bn9cdQcUSfgDgPeWBDYdDSXxe52nYR0M549SwfAi-w"  # Sizning API kalitingizni bu yerga kiriting

# Headers'ni sozlang
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# VPN foydalanuvchilar ro'yxatini olish uchun funksiya
def get_vpn_users():
    url = f"https://dash.testvpn.pro/api/users"  # Foydalanuvchilar ro'yxati endpointi
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        users = response.json()  # JSON formatida foydalanuvchilar ro'yxati
        return users
    else:
        print("Foydalanuvchilarni olishda xato:", response.status_code)
        return None

# Foydalanuvchilar ro'yxatini olish va chop etish
vpn_users = get_vpn_users()
if vpn_users:
    for user in vpn_users:
        print(f"Foydalanuvchi nomi: ")
