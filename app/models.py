from . import db

class College(db.Model):
    __tablename__ = "colleges"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    students = db.relationship("Student", backref="college", lazy=True)
    events = db.relationship("Event", backref="college", lazy=True)

class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    college_id = db.Column(db.Integer, db.ForeignKey("colleges.id"), nullable=False)
    registrations = db.relationship("Registration", backref="student", lazy=True)

class Event(db.Model):
    __tablename__ = "events"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    college_id = db.Column(db.Integer, db.ForeignKey("colleges.id"), nullable=False)
    registrations = db.relationship("Registration", backref="event", lazy=True)

class Registration(db.Model):
    __tablename__ = "registrations"
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey("events.id"), nullable=False)
    attendance = db.relationship("Attendance", backref="registration", lazy=True)
    feedback = db.relationship("Feedback", backref="registration", lazy=True)

class Attendance(db.Model):
    __tablename__ = "attendance"
    id = db.Column(db.Integer, primary_key=True)
    registration_id = db.Column(db.Integer, db.ForeignKey("registrations.id"), nullable=False)
    attended = db.Column(db.Boolean, default=False)

class Feedback(db.Model):
    __tablename__ = "feedback"
    id = db.Column(db.Integer, primary_key=True)
    registration_id = db.Column(db.Integer, db.ForeignKey("registrations.id"), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
