import requests

blocklist_urls = [
    "https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_2_Base/filter.txt",
    "https://big.oisd.nl",
    "https://secure.fanboy.co.nz/fanboy-cookiemonster.txt",
    "https://easylist.to/easylist/easylist.txt"
    # Add your other blocklist URLs here
]

combined_blocklist = set()  # Use a set to avoid duplicates

for url in blocklist_urls:
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        for line in response.text.splitlines():
            line = line.strip()
            if line and not line.startswith("!"): #removes comments and empty lines.
                combined_blocklist.add(line)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")

with open("combined_blocklist.txt", "w") as f:
    for item in combined_blocklist:
        f.write(item + "\n")

print("Combined blocklist saved to combined_blocklist.txt")
