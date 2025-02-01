# Multilingual FAQ API

This project is a backend service for managing FAQs with multilingual support. It is built using Django and Django REST Framework (DRF) and includes features such as a WYSIWYG editor (via django-ckeditor), multi-language translation support, caching with Redis, and unit tests for code quality.

## Table of Contents

- [Installation Steps](#installation-steps)
- [API Usage Examples](#api-usage-examples)
- [Contribution Guidelines](#contribution-guidelines)
- [Deployment Instructions](#deployment-instructions)
- [Additional Information](#additional-information)

## Installation Steps

Follow these instructions to set up the project on your local machine:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Anjalispalve/multilingual-faq-api.git
   cd multilingual-faq-api
Set Up a Virtual Environment:

Create and activate a virtual environment:

Windows:

python -m venv env
env\Scripts\activate

python3 -m venv env
source env/bin/activate

Install Dependencies:

Install the required packages listed in requirements.txt:


pip install -r requirements.txt
Set Up Environment Variables:

Create a .env file in the root directory and add the following configurations:

env

DJANGO_SECRET_KEY=your_secret_key
DEBUG=True
Run Migrations:

Apply database migrations to set up the database schema:


python manage.py makemigrations
python manage.py migrate
Create a Superuser:

To access the admin panel, create a superuser account:


python manage.py createsuperuser
Run the Development Server:

# Start the server to test your installation:


python manage.py runserver
Your project should now be running at http://127.0.0.1:8000/.

API Usage Examples
Here are some example API requests:

Fetch FAQs:

Fetch all FAQs in English:


curl http://127.0.0.1:8000/faqs/?lang=en
Create a New FAQ:

Create a new FAQ entry with the following request:


curl -X POST http://127.0.0.1:8000/api/faqs/ \
     -H "Content-Type: application/json" \
     -d '{
           "question": "What is Django?",
           "answer": "<p>A high-level Python web framework.</p>"
         }'
Update an Existing FAQ:

Update an FAQ entry with ID 1:


curl -X PUT http://127.0.0.1:8000/api/faqs/1/ \
     -H "Content-Type: application/json" \
     -d '{
           "question": "What is Django?",
           "answer": "<p>An advanced Python web framework.</p>"
         }'
Delete an FAQ:

Delete the FAQ with ID 1:


curl -X DELETE http://127.0.0.1:8000/api/faqs/1/
Contribution Guidelines
We welcome contributions to this project! Here's how you can contribute:

Fork the Repository:

Fork the repository to your GitHub account.
Clone Your Fork:

git clone https://github.com/Anjalispalve/multilingual-faq-api.git
cd project-name
Create a New Branch:

Create a new branch for your changes:


git checkout -b feature/your-feature-name
Make Changes and Commit:

Follow coding standards.

Write meaningful commit messages following the Conventional Commits format:

feat: Add new feature
fix: Correct an issue
docs: Update README.md
Commit your changes:


git add .
git commit -m "feat: Add multilingual FAQ model"
Push Changes:

Push your changes to your fork:


git push origin feature/your-feature-name
Open a Pull Request:

Open a pull request from your fork's branch to the main repository's main branch.
Deployment Instructions
To deploy the project, follow these steps:

# Docker Setup
Build Docker Image:


docker build -t project-name .
Run with Docker Compose:


docker-compose up --build
This will start both the Django application and any required services (e.g., Redis for caching).

Deploy to Heroku
Create a New Heroku App:


heroku create
Push to Heroku:


git push heroku main
Run Migrations on Heroku:

heroku run python manage.py migrate
Open Your App:

heroku open
Additional Information
Admin Panel:
Access the Django admin panel at http://127.0.0.1:8000/admin/ using the superuser credentials you created.

Caching:
This project uses Redis for caching to improve performance. Ensure Redis is running locally or modify the environment variables to use a hosted service.

# Unit Tests:
Run the unit tests using:

python -m pytest
