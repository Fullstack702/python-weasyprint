ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

DEPLOY_CHROMEDRIVER='https://chromedriver.storage.googleapis.com/78.0.3904.70/chromedriver_linux64.zip'
DEPLOY_ZIPFILE='$(ROOT_DIR)/build/deploy.zip'

ROBOTO_ZIPFILE='$(ROOT_DIR)/resources/Roboto.zip'

LIBDIR=$(shell python -c 'from distutils.sysconfig import get_python_lib; print(get_python_lib())')
SRCDIR='$(ROOT_DIR)/src/'

clean:
	rm -rf build function.zip
	rm -rf __pycache__
	rm -rf bin

setup-roboto-font:
	mkdir -p $(HOME)/.fonts
	unzip $(ROBOTO_ZIPFILE) -d $(HOME)/.fonts
	rm $(HOME)/.fonts/LICENSE.txt

fetch-deploy-dependencies:
	mkdir -p bin/

	curl -sSL $(DEPLOY_CHROMEDRIVER) > chromedriver.zip
	unzip chromedriver.zip -d bin/

	rm chromedriver.zip

build-deploy-package: clean fetch-deploy-dependencies setup-roboto-font
	mkdir build

	cd $(SRCDIR) && zip -r9 $(DEPLOY_ZIPFILE) .

	zip -ur9 $(DEPLOY_ZIPFILE) bin/

	cp $(DEPLOY_ZIPFILE) .




