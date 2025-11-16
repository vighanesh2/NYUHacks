#!/usr/bin/env python3
"""
Quick test to see DuckDuckGo + Claude in action
"""

import asyncio
from database import SessionLocal, User
from agent import SATLearningAgent

async def test_with_search():
    print("🧪 Testing AI Agent with DuckDuckGo Search\n")
    print("=" * 60)
    
    db = SessionLocal()
    
    # Create or get test user
    test_user = db.query(User).filter(User.username == "ddg_test_user").first()
    if not test_user:
        test_user = User(username="ddg_test_user")
        db.add(test_user)
        db.commit()
        db.refresh(test_user)
        print(f"✅ Created user: {test_user.username} (ID: {test_user.id})\n")
    else:
        print(f"✅ Using existing user: {test_user.username} (ID: {test_user.id})\n")
    
    # Initialize agent
    agent = SATLearningAgent(db, test_user.id)
    
    print("🚀 Generating 5 questions WITH web search...\n")
    questions = await agent.generate_questions(5, use_web_search=True)
    
    if questions:
        print(f"\n✅ Generated {len(questions)} questions!\n")
        print("📝 Sample Question:")
        q = questions[0]
        print(f"   Topic: {q['topic']}")
        print(f"   Q: {q['question']}")
        print(f"   Options: {', '.join(q['options'])}")
        print(f"   Answer: {q['options'][q['correctAnswer']]}")
        print(f"   Reasoning: {q.get('reasoning', 'N/A')[:100]}...")
    else:
        print("❌ No questions generated")
    
    db.close()
    print("\n" + "=" * 60)
    print("✅ Test complete!\n")
    print("What you just saw:")
    print("1. 🦆 DuckDuckGo searched for real SAT questions")
    print("2. 📝 Search results added to Claude's context")
    print("3. 🤖 Claude Haiku 4.5 generated personalized questions")
    print("4. ✨ Result: Better, more realistic SAT questions!")

if __name__ == "__main__":
    asyncio.run(test_with_search())

