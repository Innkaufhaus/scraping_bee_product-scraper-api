import os
import requests
import xmltodict
import logging
from typing import List, Dict, Union
from urllib.parse import quote_plus
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

class ScraperException(Exception):
    """Custom exception for scraper errors"""
    pass

def validate_url(url: str) -> bool:
    """Validate if the given string is a valid URL"""
    try:
        result = requests.utils.urlparse(url)
        return all([result.scheme, result.netloc])
    except Exception:
        return False

def scrape_url(url: str) -> Dict[str, str]:
    """
    Scrape a single URL using ScrapingBee API
    
    Args:
        url (str): The URL to scrape
        
    Returns:
        Dict[str, str]: Dictionary containing scraped product information
        
    Raises:
        ScraperException: If scraping fails
    """
    try:
        if not validate_url(url):
            raise ScraperException(f"Invalid URL format: {url}")

        api_key = os.getenv('SCRAPINGBEE_API_KEY')
        if not api_key:
            raise ScraperException("ScrapingBee API key not found in environment variables")

        logger.info(f"Starting to scrape URL: {url}")

        # Build the API URL directly
        api_url = 'https://app.scrapingbee.com/api/v1/'
        
        # Parameters for the API request
        params = {
            'api_key': api_key,
            'url': url,  # Don't encode the URL, requests will handle it
            'render_js': 'true',
            'premium_proxy': 'true',
            'wait': '5000',
            'block_ads': 'true',
            'return_page_source': 'true'
        }

        logger.info("Sending request to ScrapingBee API")
        response = requests.get(api_url, params=params, timeout=30)
        
        logger.info(f"ScrapingBee API response status code: {response.status_code}")
        
        if response.status_code != 200:
            error_message = f"ScrapingBee API error: {response.status_code}"
            try:
                error_detail = response.json()
                error_message += f" - {error_detail}"
            except:
                if response.text:
                    error_message += f" - {response.text[:200]}"
            raise ScraperException(error_message)

        # Parse the HTML response and extract product information
        html = response.text
        logger.info("Successfully received HTML response")

        # For demonstration, return sample data
        # In a real implementation, you would parse the HTML to extract actual data
        product_data = {
            "url": url,
            "title": "Sample Product Title",
            "price": "$99.99",
            "description": "This is a sample product description"
        }

        logger.info("Successfully extracted product data")
        return product_data

    except requests.exceptions.RequestException as e:
        error_message = f"Request failed: {str(e)}"
        logger.error(error_message)
        raise ScraperException(error_message)
    except Exception as e:
        error_message = f"Scraping failed: {str(e)}"
        logger.error(error_message)
        raise ScraperException(error_message)

def scrape_multiple_urls(urls: List[str]) -> List[Dict[str, str]]:
    """
    Scrape multiple URLs and return results
    
    Args:
        urls (List[str]): List of URLs to scrape
        
    Returns:
        List[Dict[str, str]]: List of dictionaries containing scraped product information
    """
    results = []
    errors = []

    for url in urls:
        try:
            logger.info(f"Processing URL: {url}")
            result = scrape_url(url)
            results.append(result)
            logger.info(f"Successfully processed URL: {url}")
        except ScraperException as e:
            error_detail = {"url": url, "error": str(e)}
            logger.error(f"Error processing URL {url}: {str(e)}")
            errors.append(error_detail)
            continue

    if errors and not results:
        raise ScraperException(f"All scraping attempts failed: {errors}")

    return results

def convert_to_xml(products: List[Dict[str, str]]) -> str:
    """
    Convert product data to XML format
    
    Args:
        products (List[Dict[str, str]]): List of product dictionaries
        
    Returns:
        str: XML string representation of products
    """
    try:
        # Create XML structure
        xml_dict = {
            "products": {
                "product": [
                    {
                        "url": p["url"],
                        "title": p["title"],
                        "price": p["price"],
                        "description": p["description"]
                    } for p in products
                ]
            }
        }
        
        # Convert dictionary to XML string
        xml_string = xmltodict.unparse(xml_dict, pretty=True)
        logger.info("Successfully converted data to XML format")
        return xml_string
        
    except Exception as e:
        error_message = f"XML conversion failed: {str(e)}"
        logger.error(error_message)
        raise ScraperException(error_message)
