import re

def sperator_fonk(text):
    sperator_r = re.sub(r'[^\w\s]', ' ', text).lower()
    sperator_r=' '.join(sperator_r.split())

    return sperator_r