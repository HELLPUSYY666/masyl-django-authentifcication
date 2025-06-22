# masyl-django-authentifcication

# Project Overview

This project is a web application for creating a blog where users can share posts and leave comments about unusual phenomena. The application is built using Django and Redis and includes user authentication through Django Authentication. Users can write articles, comment on them, and interact with other members of the community.

# Features

User Registration and Authentication: Integrated with Django Authentication for secure account creation and login.
Content Management: Ability to create, edit, and delete posts.
Comments: Support for commenting on posts, allowing users to discuss and share opinions.
Notification System and Caching: Utilizes Redis for caching data and managing user sessions to enhance performance.
Modern Technologies: The project leverages Docker and Docker Compose for simplified deployment and container management.

## Tech Stack

- Python 3.x: The main programming language of the project.
- Django: Framework for building the server-side logic of the web application.
- Redis: Used for caching and session management.
- HTML/CSS: Used for building and styling the user interface.
- Docker: For packaging the application and its dependencies into containers.
- Docker Compose: For managing multi-container applications.
- Installation and Setup

# Requirements

Installed Docker
Installed Docker Compose

Clone the Repository
git clone https://github.com/HELLPUSYY666/masyl-django-authentifcication.git
cd masyl-django-authentifcication

Build and Run the Application
Build the containers with:
docker-compose build

Start the application:
docker-compose up

After a successful startup, open your browser and go to http://localhost:8000.

# Database Migrations
To run the database migrations, use the following command:
docker-compose run web python manage.py migrate

Create a Superuser
To create a superuser for managing the application via the admin interface, run:

docker-compose run web python manage.py createsuperuser
Project Structure

project_name/: The main project directory.
app_name/: The directory containing the application, including models, views, and URLs.
static/: Directory for storing static files (CSS, JavaScript).
templates/: Templates for rendering HTML.
manage.py: The script for running Django commands.
Dockerfile: Defines the instructions for building the application container.
docker-compose.yml: Configuration file for running a multi-container application.
requirements.txt: List of project dependencies.
Usage

Navigate to http://localhost:8000 to view the home page.
Register or log in to create posts and leave comments.
Once logged in, you can create and edit posts and comment on existing ones.
Contributing

We welcome contributions to the project! If you have suggestions for improvements or bug fixes, please create a pull request with a description of the changes made.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Author

Developer: Zakariya

Acknowledgements

Thanks to the Django team for creating an excellent framework.
Thanks to the Redis community for providing a powerful caching and session management solution.
Thanks to the Docker team for making containerized deployment simple.
This README file provides a comprehensive description of the project, its functionality, and instructions for installation and running.
