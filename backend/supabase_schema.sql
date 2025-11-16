-- SAT Learning Arcade - Supabase Database Schema
-- Copy and paste this into Supabase SQL Editor

-- Drop existing tables if they exist (optional, for fresh start)
DROP TABLE IF EXISTS question_attempts CASCADE;
DROP TABLE IF EXISTS user_topic_performance CASCADE;
DROP TABLE IF EXISTS game_sessions CASCADE;
DROP TABLE IF EXISTS users CASCADE;

-- Users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Game sessions table
CREATE TABLE game_sessions (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    game_type VARCHAR(50) NOT NULL,
    score INTEGER DEFAULT 0,
    correct_answers INTEGER DEFAULT 0,
    wrong_answers INTEGER DEFAULT 0,
    accuracy FLOAT DEFAULT 0.0,
    max_streak INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Question attempts table
CREATE TABLE question_attempts (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    session_id INTEGER REFERENCES game_sessions(id) ON DELETE CASCADE,
    question_id INTEGER,
    topic VARCHAR(100),
    difficulty VARCHAR(20),
    is_correct BOOLEAN,
    time_spent FLOAT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- User topic performance table
CREATE TABLE user_topic_performance (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    topic VARCHAR(100) NOT NULL,
    total_attempts INTEGER DEFAULT 0,
    correct_attempts INTEGER DEFAULT 0,
    accuracy FLOAT DEFAULT 0.0,
    avg_time FLOAT DEFAULT 0.0,
    last_updated TIMESTAMP DEFAULT NOW(),
    UNIQUE(user_id, topic)
);

-- Indexes for better performance
CREATE INDEX idx_question_attempts_user_id ON question_attempts(user_id);
CREATE INDEX idx_question_attempts_topic ON question_attempts(topic);
CREATE INDEX idx_question_attempts_session_id ON question_attempts(session_id);
CREATE INDEX idx_game_sessions_user_id ON game_sessions(user_id);
CREATE INDEX idx_user_topic_performance_user_id ON user_topic_performance(user_id);

-- Optional: Enable Row Level Security (for production)
-- ALTER TABLE users ENABLE ROW LEVEL SECURITY;
-- ALTER TABLE game_sessions ENABLE ROW LEVEL SECURITY;
-- ALTER TABLE question_attempts ENABLE ROW LEVEL SECURITY;
-- ALTER TABLE user_topic_performance ENABLE ROW LEVEL SECURITY;

-- Verify tables were created
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema='public'
ORDER BY table_name;

-- Show success message
SELECT 'Database schema created successfully!' as status;

