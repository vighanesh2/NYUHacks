#!/usr/bin/env python3
"""
Test Supabase connection and setup
Run this after updating DATABASE_URL to Supabase
"""

from sqlalchemy import create_engine, text
from database import Base, User, GameSession, QuestionAttempt, UserTopicPerformance
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL

print("🧪 Testing Supabase Connection\n")
print("=" * 50)

# Test 1: Connection
print("\n1️⃣  Testing database connection...")
try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version();"))
        version = result.fetchone()[0]
        print(f"✅ Connected to PostgreSQL!")
        print(f"   Version: {version[:50]}...")
except Exception as e:
    print(f"❌ Connection failed: {e}")
    exit(1)

# Test 2: Create tables
print("\n2️⃣  Creating tables...")
try:
    Base.metadata.create_all(bind=engine)
    print("✅ All tables created!")
    
    # List tables
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema='public'
        """))
        tables = [row[0] for row in result]
        print(f"   Tables: {', '.join(tables)}")
except Exception as e:
    print(f"❌ Table creation failed: {e}")
    exit(1)

# Test 3: Insert test data
print("\n3️⃣  Testing data insertion...")
try:
    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal()
    
    # Create test user
    test_user = User(username="supabase_test_user")
    db.add(test_user)
    db.commit()
    db.refresh(test_user)
    
    print(f"✅ Created test user: {test_user.username} (ID: {test_user.id})")
    
    # Create test session
    test_session = GameSession(
        user_id=test_user.id,
        game_type="zombie",
        score=100,
        correct_answers=5,
        wrong_answers=5,
        accuracy=50.0,
        max_streak=3
    )
    db.add(test_session)
    db.commit()
    
    print(f"✅ Created test game session (ID: {test_session.id})")
    
    db.close()
except Exception as e:
    print(f"❌ Data insertion failed: {e}")
    exit(1)

# Test 4: Query data
print("\n4️⃣  Testing data retrieval...")
try:
    db = SessionLocal()
    
    users = db.query(User).all()
    sessions = db.query(GameSession).all()
    
    print(f"✅ Found {len(users)} user(s)")
    print(f"✅ Found {len(sessions)} session(s)")
    
    db.close()
except Exception as e:
    print(f"❌ Query failed: {e}")
    exit(1)

print("\n" + "=" * 50)
print("✅ ALL SUPABASE TESTS PASSED! 🎉")
print("\nYour database is ready!")
print("You can now:")
print("  1. Start the backend: python main.py")
print("  2. View data in Supabase dashboard")
print("  3. Use the API normally - everything works!")

