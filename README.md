# 📖 Page Size Retriever

This script is designed to fetch the page sizes for a list of URLs and write the results to a CSV file.

## 🛠️ Dependencies

- `os`
- `requests`
- `csv`

## 📝 Description

### `get_page_size(url)`

This function takes a URL as an argument and returns the size of the page in bytes. If there's an error fetching the page, it will print an error message and return `None`.

### `main()`

This is the main function that:

1. Reads the URLs from the `urls.txt` file.
2. Retrieves the page sizes for each URL.
3. Writes the results to a `page_sizes.csv` file.

## 🚀 Usage

1. Make sure you have a file named `urls.txt` in the same directory, containing one URL per line.
2. Run the script:

bashCopy code

`python script_name.py`

3. The results will be saved in `page_sizes.csv` with the columns "URL" and "Size (bytes)".

## ⚠️ Notes

- If the script encounters an error while fetching a page size for a specific URL, it will print an error message and record 'N/A' for that URL in the CSV file.