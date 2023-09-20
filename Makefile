.PHONY: deps clean build

build:
	make clean
	python setup.py build
	pyinstaller -F src/main.py

clean:
	rm -rf build/*
