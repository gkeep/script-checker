version=2024.7.0

deps:
	sudo apt install -y python3 python3-pip python3-virtualenv \
    	make build-essential libx11-xcb-dev libglu1-mesa-dev qtbase5-dev qt5-qmake libgl1-mesa-dri \
         qt6-base-dev qt6-wayland-dev qt6-wayland-dev-tools \
         libgtk-3-common libgtk-3-dev libgtk-4-common libgtk-4-dev libstdc++6

	python3 -m pip install -r requirements.txt

build_linux:
	pyinstaller --onefile src/main.py --name script_checker_$(version).bin

build_linux_docker: build_linux
	mv dist/script_checker_$(version).bin /app/builds