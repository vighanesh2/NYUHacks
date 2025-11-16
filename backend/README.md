# SAT Learning Agent Backend 🤖

AI-powered adaptive learning system using Claude Haiku 4.5 + DuckDuckGo search.

## 🚀 Quick Start

```bash
cd backend

# 1. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create .env file
echo "OPENROUTER_API_KEY=sk-or-v1-07950041baf..." > .env

# 4. Run server
python main.py
```

Server runs at: **http://localhost:8000**  
API docs at: **http://localhost:8000/docs**

## ✅ Quick Test

```bash
python test_api.py
```

You'll see:
- ✅ AI generating personalized SAT questions
- ✅ Claude Haiku 4.5 in action
- ✅ Database tracking performance

## 🎯 Key Features

- **Claude Haiku 4.5** - Fast, cheap, high-quality AI
- **Adaptive Learning** - Focuses 60% on weak topics
- **Performance Tracking** - Remembers user history
- **DuckDuckGo Search** - Finds real SAT questions (optional)
- **Supabase Ready** - Easy database migration

## 📊 API Endpoints

### `POST /users`
Create a user
```bash
curl -X POST http://localhost:8000/users \
  -H "Content-Type: application/json" \
  -d '{"username":"juan"}'
```

### `POST /questions`
Get 50 personalized SAT questions
```bash
curl -X POST http://localhost:8000/questions \
  -H "Content-Type: application/json" \
  -d '{"user_id":1,"num_questions":50}'
```

### `POST /game-results`
Submit game statistics
```bash
curl -X POST http://localhost:8000/game-results \
  -H "Content-Type: application/json" \
  -d '{
    "user_id":1,
    "game_type":"zombie",
    "score":850,
    "correct_answers":8,
    "wrong_answers":2,
    "accuracy":80.0,
    "max_streak":5,
    "question_attempts":[...]
  }'
```

### `GET /insights/{user_id}`
Get AI learning recommendations
```bash
curl http://localhost:8000/insights/1
```

## 🗄️ Supabase Setup (For Your Teammate)

**Currently using:** SQLite (local file)  
**For production:** Supabase (PostgreSQL)

### Migration Steps:

1. **Get Supabase connection string:**
   ```
   postgresql://postgres:[PASSWORD]@db.xxxxx.supabase.co:5432/postgres
   ```

2. **Update `.env`:**
   ```bash
   DATABASE_URL=postgresql://postgres:...
   ```

3. **Run SQL schema:**
   - Open Supabase SQL Editor
   - Paste contents of `supabase_schema.sql`
   - Click "Run"

4. **Install PostgreSQL driver:**
   ```bash
   pip install 'psycopg[binary]==3.2.3'
   ```

5. **Test:**
   ```bash
   python test_supabase.py
   ```

**That's it!** No code changes needed - SQLAlchemy handles both databases.

## 🔐 Adding Authentication

For Supabase Auth:

```bash
pip install supabase
```

Update `.env`:
```bash
SUPABASE_URL=https://xxxxx.supabase.co
SUPABASE_ANON_KEY=your_key_here
```

See `supabase_schema.sql` for auth setup.

## 🧠 How the AI Agent Works

### 1. Performance Analysis
```python
- Tracks accuracy per topic
- Identifies weak areas (<60%)
- Identifies strong areas (>80%)
```

### 2. Question Distribution
```python
# For 50 questions:
- 30 questions (60%) → Weak topics
- 15 questions (30%) → Mixed
- 5 questions (10%) → Challenge strong topics
```

### 3. Web Search (Optional)
```python
# Searches DuckDuckGo for real SAT questions
agent.generate_questions(50, use_web_search=True)
```

### 4. Adaptive Difficulty
```python
if accuracy < 50%:
    difficulty = "easy"
elif accuracy > 75%:
    difficulty = "hard"
```

## 📁 Project Structure

```
backend/
├── main.py              # FastAPI server
├── agent.py             # AI learning agent
├── database.py          # Database models
├── config.py            # Configuration
├── requirements.txt     # Dependencies
├── supabase_schema.sql  # Database schema
├── test_api.py          # API tests
└── .env                 # Secrets (not in git)
```

## 🛠️ Tech Stack

- **FastAPI** - Web framework
- **SQLAlchemy** - Database ORM
- **OpenRouter** - AI gateway
- **Claude Haiku 4.5** - Question generation
- **DuckDuckGo Search** - Web research
- **SQLite/PostgreSQL** - Database

## 🐛 Troubleshooting

**"Module not found"**
```bash
source venv/bin/activate
pip install -r requirements.txt
```

**"API key error"**
```bash
# Check .env file exists
cat .env
# Should show: OPENROUTER_API_KEY=sk-or-v1-...
```

**"DuckDuckGo rate limit"**
```python
# Temporary - from testing too fast
# Either wait 5 minutes or disable:
agent.generate_questions(50, use_web_search=False)
```

## 🎓 For Hackathon Demo

**Show the magic:**
1. Open http://localhost:8000/docs
2. Create a user
3. Generate questions - **watch Claude work!**
4. Submit game results
5. Get insights - **AI adapts to weak topics!**
6. Generate again - **60% focused on weaknesses!**

## 📚 Learn More

- [OpenRouter Docs](https://openrouter.ai/docs)
- [FastAPI Docs](https://fastapi.tiangolo.com)
- [Supabase Docs](https://supabase.com/docs)

---

**Built for NYU Hacks 2025! 🎓**
