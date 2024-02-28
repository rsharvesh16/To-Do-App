
# Django ToDo Application

This is a simple ToDo application built using Django, allowing users to create, manage, and store tasks.

## Features

- Create, edit, and delete tasks.
- Mark tasks as completed.
- Simple and user-friendly interface.

## Installation

To install and run this application, follow these steps:

1. Clone this repository:

   ```bash
   git clone https://github.com/rsharvesh16/To-Do-App.git
   ```

2. Change into the project directory:

   ```bash
   cd To-Do-App
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser account:

   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

7. Visit `http://127.0.0.1:8000/` in your browser to access the application.

## Usage

Once the application is running, you can access it through your browser. You will see a list of existing tasks and options to add, edit, or delete tasks. To mark a task as completed, simply click on the checkbox next to it.

## Contributing

Contributions are open soon! Once it is Licenced, If you have any suggestions, improvements, or new features to add, feel free to open an issue or create a pull request.
