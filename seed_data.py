from app import db, app
from app.models import College, Student

with app.app_context():
    
    college = College(name="REVA University")
    db.session.add(college)
    db.session.commit()

    
    student = Student(name="Preetham", college_id=college.id)
    db.session.add(student)
    db.session.commit()

    print(f"✅ College ID: {college.id}, Student ID: {student.id}")
