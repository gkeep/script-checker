.PHONY: build

build:
	pyinstaller -F src/main.py -n script_checker
