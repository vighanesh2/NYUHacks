from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, JSON, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

SQLALCHEMY_DATABASE_URL = "sqlite:///./sat_learning.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class GameSession(Base):
    __tablename__ = "game_sessions"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    game_type = Column(String)  # zombie, whackamole, carnival
    score = Column(Integer)
    correct_answers = Column(Integer)
    wrong_answers = Column(Integer)
    accuracy = Column(Float)
    max_streak = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    
class QuestionAttempt(Base):
    __tablename__ = "question_attempts"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    session_id = Column(Integer, index=True)
    question_id = Column(Integer)
    topic = Column(String)  # Algebra, Grammar, Reading, etc.
    difficulty = Column(String)  # easy, medium, hard
    is_correct = Column(Boolean)
    time_spent = Column(Float)  # seconds
    created_at = Column(DateTime, default=datetime.utcnow)

class UserTopicPerformance(Base):
    __tablename__ = "user_topic_performance"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    topic = Column(String, index=True)
    total_attempts = Column(Integer, default=0)
    correct_attempts = Column(Integer, default=0)
    accuracy = Column(Float, default=0.0)
    avg_time = Column(Float, default=0.0)
    last_updated = Column(DateTime, default=datetime.utcnow)

# Create all tables
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

