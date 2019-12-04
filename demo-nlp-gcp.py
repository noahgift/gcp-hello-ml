# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

result = "LeBron James plays for the Lakers"
client = language.LanguageServiceClient()
document = types.Document(
content=result,
        type=enums.Document.Type.PLAIN_TEXT)
entities = client.analyze_entities(document).entities
print(str(entities))
