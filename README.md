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
pip -r requirements.txt
```

this should install flask

```
Flask==1.0.2
```

## Reference

* [Github Markdown Cheatsheet](https://guides.github.com/features/mastering-markdown/)
* [hello world python 3 docs](https://cloud.google.com/appengine/docs/standard/python3/quickstart)
michael was here
* [cloudshell quick start](https://cloud.google.com/shell/docs/quickstart)
* [how do I switch projects](https://stackoverflow.com/questions/46770900/how-to-change-the-project-in-gcp-using-cli-commands)
