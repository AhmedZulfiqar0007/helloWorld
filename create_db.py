from app import app, db

# This ensures the app context is available
with app.app_context():
    db.drop_all()     # ⚠️ deletes old tables (important if you changed schema like adding email)
    db.create_all()   # creates new tables

    print("Database created successfully!")