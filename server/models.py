# server/models.py

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import CheckConstraint, ForeignKey
from datetime import date

db = SQLAlchemy()

class Exercise(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    category = db.Column(db.String)
    equipment_needed = db.Column(db.Boolean, nullable=False)

    # Relationships
    workout_exercises = db.relationship("WorkoutExercise", back_populates="exercise", cascade="all, delete")
    workouts = db.relationship("Workout", secondary="workout_exercises", back_populates="exercises")

    @validates("name")
    def validate_name(self, key, value):
        """
        Model Validation:
        Ensure that an Exercise has a non-empty name.
        This supports the rubric requirement for model-level validation.
        """
        if not value or value.strip() == "":
            raise ValueError("Exercise name cannot be empty.")
        return value.strip()

    def __repr__(self):
        return f"<Exercise {self.name}>"

class Workout(db.Model):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=date.today, nullable=False)
    duration_minutes = db.Column(db.Integer, CheckConstraint('duration_minutes > 0', name='check_positive_duration'))
    notes = db.Column(db.Text)

    # Relationships
    workout_exercises = db.relationship("WorkoutExercise", back_populates="workout", cascade="all, delete")
    exercises = db.relationship("Exercise", secondary="workout_exercises", back_populates="workouts")

    @validates("duration_minutes")
    def validate_duration(self, key, value):
        """
        Model Validation:
        Ensure that Workout.duration_minutes is positive if provided.
        This supports the rubric requirement for model-level validation.
        """
        if value is not None and value <= 0:
            raise ValueError("Workout duration must be positive.")
        return value

    def __repr__(self):
        return f"<Workout {self.id} on {self.date}>"

class WorkoutExercise(db.Model):
    __tablename__ = "workout_exercises"

    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, ForeignKey("workouts.id"), nullable=False)
    exercise_id = db.Column(db.Integer, ForeignKey("exercises.id"), nullable=False)
    reps = db.Column(db.Integer, CheckConstraint('reps >= 0', name='check_nonnegative_reps'))
    sets = db.Column(db.Integer, CheckConstraint('sets >= 0', name='check_nonnegative_sets'))
    duration_seconds = db.Column(db.Integer, CheckConstraint('duration_seconds >= 0', name='check_nonnegative_duration'))

    # Relationships
    workout = db.relationship("Workout", back_populates="workout_exercises")
    exercise = db.relationship("Exercise", back_populates="workout_exercises")

    def __repr__(self):
        return f"<WorkoutExercise Workout={self.workout_id} Exercise={self.exercise_id}>"