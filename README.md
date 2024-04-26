# Simple Agenda CRUD Django Project

## Overview
This Django project serves as a practical application for testing and understanding login, CRUD, form and authorization functionalities within the Django framework. I Developed it alongside instructional materials and documentation, the project focuses on implementing CRUD operations while integrating user authentication mechanisms.

## Features
- **CRUD Operations**: Users can create, read, update, and delete agenda items.
- **User Authentication**: Secure user authentication system using Django's built-in authentication, with a registration form and login screen.
- **Responsive Design**: The interface is designed to be responsive, allowing users to access the agenda from various devices.
- **Test Scripts**: I've also added a test script to fill the database with random information.

## Requirements
All the requirements and extensions can be found in the requirements.txt file. Python (3.x) should be instaled in your system.

## Installation
1. Clone the repository:
```
git clone https://github.com/yourusername/simple-agenda-crud-django.git
```
2. Navigate to the project directory:
```
pip install -r requirements.txt
```
3. Apply Django's database migrations
```
python manage.py migrate+
```
4. Run the development server.
```
python manage.py runserver
```
Access the application at http://127.0.0.1:8000/

## Usage
1. **Register/Login:** When you first run the app, no accounts are going to be registered, but you can create yours.
2. **View Agenda:** To view the agenda information just scroll down and navigate the pages with paginator.
3. **Creating Contacts:** To create a new contact just access the link to the form and fill it.
4. **Edit, Delete Agenda Items:** To edit or delete any contact just access them in the table (the buttons are on the bottom).
5. **Generating information:** I set up a script in the "tests" folder, run it directly to fill the database with random contacts.




