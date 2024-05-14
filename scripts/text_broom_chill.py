import re
from bs4 import BeautifulSoup

def text_broom_chill(text):
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = BeautifulSoup(text, "html.parser").get_text()
    text = re.sub(r'\.{2,}', '.', text)
    text = re.sub(r'[^\wäöüßÄÖÜ.,;:!?\'"()\[\]{}\-/@#$%^&+=*]', ' ', text)
    text = text.replace('_', ' ')
    text = text.lower()

    return text
