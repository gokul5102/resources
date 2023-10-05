import requests
from bs4 import BeautifulSoup

def scrape_confluence(query):
    base_url = "https://your-confluence-url.com"
    search_url = f"{base_url}/wiki/search?text={query}"

    response = requests.get(search_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        resolution = soup.find('div', class_='resolution').text
        return resolution
    else:
        return "No resolution found."



import requests

def create_snow_ticket(description):
    snow_api_url = "https://your-servicenow-api-url.com/api/tickets"

    payload = {
        "description": description,
        "priority": "High",
        # Add more relevant fields here
    }

    headers = {
        "Authorization": "Bearer YourAccessToken",
        "Content-Type": "application/json"
    }

    response = requests.post(snow_api_url, json=payload, headers=headers)

    if response.status_code == 201:
        return "Ticket created successfully."
    else:
        return "Failed to create a ticket."
