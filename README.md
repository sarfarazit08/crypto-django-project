# crypto-django-project

Setting up a Django project locally in VS Code involves several steps. 
I'll provide you with a step-by-step guide to help you get started. Make sure you have Python and VS Code installed on your system before proceeding.

**Step 1: Create a Virtual Environment**

It's a good practice to create a virtual environment to isolate your project dependencies. Open your terminal or command prompt and navigate to your project directory.

```bash
cd /path/to/your/project
```

Create a virtual environment (you can replace "venv" with your preferred name):

```bash
python -m venv venv
```

Activate the virtual environment:

- On Windows:

  ```bash
  venv\Scripts\activate
  ```

- On macOS and Linux:

  ```bash
  source venv/bin/activate
  ```

**Step 2: Install Django**

While the virtual environment is active, install Django using pip:

```bash
pip install django
```

**Step 3: Create a Django Project**

Create a new Django project using the following command (replace "projectname" with your preferred project name):

```bash
django-admin startproject projectname .
```

The "." at the end tells Django to create the project in the current directory.

**Step 4: Configure the Database**

Open the project's settings.py file (located in the project directory) in VS Code. Update the database settings with your preferred database engine, name, user, and password. By default, Django uses SQLite for local development:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

**Step 5: Apply Migrations**

Run the initial migrations to create the database schema:

```bash
python manage.py migrate
```

**Step 6: Create a Superuser**

Create a superuser account to access the Django admin interface:

```bash
python manage.py createsuperuser
```

Follow the prompts to enter a username, email, and password.

**Step 7: Start the Development Server**

Start the Django development server:

```bash
python manage.py runserver
```

You should see output indicating that the development server is running. By default, it will run on http://127.0.0.1:8000/.

**Step 8: Access the Admin Interface**

Open your web browser and go to http://127.0.0.1:8000/admin/. Log in with the superuser credentials you created in Step 6.

**Step 9: Start Building Your Django App**

You can now start building your Django app by creating models, views, templates, and URL patterns. Remember to activate your virtual environment every time you work on the project.

**Step 10: Install Required Packages**

As you develop your project, you may need to install additional Python packages. Always install them within your virtual environment using `pip install`.

That's it! You've successfully set up and run a Django project locally in VS Code. You can continue developing your project by creating Django apps, defining models, views, and templates, and configuring URL patterns.
