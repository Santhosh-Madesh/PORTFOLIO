# Portfolio Website

A full-stack portfolio website built with Django (backend) and React (frontend). The Django backend serves as an API to fetch GitHub projects and activities, and also serves the React Single Page Application.

## Features

- **GitHub Integration**: Automatically fetches and displays your latest GitHub repositories
- **GitHub Activity Feed**: Shows your recent GitHub activity and events
- **Modern React Frontend**: Built with React 19.2.0 for a responsive and interactive user experience
- **Django REST API**: Backend API endpoints for fetching GitHub data
- **Single Page Application**: React SPA served through Django with proper routing

## Tech Stack

### Backend
- **Django 5.2.7**: Web framework
- **Django REST Framework**: For building REST APIs
- **SQLite**: Database (default Django database)
- **WhiteNoise**: Static file serving
- **django-cors-headers**: CORS middleware for cross-origin requests
- **requests**: For making HTTP requests to GitHub API

### Frontend
- **React 19.2.0**: Frontend library
- **React Scripts 5.0.1**: Build tools and scripts
- **Tailwind CSS 4.1.16**: CSS framework for styling

## Project Structure

```
PORTFOLIO/
├── DJANGOPORTFOLIO/          # Django backend project
│   ├── DJANGOPORTFOLIO/      # Django project settings
│   │   ├── settings.py       # Django configuration
│   │   ├── urls.py           # Main URL routing
│   │   └── ...
│   ├── PORTFOLIO/            # Django app
│   │   ├── views.py          # API views
│   │   ├── urls.py           # App URL patterns
│   │   ├── build/            # React build output (generated)
│   │   └── ...
│   ├── manage.py
│   └── db.sqlite3            # SQLite database
│
├── my-portfolio/             # React frontend
│   ├── src/
│   │   ├── components/       # React components
│   │   │   ├── Navbar.jsx
│   │   │   ├── Projects.jsx
│   │   │   ├── Events.jsx
│   │   │   └── ...
│   │   ├── App.jsx           # Main React component
│   │   └── ...
│   ├── public/
│   └── package.json
│
└── requirements.txt          # Python dependencies
```

## Prerequisites

- **Python 3.8+**: Required for Django backend
- **Node.js 14+**: Required for React frontend
- **npm** or **yarn**: Package manager for Node.js

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd PORTFOLIO
```

### 2. Backend Setup

1. Create and activate a Python virtual environment:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

2. Install Python dependencies:

```bash
pip install -r requirements.txt
```

3. Run database migrations:

```bash
cd DJANGOPORTFOLIO
python manage.py migrate
```

### 3. Frontend Setup

1. Navigate to the React app directory:

```bash
cd my-portfolio
```

2. Install Node.js dependencies:

```bash
npm install
```

### 4. Configuration

1. Update the GitHub username in `DJANGOPORTFOLIO/DJANGOPORTFOLIO/settings.py`:

```python
GITHUB_USERNAME = "YOUR_GITHUB_USERNAME"
```

2. Build the React app for production (when deploying):

```bash
cd my-portfolio
npm run build
```

3. Copy the build folder to Django app (if needed):

```bash
# Copy my-portfolio/build to DJANGOPORTFOLIO/PORTFOLIO/build
```

Note: The build output should be placed in `DJANGOPORTFOLIO/PORTFOLIO/build/` for Django to serve it.

## Running the Project

### Development Mode

#### Option 1: Run Django and React separately (Recommended for development)

1. **Start Django backend** (in one terminal):

```bash
cd DJANGOPORTFOLIO
python manage.py runserver
```

The Django server will run on `http://localhost:8000`

2. **Start React development server** (in another terminal):

```bash
cd my-portfolio
npm start
```

The React app will run on `http://localhost:3000`

The CORS settings are configured to allow requests from `http://localhost:3000` to the Django backend.

#### Option 2: Run Django only (serves built React app)

1. Build the React app first:

```bash
cd my-portfolio
npm run build
```

2. Copy the build folder to Django app directory (ensure `PORTFOLIO/build/` exists)

3. Run Django server:

```bash
cd DJANGOPORTFOLIO
python manage.py runserver
```

Visit `http://localhost:8000` to see the application.

### Production Mode

1. Set `DEBUG = False` in `settings.py` (already set)
2. Update `ALLOWED_HOSTS` with your domain
3. Set a proper `SECRET_KEY` in production
4. Build the React app:

```bash
cd my-portfolio
npm run build
```

5. Collect static files:

```bash
cd DJANGOPORTFOLIO
python manage.py collectstatic
```

6. Run with a production WSGI server (e.g., Gunicorn):

```bash
gunicorn DJANGOPORTFOLIO.wsgi:application
```

## API Endpoints

The Django backend provides the following REST API endpoints:

- **GET `/api/projects/`**: Fetches the latest 6 GitHub repositories for the configured user
- **GET `/api/events/`**: Fetches the latest 5 GitHub public events for the configured user

Both endpoints return JSON responses:
- Projects: `{"repos": [...]}`
- Events: `{"events": [...]}`

## Components

The React frontend includes the following main components:

- **Navbar**: Navigation bar component
- **Projects**: Displays GitHub repositories
- **Events**: Displays GitHub activity feed
- Additional components in `src/components/` for various sections

## Environment Variables

Currently, the GitHub username is configured in `settings.py` as `GITHUB_USERNAME`. For better security and flexibility, consider using environment variables:

```python
import os
GITHUB_USERNAME = os.environ.get('GITHUB_USERNAME', 'default-username')
```

Then set it as:
```bash
export GITHUB_USERNAME=your-username  # Linux/Mac
set GITHUB_USERNAME=your-username     # Windows
```

## Database

The project uses SQLite by default. For production, consider using PostgreSQL or another production-grade database. Update `DATABASES` in `settings.py` accordingly.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Notes

- Make sure the React build output is placed in the correct directory (`DJANGOPORTFOLIO/PORTFOLIO/build/`) for Django to serve it
- The `STATICFILES_DIRS` in `settings.py` points to the React build static files
- CORS is configured to allow requests from `http://localhost:3000` during development
- Update `ALLOWED_HOSTS` in `settings.py` before deploying to production


