import requests
import time

# URL of your Netlify-deployed React app
app_url = 'https://quantotradetn.netlify.app/'

# Time interval between requests (in seconds)
interval = 5 * 60  # 5 minutes

while True:
    try:
        # Send a GET request to the app
        response = requests.get(app_url)
        if response.status_code == 200:
            print(f"Ping successful: {response.status_code}")
        else:
            print(f"Failed to ping: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")

    # Wait for the specified interval before the next request
    time.sleep(interval)
