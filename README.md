# Chocolate House Application

Welcome to the Chocolate House Application! This application allows you to manage seasonal chocolate flavors, track ingredient inventory, and collect customer feedback. It uses SQLite for data storage and Flask as the web framework.

## Features

- Add seasonal chocolate flavors
- Manage ingredients inventory
- Record customer feedback
- View existing flavors, ingredients, and feedback

## Technologies used:
- Flask: A micro web framework for Python.
- SQLite: A lightweight database engine for storing data.
- HTML/CSS: For building the frontend interface.

## Prerequisites

- [Docker](https://www.docker.com/get-started) installed on your machine
- Basic knowledge of command line interface

## Getting Started

Follow these steps to set up and run the application:


## Setup and Installation:
1. Clone the repository:
   git clone https://github.com/MKDechamma/Choco_house.git

2. Build the Docker Image:
   docker build -t chocohouse .

3. Run the Docker Container:
    docker run -it -p 5000:5000 chocohouse
    
4. Access the Application:
   Open your web browser and go to http://localhost:5000 to access the Chocolate House Application.



