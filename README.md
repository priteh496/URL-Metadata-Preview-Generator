# URL Metadata Preview Generator

## Description
Fetches Open Graph, Twitter Card, and standard HTML meta tags from any URL — like what Slack or iMessage shows when you share a link.

## Features
- Extracts og:title, og:description, og:image, og:type
- Twitter Card metadata
- Author, keywords, canonical URL
- Batch URL processing
- JSON export

## Tech Stack
- Python 3.10+, requests, BeautifulSoup4

## Installation
```bash
pip install -r requirements.txt
```

## How to Run
```bash
python main.py https://github.com
python main.py https://example.com https://python.org -o results.json
```

## Example Output
```
🔗 Fetching: https://github.com
  Title         : GitHub
  Description   : GitHub is where over 100 million developers...
  Image         : https://github.githubassets.com/images/...
  Site Name     : GitHub
  Status        : 200
```
