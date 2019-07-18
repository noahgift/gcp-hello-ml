# gcp-hello-ml

more stuff

## Hello World.

1. Create Project

![create project](https://user-images.githubusercontent.com/58792/58592055-8430da00-821c-11e9-976e-f9c832532a08.png)

2.  Activate cloud shell 

3.  Refer to [hello world docs for python3 app engine](https://cloud.google.com/appengine/docs/standard/python3/quickstart)

4.  Run describe

verify project is working
```bash
gcloud projects describe $GOOGLE_CLOUD_PROJECT
```
output of command:
```bash
createTime: '2019-05-29T21:21:10.187Z'
lifecycleState: ACTIVE
name: helloml
projectId: helloml-xxxxx
projectNumber: '881692383648'
```

5.  You may want to verify you have the correct project and if not, do this to switch:

```bash
gcloud config set project $GOOGLE_CLOUD_PROJECT
```

6.  Create app engine app:

```bash
gcloud app create 
```
this will ask for the region.  Go ahead and pick us-central [12]

```bash
Creating App Engine application in project [helloml-xxx] and region [us-central]....done.
Success! The app is now created. Please use `gcloud app deploy` to deploy your first app.
```
7.  Clone the hello world sample app repo:

```bash
git clone https://github.com/GoogleCloudPlatform/python-docs-samples
```

8.  cd into the repo:

```bash
cd python-docs-samples/appengine/standard_python37/hello_world
```

9.  Update Cloudshell image [NOTE this is optional....you don't need this]

```bash
git clone https://github.com/noahgift/gcp-hello-ml.git
# Update .cloudshellcustomimagerepo.json with project and image name
# TIP: enable "Boost Mode" in in Cloudshell
cloudshell env build-local
cloudshell env push
cloudshell env update-default-image
# Restart Cloudshell VM
```

10. create and source the virtual environment:

```bash
virtualenv --python $(which python) venv
source venv/bin/activate
```

double check it works:

```bash
which python
/home/noah_gift/python-docs-samples/appengine/standard_python37/hello_world/venv/bin/python
```

10.  activate cloud shell editor

![code editor](https://user-images.githubusercontent.com/58792/58593852-f60b2280-8220-11e9-850d-9858585be42e.png)

11.  install packages:

```bash
pip install -r requirements.txt
```

this should install flask

```
Flask==1.0.2
```

12.  run flask locally

this runs flask locally in gcp shell


```bash
python main.py
```

13.  preview 

![preview](https://user-images.githubusercontent.com/58792/58594280-fb1ca180-8221-11e9-8934-736b5ea05f1f.png)


14.  update main.py

```python

from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello I like to make AI Apps'

@app.route('/name/<value>')
def name(value):
    val = {"value": value}
    return jsonify(val)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
```

15.  Test out passing in parameters to exercise this function:

```python
@app.route('/name/<value>')
def name(value):
    val = {"value": value}
    return jsonify(val)
```
For example, calling this route will take the word lion and pass into the name function in flask:
```bash
https://8080-dot-3104625-dot-devshell.appspot.com/name/lion
```
returns value in web browser:
```python
{
value: "lion"
}
```
16.  Now deploy the app

```bash
gcloud app deploy
```

Warning first deploy could take about 10 minutes
FYI!!! you may also need to enable cloud build API.

```bash

Do you want to continue (Y/n)?  y
Beginning deployment of service [default]...
╔════════════════════════════════════════════════════════════╗
╠═ Uploading 934 files to Google Cloud Storage              ═╣

```


17.  Now stream the log files:

```bash
gcloud app logs tail -s default
```

18.  The production app is deployed and should like this:

```bash

Setting traffic split for service [default]...done.
Deployed service [default] to [https://helloml-xxx.appspot.com]
You can stream logs from the command line by running:
  $ gcloud app logs tail -s default

  $ gcloud app browse
(venv) noah_gift@cloudshell:~/python-docs-samples/appengine/standard_python37/hello_world (helloml-242121)$ gcloud app
 logs tail -s default
Waiting for new log entries...
2019-05-29 22:45:02 default[20190529t150420]  [2019-05-29 22:45:02 +0000] [8] [INFO] Starting gunicorn 19.9.0
2019-05-29 22:45:02 default[20190529t150420]  [2019-05-29 22:45:02 +0000] [8] [INFO] Listening at: http://0.0.0.0:8081
 (8)
2019-05-29 22:45:02 default[20190529t150420]  [2019-05-29 22:45:02 +0000] [8] [INFO] Using worker: threads
2019-05-29 22:45:02 default[20190529t150420]  [2019-05-29 22:45:02 +0000] [25] [INFO] Booting worker with pid: 25
2019-05-29 22:45:02 default[20190529t150420]  [2019-05-29 22:45:02 +0000] [27] [INFO] Booting worker with pid: 27
2019-05-29 22:45:04 default[20190529t150420]  "GET /favicon.ico HTTP/1.1" 404
2019-05-29 22:46:25 default[20190529t150420]  "GET /name/usf HTTP/1.1" 200
```

19.  Add a new route and test it out

```python
@app.route('/html')
def html():
    """Returns some custom HTML"""
    return """
    <title>This is a Hello World World Page</title>
    <p>Hello</p>
    <p><b>World</b></p>
    """
```

20.  Install pandas and return json results

At this point, you may want to consider creating a Makefile and do this:

```bash
touch Makefile
#this goes inside that file
install:
	pip install -r requirements.txt
```
you also may want to setup lint:

```
pylint --disable=R,C main.py
------------------------------------
Your code has been rated at 10.00/10

```

Route looks like this:

add pandas import at top:

```python
import pandas as pd
```

```python
@app.route('/pandas')
def pandas_sugar():
    df = pd.read_csv("https://raw.githubusercontent.com/noahgift/sugar/master/data/education_sugar_cdc_2003.csv")
    return jsonify(df.to_dict())

```

When you call the route ```https://<yourapp>.appspot.com/pandas```

you should get something like this:

![example out](https://user-images.githubusercontent.com/58792/58598673-2a3b0f00-8232-11e9-9621-9aa094511a46.png)

21.Add this wikipedia route

```python
import wikipedia
```

```python
@app.route('/wikipedia/<company>')
def wikipedia_route(company):
    result = wikipedia.summary(company, sentences=10)
    return result
````

22. Add NLP to app:

A.  https://github.com/noahgift/recommendations/blob/master/notebooks/NLP_GCP.ipynb
B.  Enable Cloud Natural Language API
C.  ```pip install google-cloud-language```


test it out in IPython

```python
In [1]: from google.cloud import language
   ...: from google.cloud.language import enums
   ...: 
   ...: from google.cloud.language import types
In [2]: 
In [2]: text = "LeBron James plays for the Cleveland Cavaliers."
   ...: client = language.LanguageServiceClient()
   ...: document = types.Document(
   ...:         content=text,
   ...:         type=enums.Document.Type.PLAIN_TEXT)
   ...: entities = client.analyze_entities(document).entities
In [3]: entities
```

##
End to End AI API Example

```python
from flask import Flask
from flask import jsonify
import pandas as pd
import wikipedia


app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello I like to make AI Apps'

@app.route('/name/<value>')
def name(value):
    val = {"value": value}
    return jsonify(val)

@app.route('/html')
def html():
    """Returns some custom HTML"""
    return """
    <title>This is a Hello World World Page</title>
    <p>Hello</p>
    <p><b>World</b></p>
    """
@app.route('/pandas')
def pandas_sugar():
    df = pd.read_csv("https://raw.githubusercontent.com/noahgift/sugar/master/data/education_sugar_cdc_2003.csv")
    return jsonify(df.to_dict())

@app.route('/wikipedia/<company>')
def wikipedia_route(company):

    # Imports the Google Cloud client library
    from google.cloud import language
    from google.cloud.language import enums
    from google.cloud.language import types
    result = wikipedia.summary(company, sentences=10)

    client = language.LanguageServiceClient()
    document = types.Document(
        content=result,
        type=enums.Document.Type.PLAIN_TEXT)
    entities = client.analyze_entities(document).entities
    return str(entities)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
```

## Reference

* [Github Markdown Cheatsheet](https://guides.github.com/features/mastering-markdown/)
* [hello world python 3 docs](https://cloud.google.com/appengine/docs/standard/python3/quickstart)
michael was here
* [cloudshell quick start](https://cloud.google.com/shell/docs/quickstart)
* [how do I switch projects](https://stackoverflow.com/questions/46770900/how-to-change-the-project-in-gcp-using-cli-commands)
* [more information about project setup](https://github.com/noahgift/myrepo)
* [nlp google](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/language)
* [nlp gcp](https://www.freecodecamp.org/news/how-to-make-your-own-sentiment-analyzer-using-python-and-googles-natural-language-api-9e91e1c493e/)

