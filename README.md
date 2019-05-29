# gcp-hello-ml

## Hello World

1. Create Project

![create project](https://user-images.githubusercontent.com/58792/58592055-8430da00-821c-11e9-976e-f9c832532a08.png)

2.  Active cloud shell 

3.  Refer to [hello world docs for python3 app engine](https://cloud.google.com/appengine/docs/standard/python3/quickstart)

4.  Run describe

verify project is working
```bash
gcloud projects describe helloml-xxxx
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
gcloud config set project helloml-xxx
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

9.  create and source the virtual environment:

```bash
virtualenv venv
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

## Reference

* [Github Markdown Cheatsheet](https://guides.github.com/features/mastering-markdown/)
* [hello world python 3 docs](https://cloud.google.com/appengine/docs/standard/python3/quickstart)
michael was here
* [cloudshell quick start](https://cloud.google.com/shell/docs/quickstart)
* [how do I switch projects](https://stackoverflow.com/questions/46770900/how-to-change-the-project-in-gcp-using-cli-commands)
