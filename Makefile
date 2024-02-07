version=2024.2.0

build_linux:
	pyinstaller --onefile src/main.py --name script_checker_$(version).bin

build_linux_docker: build_linux
	mv dist/script_checker_$(version).bin /app/builds