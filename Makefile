install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py

test:
	python3 -m pytest -vv --cov=main test_*.py

format:	
	black *.py 

all: install lint test format