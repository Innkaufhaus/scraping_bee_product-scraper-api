import os
import logging
from flask import Flask, request, jsonify, render_template
from utils.scraper import scrape_multiple_urls, convert_to_xml, ScraperException
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    """
    Handle scraping requests
    Expects JSON data with 'urls' key containing an array of URLs
    Returns XML data with scraped product information
    """
    try:
        data = request.get_json()
        
        if not data or 'urls' not in data:
            return jsonify({'error': 'No URLs provided'}), 400
            
        urls = data['urls']
        if not isinstance(urls, list):
            return jsonify({'error': 'URLs must be provided as an array'}), 400
            
        if not urls:
            return jsonify({'error': 'Empty URL list provided'}), 400

        # Log the scraping request
        logger.info(f"Scraping request received for {len(urls)} URLs")
        
        # Scrape the URLs
        products = scrape_multiple_urls(urls)
        
        # Convert results to XML
        xml_data = convert_to_xml(products)
        
        # Log successful scraping
        logger.info("Scraping completed successfully")
        
        # Return XML response
        return xml_data, 200, {'Content-Type': 'application/xml'}

    except ScraperException as e:
        logger.error(f"Scraping error: {str(e)}")
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    logger.error(f"Internal server error: {str(error)}")
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
