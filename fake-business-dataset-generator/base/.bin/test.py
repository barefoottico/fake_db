from google.cloud import language_v1
from google.cloud.language_v1 import Document

def analyze_text(text):
    # Initialize the client
    client = language_v1.LanguageServiceClient()
    
    # Create a document
    document = Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    
    # Perform sentiment analysis
    sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment
    print(f"Sentiment: score={sentiment.score}, magnitude={sentiment.magnitude}")
    
    # Perform entity analysis
    entities = client.analyze_entities(request={'document': document}).entities
    for entity in entities:
        print(f"Entity: name={entity.name}, type={entity.type_}, salience={entity.salience}")

# Example text
text = "Google Cloud Natural Language API provides powerful tools for analyzing and understanding text."

analyze_text(text)

