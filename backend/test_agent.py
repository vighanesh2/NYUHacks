"""
Quick test script for the SAT Learning Agent
Run this to verify your setup works!
"""

import asyncio
from database import SessionLocal, User, Base, engine
from agent import SATLearningAgent

async def test_agent():
    print("🧪 Testing SAT Learning Agent...\n")
    
    # Create tables
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created")
    
    # Create session
    db = SessionLocal()
    
    # Create test user
    test_user = User(username="test_student")
    db.add(test_user)
    db.commit()
    db.refresh(test_user)
    print(f"✅ Created test user: {test_user.username} (ID: {test_user.id})")
    
    # Initialize agent
    agent = SATLearningAgent(db, test_user.id)
    print("✅ Agent initialized")
    
    # Analyze performance (should be empty for new user)
    analysis = agent.analyze_performance()
    print(f"\n📊 Performance Analysis:")
    print(f"   Total Attempts: {analysis['total_attempts']}")
    print(f"   Recent Accuracy: {analysis['recent_accuracy']:.1f}%")
    print(f"   Recommended Difficulty: {analysis['recommended_difficulty']}")
    
    # Generate questions
    print(f"\n🤖 Generating 10 personalized questions...")
    try:
        questions = await agent.generate_questions(10)
        
        if questions:
            print(f"✅ Generated {len(questions)} questions!")
            print(f"\n📝 Sample Question:")
            q = questions[0]
            print(f"   Q: {q['question']}")
            print(f"   Options: {', '.join(q['options'])}")
            print(f"   Topic: {q['topic']}")
            print(f"   Difficulty: {q['difficulty']}")
            print(f"   Reasoning: {q.get('reasoning', 'N/A')}")
        else:
            print("❌ No questions generated")
    except Exception as e:
        print(f"❌ Error generating questions: {e}")
        print(f"   Make sure OPENROUTER_API_KEY is set!")
    
    # Get insights
    print(f"\n💡 Getting learning insights...")
    try:
        insights = await agent.get_learning_insights()
        print(f"✅ Insights generated!")
        print(f"   Focus Areas: {', '.join(insights.get('focus_areas', []))}")
        print(f"   Strategy: {insights.get('strategy', 'N/A')[:100]}...")
    except Exception as e:
        print(f"❌ Error getting insights: {e}")
    
    # Cleanup
    db.close()
    print(f"\n✅ Test complete!")

if __name__ == "__main__":
    from config import OPENROUTER_API_KEY
    
    # Check for API key
    if not OPENROUTER_API_KEY or OPENROUTER_API_KEY == "":
        print("⚠️  WARNING: OPENROUTER_API_KEY not configured!")
        print("   Check config.py or create a .env file")
        print("   Get a key at: https://openrouter.ai/keys")
        print("\n   Continuing anyway (will fail at question generation)...\n")
    else:
        print(f"✅ OpenRouter API key configured ({OPENROUTER_API_KEY[:20]}...)")
    
    asyncio.run(test_agent())

