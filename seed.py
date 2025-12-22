from app import app, db, Election
from datetime import date

with app.app_context():
    db.create_all()

    if not Election.query.first():
        election = Election(
            name="2025 Student Union Elections",
            scope="general",
            description="General student union elections for all students.",
            start_date=date(2025, 3, 10),
            end_date=date(2025, 3, 12)
        )
        db.session.add(election)
        db.session.commit()
        print("Election seeded successfully")
    else:
        print("Election already exists")
