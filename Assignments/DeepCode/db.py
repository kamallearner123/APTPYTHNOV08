from app import app, db, Question

# Wrap database operations in an app context
with app.app_context():
    db.create_all()

    # Add sample question
    question1 = Question(
        title="Sum of Two Numbers",
        description="Write a program that takes two numbers as input and prints their sum.",
        example_input="Input: 3 5",
        example_output="Output: 8"
    )
    db.session.add(question1)
    db.session.commit()
