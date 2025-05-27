# main.py
from multilanguage_support import translate
from fallback_escalation import check_escalation
from google_calendar_integration import book_slot

def process_query(query, language='en'):
    print(f"Received query: {query} in {language}")
    
    # Translate to English
    english_query = translate(query, target_lang='en')
    
    # Example intent routing
    if "schedule" in english_query.lower():
        response = "Your next class is Data Structures on Monday at 10:00 AM."
    elif "book advisor" in english_query.lower():
        response = book_slot("S101")
    else:
        response = check_escalation(english_query)

    return translate(response, target_lang=language)
