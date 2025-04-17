# Product Scraper API

A Flask web application that integrates with ScrapingBee API to scrape product information from multiple URLs simultaneously. The application accepts multiple product URLs and returns structured XML data containing product details.

## Features

- Accepts multiple product URLs in a single request
- Integrates with ScrapingBee API for reliable web scraping
- Returns product information in XML format
- Modern web interface for URL submission
- Error handling and proper status code responses
- Deployment-ready for render.com

## Tech Stack

- Python
- Flask
- ScrapingBee API
- HTML/CSS (with Tailwind CSS)
- JavaScript (for AJAX requests)

## Setup and Installation

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables:
   - `SCRAPINGBEE_API_KEY`: Your ScrapingBee API key
4. Run the application: `python app.py`

## API Usage

### POST /scrape

Request body:
```json
{
    "urls": [
        "https://example.com/product1",
        "https://example.com/product2"
    ]
}
```

Response:
```json
{
    "results": [
        "<product><url>...</url><price>...</price><description>...</description></product>",
        "<product><url>...</url><price>...</price><description>...</description></product>"
    ]
}
```

## License

MIT License
