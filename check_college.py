from app import db, app
from app.models import College

with app.app_context():
    colleges = College.query.all()
    if colleges:
        for c in colleges:
            print(f"College ID: {c.id}, Name: {c.name}")
    else:
        print("❌ No colleges found in the database.")
