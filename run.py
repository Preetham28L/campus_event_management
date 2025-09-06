from app import app, db

# Create tables if they don't exist
with app.app_context():
    db.create_all()
    print("✅ Tables created!")

if __name__ == "__main__":
    app.run(debug=True)
