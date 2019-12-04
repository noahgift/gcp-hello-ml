from flask import Flask
from flask import jsonify
from time import gmtime, strftime
import pandas as pd
import wikipedia
from textblob import TextBlob
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World December 4th!'

@app.route('/name/<value>')
def name(value):
    print(f"This value was passed into a URL: /name/{value}")
    if value == "bear":
        val = {"mammal": value}
    else:
        val = {"unknown": value}
    return jsonify(val)

@app.route('/time')
def time():
    my_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    print(f"This was the time I returned")
    my_time_dict = {"time": my_time}
    return jsonify(my_time_dict)

@app.route('/html')
def html():
    """Returns some custom HTML"""
    return """
    <title>This is a Hello World World Page</title>
    <p>Hello:  It is December 4th, 2019</p>
    <p><b>World</b></p>
    """
@app.route('/pandas')
def pandas_sugar():
    df = pd.read_csv("https://raw.githubusercontent.com/noahgift/sugar/master/data/education_sugar_cdc_2003.csv")
    return jsonify(df.to_dict())

def gcpnlp(text):
    """Uses the GCP NLP library to process text"""

    client = language.LanguageServiceClient()
    document = types.Document(
    content=text,
        type=enums.Document.Type.PLAIN_TEXT)
    entities = client.analyze_entities(document).entities
    return entities

@app.route('/wikipedia/<company>')
def wikipedia_route(company):
    result = wikipedia.summary(company, sentences=10)
    res = TextBlob(result)
    nlpres = gcpnlp(result)
    val = {"company": company, 
        "summary": result,
        "polarity": res.sentiment.polarity,
        "gcpnlp": str(nlpres)}
    return jsonify(val)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

