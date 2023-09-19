.PHONY: clean build install-cfg run

build:
	make clean
	python setup.py build

run:
	build/exe.linux-x86_64-$$(pyenv local | cut -c -3)/script_checker

clean:
	rm -rf build/*