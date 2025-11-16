# Backend - FastAPI

FastAPI backend for NYU Hacks Arcade. Handles authentication, game scores, user statistics, and question bank.

## Structure

```
backend/
├── src/
│   ├── api/                    # API route handlers
│   │   ├── auth.py            # Authentication endpoints
│   │   ├── games.py           # Game score endpoints
│   │   ├── stats.py           # User statistics endpoints
│   │   └── questions.py       # Question bank endpoints
│   ├── services/              # Business logic
│   │   ├── auth_service.py    # Authentication service
│   │   └── game_service.py    # Game score service
│   ├── models/                # Pydantic schemas
│   │   └── schemas.py         # Request/response models
│   ├── utils/                 # Utilities
│   │   └── database.py        # Database connection
│   └── main.py                # FastAPI app entry point
├── database/
│   └── schema.sql             # Database schema
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables
└── README.md                  # This file
```

## Setup

### 1. Install Python Dependencies

**Option A: Using the run script (recommended)**
```bash
cd backend
./run.sh
```

**Option B: Manual setup**
```bash
cd backend

# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Make sure your `.env` file has:

```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key
# OR
NEXT_PUBLIC_SUPABASE_URL=your_supabase_project_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_anon_key
```

### 3. Run the Server

**Using the script:**
```bash
./run.sh
```

**Or manually:**
```bash
# With virtual environment activated
python src/main.py

# Or with uvicorn directly
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Authentication

- `POST /api/auth/signup` - Sign up a new user
- `POST /api/auth/login` - Login user
- `POST /api/auth/logout` - Logout user
- `GET /api/auth/me` - Get current user info

### Games

- `POST /api/games/save-score` - Save game score and analytics

### Statistics

- `GET /api/stats/user` - Get user statistics
- `GET /api/stats/sessions` - Get recent game sessions

### Questions

- `GET /api/questions/` - Get questions from question bank
- `GET /api/questions/topics` - Get available topics

### Health Check

- `GET /` - API health check
- `GET /api/health` - Detailed health check

## API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Authentication

All endpoints (except `/api/auth/signup` and `/api/auth/login`) require authentication.

Include the token in the Authorization header:
```
Authorization: Bearer <your_access_token>
```

## Example Requests

### Signup
```bash
curl -X POST http://localhost:8000/api/auth/signup \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "password123"
  }'
```

### Login
```bash
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "password123"
  }'
```

### Save Game Score
```bash
curl -X POST http://localhost:8000/api/games/save-score \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <token>" \
  -d '{
    "gameId": "whackamole",
    "analytics": {
      "gameId": "whackamole",
      "score": 1000,
      "accuracy": 0.75,
      "correctAnswers": 3,
      "wrongAnswers": 1,
      "questionAttempts": [],
      "topicPerformance": {},
      "streakInfo": {"maxStreak": 2},
      "averageResponseTime": 5000
    }
  }'
```

### Get User Stats
```bash
curl -X GET http://localhost:8000/api/stats/user \
  -H "Authorization: Bearer <token>"
```

## Troubleshooting

### Python/pip not found
If you get errors about Python or pip not being found:
1. Make sure Python 3.8+ is installed: `python3 --version`
2. Use `python3` and `pip3` explicitly
3. Or create a virtual environment: `python3 -m venv venv`

### Dependencies installation fails
- Make sure you're using the correct Python version
- Try upgrading pip: `pip install --upgrade pip`
- Use virtual environment to avoid conflicts

### Database connection errors
- Verify `.env` file has correct Supabase credentials
- Check that database schema has been run in Supabase
- Ensure Supabase project is active

## Development

### Running in Development Mode

```bash
uvicorn src.main:app --reload
```

### Code Structure

- **API Routes** (`src/api/`) - Define endpoints and request/response handling
- **Services** (`src/services/`) - Business logic and database operations
- **Models** (`src/models/`) - Pydantic schemas for validation
- **Utils** (`src/utils/`) - Shared utilities like database connection

## Database

The backend uses Supabase (PostgreSQL) for data storage. Make sure you've run the schema from `database/schema.sql` in your Supabase project.

## CORS

The API is configured to allow requests from:
- `http://localhost:3000` (Next.js frontend)
- `http://localhost:3001`
- `http://127.0.0.1:3000`

To add more origins, update `src/main.py`.

## Next Steps

1. Update frontend to use FastAPI endpoints instead of Next.js API routes ✅
2. Implement question bank storage in database
3. Add more analytics endpoints
4. Add rate limiting
5. Add request logging
6. Add unit tests
