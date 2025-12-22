from app import app, db, Election, Candidate
from datetime import date

with app.app_context():
    db.create_all()

    election = Election.query.first()
    if not election:
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

    if not election.candidates:
        c1 = Candidate(
            name="John Doe",
            position="President",
            manifesto="Improving transparency and student engagement.",
            election=election
        )

        c2 = Candidate(
            name="Jane Smith",
            position="President",
            manifesto="Building a better academic environment.",
            election=election
        )

        db.session.add_all([c1, c2])
        db.session.commit()
        print("Candidates seeded successfully")
    else:
        print("Candidates already exist")
