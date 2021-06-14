## General info
Simple script which analyses user text input about his workout(Nutritionix API). This api is using simple natural language processing technology to read your workout data from text input. When the data is processed it is saved in google sheet using google sheet api

## Technologies
Project is created with:
* Python 3.7
* Google sheet api
* Nutritionix API

## Setup
To make this projet working you need to create your google sheet api account, and change account credentials in script.

Then you should clone this repository:

```
$ git clone https://github.com/mateuszone/workout-tracking.git
$ cd  workout-tracking
```
To run the project you should have Python 3 installed on your computer. Then it's recommended to create a virtual environment for your projects dependencies. To install virtual environment:

pip install virtualenv

Then run the following command in the project directory:

virtualenv venv

That will create a new folder venv in your project directory. Next activate virtual environment:

```
$ source venv/bin/active
```
