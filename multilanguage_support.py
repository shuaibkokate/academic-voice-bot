# multilanguage_support.py
from googletrans import Translator

def translate(text, target_lang='en'):
    translator = Translator()
    try:
        translation = translator.translate(text, dest=target_lang)
        return translation.text
    except:
        return text  # fallback to original
