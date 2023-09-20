.PHONY: clean build deps

build:
	make clean
	python setup.py build
	source venv/bin/activate
	pyinstaller -F src/main.py

clean:
	rm -rf build/*

deps:
	sudo apt install python3-virtualenv
	python3 -m virtualenv venv
	source venv/bin/activate
	python3 -m pip install -r requirements.txt pyinstaller