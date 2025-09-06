from app import app, db
from sqlalchemy import text

with app.app_context():
    try:
        db.session.execute(text("SELECT 1"))
        print("✅ Database connected!")
    except Exception as e:
        print(f"❌ Connection failed: {e}")
