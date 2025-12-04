# Weather App

A modern weather application built with Django and TailwindCSS that provides current weather information and forecasts.

## Features

- Current weather conditions
- Hourly and daily forecasts
- Responsive design with dark/light mode
- Location-based weather information
- Weather alerts and notifications

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- WeatherAPI.com API key (free tier available)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd WeatherApp
   ```

2. Create and activate a virtual environment:
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Update the `.env` file with your configuration

## Configuration

1. Get your free API key from [WeatherAPI.com](https://www.weatherapi.com/)
2. Update the `.env` file with your API key and other settings

## Running the Application

1. Apply migrations:
   ```bash
   python manage.py migrate
   ```

2. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

3. Run the development server:
   ```bash
   python manage.py runserver
   ```

4. Open your browser and navigate to `http://127.0.0.1:8000/`

## Project Structure

```
WeatherApp/
├── WeatherProject/         # Django project settings
├── weather/               # Main app
│   ├── migrations/        # Database migrations
│   ├── static/            # Static files (CSS, JS, images)
│   ├── templates/         # HTML templates
│   ├── __init__.py
│   ├── admin.py          # Admin configuration
│   ├── apps.py           # App configuration
│   ├── models.py         # Database models
│   ├── urls.py           # URL routing
│   └── views.py          # View functions
├── .env.example          # Example environment variables
├── manage.py             # Django management script
└── requirements.txt      # Python dependencies
```

## Technologies Used

- **Backend**: Django 5.0.1
- **Frontend**: HTML5, TailwindCSS
- **API**: WeatherAPI.com
- **Database**: SQLite (development), PostgreSQL (production-ready)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
