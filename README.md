Campus Event Management Platform
-Project Overview
This project is a Campus Event Management System built with Flask and SQLAlchemy.
It allows:
College admins to create events (workshops, hackathons, tech talks, fests).
Students to register for events, mark attendance, and submit feedback.
Generating reports for event popularity, student participation, top active students, and filtering events by type.
This prototype uses SQLite for simplicity but can be extended to MySQL or Postgres.

Tech Stack
Backend: Python, Flask, Flask-SQLAlchemy
Database: SQLite
Testing: Postman
Optional: UI can be added using React or plain HTML/CSS

Project Structure
campus_event_management/
│
├─ app/
│   ├─ __init__.py       # Flask app setup
│   ├─ models.py         # Database models
│   └─ routes.py         # API routes
│
├─ run.py                # Entry point to run Flask server
├─ requirements.txt      # Python dependencies
└─ README.md             # Project documentation

API Endpoints
1. Health Check

GET /

Response: "✅ Campus Event Management API is running!"

2. Create Event

POST /event

Body (JSON):

{
    "name": "Hackathon",
    "type": "Workshop",
    "date": "2025-09-15",
    "college_id": 1
}

3. Register Student

POST /register

Body (JSON):

{
    "student_id": 1,
    "event_id": 1
}

4. Mark Attendance

POST /attendance

Body (JSON):

{
    "registration_id": 1,
    "attended": true
}

5. Submit Feedback

POST /feedback

Body (JSON):

{
    "registration_id": 1,
    "rating": 5
}

6. Event Popularity Report

GET /report/event-popularity
Returns number of registrations per event, sorted descending.

7. Student Participation Report

GET /report/student-participation
Returns number of events each student attended.

8. Top 3 Most Active Students

GET /report/top-active-students
Returns top 3 students by events attended.

9. Events by Type

GET /report/events-by-type/<event_type>
Example: /report/events-by-type/Workshop

Reports / Outputs

-Event Popularity Report: Shows events with most registrations.
-Student Participation Report: Shows how many events each student attended.
-Top 3 Active Students: Quickly identify most engaged students.
-Event Type Filter: View events by type (Workshop/Fest/Seminar).

Assumptions

-College ID and Event ID are unique.
-Students can register for multiple events.
-Attendance and feedback are linked to a registration record.
-Minimal error handling in prototype (can be extended).

Next Steps / Enhancements

-Add authentication for students and admins.
-Add UI for browsing events and registering.
-Move to MySQL/Postgres for multi-college scaling.
-Add email notifications for event reminders.

With this setup, all APIs and reports can be tested using Postman or any REST client.