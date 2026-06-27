start:
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt
	./venv/bin/python app.py

run:
	./venv/bin/python app.py

setup:
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt

.PHONY: start run setup