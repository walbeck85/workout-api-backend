#!/usr/bin/env python3

from datetime import date

from server.app import app
from server.models import db, Exercise, Workout, WorkoutExercise

# This script can be safely re-run.
# It will wipe and recreate the tables, then insert fresh sample data.

with app.app_context():
    print("Dropping all tables...")
    db.drop_all()

    print("Creating all tables...")
    db.create_all()

    # ----- Seed Exercises -----
    print("Seeding exercises...")
    pushups = Exercise(
        name="Push Ups",
        category="Strength",
        equipment_needed=False
    )

    squats = Exercise(
        name="Squats",
        category="Strength",
        equipment_needed=False
    )

    plank = Exercise(
        name="Plank",
        category="Core",
        equipment_needed=False
    )

    db.session.add_all([pushups, squats, plank])
    db.session.commit()

    # ----- Seed Workouts -----
    print("Seeding workouts...")
    w1 = Workout(
        date=date(2025, 10, 1),
        duration_minutes=30,
        notes="Morning strength session"
    )

    w2 = Workout(
        date=date(2025, 10, 3),
        duration_minutes=45,
        notes="Core and mixed work"
    )

    db.session.add_all([w1, w2])
    db.session.commit()

    # ----- Associate Exercises with Workouts -----
    print("Linking exercises to workouts...")
    we1 = WorkoutExercise(
        workout_id=w1.id,
        exercise_id=pushups.id,
        reps=20,
        sets=3,
        duration_seconds=None
    )

    we2 = WorkoutExercise(
        workout_id=w1.id,
        exercise_id=squats.id,
        reps=15,
        sets=4,
        duration_seconds=None
    )

    we3 = WorkoutExercise(
        workout_id=w2.id,
        exercise_id=plank.id,
        reps=None,
        sets=3,
        duration_seconds=60
    )

    db.session.add_all([we1, we2, we3])
    db.session.commit()

    print("✅ Seed complete.")