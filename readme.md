# Docker-Vue-Django
This repo is a basic sample to use docker-compose with vue3 and django3.2


## Installation

* Firstly clone the project
    ```bash
    git clone https://github.com/ilyassari/dockervuedjango
    ```

* After clone the project; open terminal in base directory (the folder which contains *'docker-compose.yml'* )

Docker must be installed. See [docker](https://docs.docker.com/engine/install/) website to learn how installation be in your os.


* Rename *'sample.env.dev'* to *'.env.dev'*

* Create a new *SECRET_KEY*: [this website](https://djecrety.ir/) is recomended. paste new *SECRET_KEY* in the file named *'.env.dev'*


## Usage
* Be sure ports of localhost:8000 & localhost:8080 are available.

* To build docker images and containers:
    ```bash
    docker-compose up -d --build
    ```

* Superuser would be created. and some sample texts would be added. You can check with browser.  
  http://localhost:8000/ (You can log in with the superuser username and password specified in the .env.dev file.)  
  http://localhost:8080/