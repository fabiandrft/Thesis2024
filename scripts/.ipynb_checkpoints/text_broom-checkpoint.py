import re
from bs4 import BeautifulSoup

def text_broom(text):
    # Aggressively remove URLs
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    
    # Remove HTML tags
    text = BeautifulSoup(text, "html.parser").get_text()
    
    # Replace instances of multiple periods with a single period
    text = re.sub(r'\.{2,}', '.', text)
    
    # No longer removing non-letter/number/space/Umlaut characters or other punctuation
    # The step to explicitly remove unwanted characters is removed to retain punctuation
    #This should be applied to text_cleanwithpunct
    
    # Convert to lowercase to normalize case
    text = text.lower()
    
    return text