setup:
	# You may want to do this
	virtualenv --python $(which python3) ~/.hellovenv
	# afterward then source
	# source ~/.hellovenv/bin/activate

install:
	pip install -r requirements.txt

lint:
	pylint --disable=R,C main.py