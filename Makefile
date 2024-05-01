install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

install-azure:
	pip install --upgrade pip &&\
		pip install -r requirements-azure.txt

format:
	black *.py

lint:
	pylint --disable=R,C reverse_list.py

test:
	python -m pytest -vv --cov=reverse_list test_reverse_list.py

all: install lint test