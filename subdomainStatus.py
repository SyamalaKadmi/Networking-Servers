import requests
import time
from prettytable import PrettyTable
from urllib.parse import urlparse

# Common subdomains to check
common_subdomains = [
    "www", "mail", "blog", "shop", "api", "dev", "test", "secure"
]

def get_subdomains(base_url):
    """Generate full subdomain URLs based on the base URL."""
    parsed_url = urlparse(base_url)
    subdomains = [f"https://{sub}.{parsed_url.netloc}" for sub in common_subdomains]
    return subdomains

def check_status(url):
    """Check the status of the given URL."""
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

def display_status(base_url):
    """Display the status of subdomains in a table format."""
    subdomains = get_subdomains(base_url)
    table = PrettyTable()
    table.field_names = ["Subdomain", "Status"]

    for subdomain in subdomains:
        status = "Up" if check_status(subdomain) else "Down"
        table.add_row([subdomain, status])
    
    print(table)

def main():
    website = input("Enter the website (e.g., example.com): ")
    base_url = f"http://{website}"
    
    while True:
        print(f"\nChecking status of subdomains for {base_url}...\n")
        display_status(base_url)
        time.sleep(60)  # Wait for 1 minute before checking again

if __name__ == "__main__":
    main()
