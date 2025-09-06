from flask import request, jsonify
from . import app, db
from .models import College, Student, Event, Registration, Attendance, Feedback

@app.route("/")
def home():
    return "✅ Campus Event Management API is running!"


@app.route("/event", methods=["POST"])
def create_event():
    data = request.get_json()
    event = Event(
        name=data["name"],
        type=data["type"],
        date=data["date"],
        college_id=data["college_id"]
    )
    db.session.add(event)
    db.session.commit()
    return jsonify({"message": "Event created", "event_id": event.id})


@app.route("/register", methods=["POST"])
def register_student():
    data = request.get_json()
    registration = Registration(
        student_id=data["student_id"],
        event_id=data["event_id"]
    )
    db.session.add(registration)
    db.session.commit()
    return jsonify({"message": "Student registered", "registration_id": registration.id})


@app.route("/attendance", methods=["POST"])
def mark_attendance():
    data = request.get_json()
    att = Attendance(
        registration_id=data["registration_id"],
        attended=data["attended"]
    )
    db.session.add(att)
    db.session.commit()
    return jsonify({"message": "Attendance marked"})


@app.route("/feedback", methods=["POST"])
def submit_feedback():
    data = request.get_json()
    fb = Feedback(
        registration_id=data["registration_id"],
        rating=data["rating"]
    )
    db.session.add(fb)
    db.session.commit()
    return jsonify({"message": "Feedback submitted"})


@app.route("/report/event-popularity")
def event_popularity():
    events = Event.query.all()
    report = []
    for e in events:
        count = Registration.query.filter_by(event_id=e.id).count()
        report.append({"event_name": e.name, "registrations": count})
    report.sort(key=lambda x: x["registrations"], reverse=True)
    return jsonify(report)

@app.route("/report/student-participation")
def student_participation():
    students = Student.query.all()
    report = []
    for s in students:
        count = Registration.query.filter_by(student_id=s.id).count()
        report.append({"student_name": s.name, "events_attended": count})
    return jsonify(report)

@app.route("/report/top-active-students")
def top_active_students():
    students = Student.query.all()
    report = []
    for s in students:
        count = Registration.query.filter_by(student_id=s.id).count()
        report.append({"student_name": s.name, "events_attended": count})
    report.sort(key=lambda x: x["events_attended"], reverse=True)
    return jsonify(report[:3])

@app.route("/report/events-by-type/<event_type>")
def events_by_type(event_type):
    events = Event.query.filter_by(type=event_type).all()
    report = [{"event_name": e.name, "date": e.date} for e in events]
    return jsonify(report)
