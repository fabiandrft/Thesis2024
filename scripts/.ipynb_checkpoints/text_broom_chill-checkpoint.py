import re
from bs4 import BeautifulSoup

def text_broom_chill(text):
    # Aggressively remove URLs
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    
    # Remove HTML tags
    text = BeautifulSoup(text, "html.parser").get_text()
    
    # Replace instances of multiple periods with a single period
    text = re.sub(r'\.{2,}', '.', text)
    
    # Retain only English and German letters, numbers, spaces, German Umlaute, and punctuation
    # Note: \w matches any word character (equivalent to [a-zA-Z0-9_]), but we want to avoid "_",
    # so we use a-zA-Z0-9 along with explicit German Umlaute and common punctuation marks
    text = re.sub(r'[^\wäöüßÄÖÜ.,;:!?\'"()\[\]{}\-/@#$%^&+=*]', ' ', text)
    
    # Remove underscores (not included in the list of retained characters)
    text = text.replace('_', ' ')
    
    # Convert to lowercase to normalize case
    text = text.lower()
    
    return text
