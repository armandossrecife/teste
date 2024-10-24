import requests
import json

MY_API_URL = "http://localhost:8000/user/me"
MY_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhcm1hbmRvQHVmcGkuZWR1LmJyIiwiZXhwIjoxNzI5NzkzNjY5fQ.yTwOH1cugnmqbzqvn7Sengy5bJ_EyqLfU1oknu3Klgo"

def get_user_info(token):
    url = MY_API_URL  
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        user_data = json.loads(response.text)
        return user_data
    else:
        print(f"Error fetching user data: {response.text}")
        return None

print("Teste do user/me")
user_info = get_user_info(token=MY_TOKEN)
print(user_info)
