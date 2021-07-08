# 20-21_viagdi

# CyberPeek

![Image text](https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/osint/catalog/static/images/CyberPeek.png)


# Project Description

CyberPeek is an analysis tool developed for allowing the management of information and evidence collected in an OSINT source analysis, on the different elements involved (individuals, societies, relationships, etc.), as well as the automatic representation of this information through visual models. 

The purpose of this tool would then be to facilitate the analysis of the information collected by showing, at all times, the existing relationships between the identified elements.

This tool allows analysts to work together, so that they can share specific studies of those entities/individuals they deem appropriate, adding comments between them in the same research.

# Features / Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install django and bootstrap libraries:

```bash
pip install django
```

```bash
pip install django-bootstrap
```

This second library is used to design css styles of the web interface.

# How to run

Firstly, create a virtual environment in some directory to which you want to clone the project:

```bash
python3 -m venv /path/to/new/virtual/environment
```

Then, install the requirements of the environment registered in requirements.txt

```bash
pip install -r requirements.txt
```

Now, clone the repository locally. Then, using some programming tool such as PyCharm, open a terminal propt. From directory 20-21_viagdi/osint/, run the following commands to set up the django models of the proyect:

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

Now, the project is ready tu use.

# Basic usage

To run the project, run the following command in a terminal promp with the last virtual environment installed, and from de directory 20-21_viagdi/osint/

```bash
python manage.py runserver 
```
Go to http://127.0.0.1:8000/ and you will be able to use the tool.


# Development documentation

# Architecture

This project has two python packages, osint and catalog. osint package is created by default by Django and contain the main python fields to develop a django project. catalog package all field related to the models of the project,
that are the information fields an analyst can fill, and all the fields related to the interface's design.

# Prepare development/execution environment
