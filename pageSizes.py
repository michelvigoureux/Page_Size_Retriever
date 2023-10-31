import os
import requests
import csv

def get_page_size(url):
    """Retrieve the page size for a given URL."""
    try:
        response = requests.get(url)
        return len(response.content)
    except:
        print(f"Error retrieving page size for {url}")
        return None

def main():
    # Read URLs from the urls.txt file
    with open("urls.txt", "r") as f:
        urls = [line.strip() for line in f.readlines()]

    # Get the page sizes for each URL
    page_sizes = []
    for url in urls:
        page_size = get_page_size(url)
        page_sizes.append(page_size)

    # Write the results to a CSV file
    with open("page_sizes.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["URL", "Size (bytes)"])
        for url, size in zip(urls, page_sizes):
            writer.writerow([url, size if size is not None else 'N/A'])

if __name__ == "__main__":
    main()
