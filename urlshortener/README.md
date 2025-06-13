# Secure URL Shortener Backend

A Django-based URL shortener backend application with password protection for shortened URLs.

## Features

- URL shortening with custom short codes
- Password protection for shortened URLs
- Secure password hashing and storage

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Create a superuser (admin account):
```bash
python manage.py createsuperuser
```

5. Start the development server:
```bash
python manage.py runserver
```

The server will start at http://localhost:8000

## API Endpoints

- `POST /api/shorten/` - Create a shortened URL
  - Request body: 
    ```json
    {
      "url": "https://example.com",
      "password": "your-secure-password"  // Optional
    }
    ```
  - Response: 
    ```json
    {
      "short_url": "http://localhost:8000/abc123",
      "has_password": true  // If password was provided
    }
    ```

- `GET /<short_code>` - Access the shortened URL
  - If password protected, will return a password form
  - After correct password, redirects to the original URL

- `POST /api/verify-password/<short_code>/` - Verify password for protected URL
  - Request body:
    ```json
    {
      "password": "your-password"
    }
    ```
  - Response:
    ```json
    {
      "success": true,
      "redirect_url": "https://original-url.com"
    }
    ```

## Security Features

- Passwords are hashed using Django's secure password hashing
- Rate limiting on password attempts
- CSRF protection on all forms
- Secure session management
- Password strength requirements
- Optional expiration dates for shortened URLs

## Admin Interface

Access the admin interface at `/admin` to:
- View all shortened URLs
- Manage passwords
- View access statistics
- Delete or modify existing URLs
- Set URL expiration dates 