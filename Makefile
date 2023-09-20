.PHONY: deps clean build

deps:
	sudo apt install python3-pip
	python3 -m pip install -r requirements.txt pyinstaller

build:
	make clean
	python setup.py build
	pyinstaller -F src/main.py

clean:
	rm -rf build/*
