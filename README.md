# Product Scraper API

A Flask-based web application that uses ScrapingBee API to scrape product information from multiple URLs and return structured XML data. Features a modern, responsive UI built with Tailwind CSS.

## 🚀 Features

- 🌐 Scrape multiple product URLs simultaneously
- 📄 Return product data in structured XML format
- 🎨 Modern, responsive UI with Tailwind CSS
- ⚡ Real-time loading states and error handling
- 💾 Download results as XML file
- 📝 Detailed logging for debugging

## 🛠️ Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, Tailwind CSS, JavaScript
- **Scraping**: ScrapingBee API
- **Data Format**: XML
- **Styling**: Font Awesome, Google Fonts

## 📋 Prerequisites

- Python 3.8 or higher
- ScrapingBee API key ([Get one here](https://app.scrapingbee.com/))
- Git

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/product-scraper-api.git
cd product-scraper-api
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your ScrapingBee API key
nano .env  # or use your preferred text editor
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to:
```
http://localhost:8000
```

## 🔑 Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
SCRAPINGBEE_API_KEY=your_api_key_here
FLASK_ENV=development
FLASK_APP=app.py
```

## 🎯 Usage

1. Enter product URLs (one per line) in the text area
2. Click "Scrape Products"
3. View the formatted XML results
4. Download the results using the "Download XML" button

## 📝 API Endpoints

### POST /scrape

Accepts a JSON payload with URLs and returns product information in XML format.

**Request Body:**
```json
{
    "urls": [
        "https://example.com/product1",
        "https://example.com/product2"
    ]
}
```

**Response:**
```xml
<?xml version="1.0" encoding="utf-8"?>
<products>
    <product>
        <url>https://example.com/product1</url>
        <title>Product Title</title>
        <price>$99.99</price>
        <description>Product description</description>
    </product>
</products>
```

## 🚨 Error Handling

The API returns appropriate HTTP status codes:
- 400: Bad Request (invalid input)
- 401: Unauthorized (invalid API key)
- 500: Internal Server Error

## 🔍 Logging

The application logs important events and errors to help with debugging:
- Request information
- Scraping status
- API responses
- Error details

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [ScrapingBee](https://www.scrapingbee.com/) for their excellent web scraping API
- [Tailwind CSS](https://tailwindcss.com/) for the utility-first CSS framework
- [Font Awesome](https://fontawesome.com/) for the icons
- [Google Fonts](https://fonts.google.com/) for the typography

## 📞 Support

For support, email your-email@example.com or open an issue in the GitHub repository.
