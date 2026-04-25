🌤️ Skies — Weather App
A full-stack weather application built with FastAPI and PostgreSQL. Users can sign up, log in, search for real-time weather data, save it, and view their personal weather history.

Features

JWT-based authentication (signup & login)
Real-time weather data via Open-Meteo API
Save weather snapshots per user
Personal weather history page
Simple HTML/CSS/JS frontend


Tech Stack

Backend: FastAPI, SQLAlchemy (async), PostgreSQL, asyncpg
Auth: JWT (python-jose), bcrypt (passlib)
Weather API: Open-Meteo (free, no key needed)
Frontend: HTML, CSS, Vanilla JS


Project Structure
fast_api/
├── db/
│   ├── dao/
│   │   ├── user_dao.py       # User DB queries
│   │   └── weather_dao.py    # Weather DB queries
│   ├── models/
│   │   └── models.py         # SQLAlchemy models (User, Weather)
│   └── dependencies.py       # DB session injection
├── web/
│   └── api/
│       ├── auth/             # Signup & login endpoints
│       ├── weather/          # Weather fetch, save, history endpoints
│       └── router.py         # Central route registration
├── static/
│   ├── index.html            # Login / Signup page
│   ├── weather.html          # Weather search & save page
│   └── history.html          # Saved weather history page
├── settings.py               # App configuration
└── lifespan.py               # DB startup setup

Setup
1. Clone the repo
bashgit clone <your-repo-url>
cd fast_api
2. Create and activate virtual environment
bashpython -m venv venv
source venv/bin/activate
3. Install dependencies
bashpip install -r requirements.txt
4. Create .env file in the project root
bashFAST_API_DB_HOST=localhost
FAST_API_DB_PORT=5432
FAST_API_DB_USER=postgres
FAST_API_DB_PASS=your_password
FAST_API_DB_BASE=db
FAST_API_RELOAD=True
FAST_API_SECRET_KEY=your-secret-key
5. Create the PostgreSQL database
bashpsql -U postgres -c "CREATE DATABASE db;"
6. Run the app
bashpython -m fast_api
7. Open in browser
http://localhost:8000

API Endpoints
MethodEndpointDescriptionAuthPOST/api/auth/signupCreate accountNoPOST/api/auth/loginLogin, get JWT tokenNoGET/api/weather/fetch_weather?country=LondonFetch live weatherNoPOST/api/weather/saveSave weather to DBYesGET/api/weather/historyGet user's saved weatherYes
API docs available at: http://localhost:8000/docs

Notes

Tables are created automatically on first run
JWT tokens expire after 30 minutes
Weather data is sourced from Open-Meteo — free and no API key required
