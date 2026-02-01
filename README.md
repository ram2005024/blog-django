# Django Blog Application

A full-featured blog application built with Django, featuring user authentication, post management, and a clean, responsive interface.

**Live Demo:** [https://shekhar.pythonanywhere.com/](https://shekhar.pythonanywhere.com/)

## Features

- User registration and authentication
- Create, read, update, and delete blog posts
- Rich text editor for post creation
- User dashboard for managing posts
- Responsive design for mobile and desktop
- SQLite database for data storage
- Template-based rendering with Django templating engine

## Technology Stack

- **Framework:** Django 4.x
- **Database:** SQLite3
- **Frontend:** HTML, CSS, JavaScript
- **Deployment:** PythonAnywhere

## Project Structure

```
DJANGO-BLOG/
├── assignments/          # Blog assignments module
├── blog/                # Main blog application
├── blogs/               # Blog posts module
├── dashboard/           # User dashboard
├── env/                 # Virtual environment (not tracked)
├── media/               # Media files (uploads)
├── node_modules/        # Node.js dependencies (if any)
├── templates/           # HTML templates
├── .gitignore          # Git ignore file
├── db.sqlite3          # SQLite database
├── manage.py           # Django management script
├── package.json        # Node.js package configuration
├── package-lock.json   # Node.js package lock file
├── pyvenv.cfg          # Python virtual environment config
└── requirement.txt     # Python dependencies
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

### Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/ram2005024/blog-django.git
cd blog-django
```

2. **Create a virtual environment**

```bash
# On Windows
python -m venv env
env\Scripts\activate

# On macOS/Linux
python3 -m venv env
source env/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirement.txt
```

4. **Apply database migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create a superuser (admin account)**

```bash
python manage.py createsuperuser
```

Follow the prompts to set up your admin username, email, and password.

6. **Run the development server**

```bash
python manage.py runserver
```

7. **Access the application**

Open your browser and navigate to:
- **Homepage:** `http://127.0.0.1:8000/`
- **Admin Panel:** `http://127.0.0.1:8000/admin/`

## Configuration

### Environment Variables

For production deployment, consider setting the following environment variables:

```python
# In settings.py
DEBUG = False  # Set to False in production
ALLOWED_HOSTS = ['your-domain.com', 'www.your-domain.com']
SECRET_KEY = 'your-secret-key-here'  # Use environment variable
```

### Database Configuration

The application uses SQLite by default. For production, consider using PostgreSQL or MySQL.

## Usage

### Creating a Blog Post

1. Log in to your account or create a new one
2. Navigate to the Dashboard
3. Click "Create New Post"
4. Fill in the title, content, and any additional fields
5. Click "Publish" to make your post live

### Managing Posts

- View all your posts from the Dashboard
- Edit existing posts by clicking the "Edit" button
- Delete posts using the "Delete" option

## Deployment

This application is deployed on PythonAnywhere. To deploy your own instance:

1. Create a PythonAnywhere account
2. Upload your code via Git or the file manager
3. Set up a virtual environment on PythonAnywhere
4. Install dependencies
5. Configure the WSGI file
6. Set up static files
7. Reload your web app

Detailed deployment instructions can be found in the [PythonAnywhere documentation](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/).

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature/your-feature-name`)
6. Open a Pull Request

## Development Roadmap

- [ ] Add comment functionality
- [ ] Implement post categories and tags
- [ ] Add search functionality
- [ ] Integrate rich text editor (TinyMCE/CKEditor)
- [ ] Add user profile pages
- [ ] Implement pagination for blog posts
- [ ] Add social media sharing buttons

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

**Ram Sharma**

- GitHub: [@ram2005024](https://github.com/ram2005024)
- Project Link: [https://github.com/ram2005024/blog-django](https://github.com/ram2005024/blog-django)

## Acknowledgments

- Django documentation and community
- PythonAnywhere for hosting
- All contributors who help improve this project

---

**Note:** This is a learning project. Feedback and suggestions are always welcome!
