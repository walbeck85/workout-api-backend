"""
server/models.py
----------------
This module defines the data model and relationships for the Workout API backend.

The design follows a three-table relational schema:
    - Workout
    - Exercise
    - WorkoutExercise (join table)

Each table and relationship is outlined below before implementation.
"""

# Import dependencies
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

# ---------------------------------------------------------------------
# ENTITY DESIGN (to be implemented in Task 3)
# ---------------------------------------------------------------------

# Exercise
"""
Represents an individual exercise that can be used across multiple workouts.
Attributes:
    id (Integer, Primary Key)
    name (String)
    category (String)
    equipment_needed (Boolean)
Relationships:
    - Has many WorkoutExercises
    - Has many Workouts through WorkoutExercises
"""

# Workout
"""
Represents a single workout session, containing one or more exercises.
Attributes:
    id (Integer, Primary Key)
    date (Date)
    duration_minutes (Integer)
    notes (Text)
Relationships:
    - Has many WorkoutExercises
    - Has many Exercises through WorkoutExercises
"""

# WorkoutExercise (Join Table)
"""
Associates a Workout with an Exercise, including extra metadata.
Attributes:
    id (Integer, Primary Key)
    workout_id (Foreign Key → Workout.id)
    exercise_id (Foreign Key → Exercise.id)
    reps (Integer)
    sets (Integer)
    duration_seconds (Integer)
Relationships:
    - Belongs to Workout
    - Belongs to Exercise
"""

# ---------------------------------------------------------------------
# RELATIONSHIP DIAGRAM (Conceptual)
# ---------------------------------------------------------------------
# Workout 1───∞ WorkoutExercise ∞───1 Exercise
# ---------------------------------------------------------------------