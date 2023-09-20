.PHONY: deps build

build:
	pyinstaller -F src/main.py
