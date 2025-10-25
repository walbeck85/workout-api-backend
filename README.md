# Summative Lab: Workout API Backend

## Project Overview
This project is a Flask-based backend API for a workout tracking application used by personal trainers. The API is responsible for:
- Creating, deleting, and viewing workouts.
- Creating, deleting, and viewing exercises.
- Adding an exercise to a workout (including reps / sets / duration data).

For this assessment, update actions are not required. You also do not need to support removing an exercise from a workout — only adding one.

The goal of this application is to demonstrate the ability to design and build a maintainable backend that:
- Defines models and relationships using SQLAlchemy.
- Enforces data integrity using table constraints, model validations, and schema validations.
- Serializes data and enforces request integrity using Marshmallow.
- Follows REST-style API patterns for common backend operations.

## Requirements Summary

### Data Integrity Requirements
Your API must include working examples of **all three** validation layers below. To earn full credit, you must have more than one working validation in each category:

1. **Table Constraints (database-level)**
   - Examples: `nullable=False`, `unique=True`, `CheckConstraint` to keep values in a valid range, etc.

2. **Model Validations (SQLAlchemy model-level)**
   - Custom Python validation using `@validates` to reject bad values before committing to the database.

3. **Schema Validations (Marshmallow-level)**
   - Marshmallow field and schema validators that prevent invalid incoming request data.

### Core Features
The API must support:
- Creating workouts
- Deleting workouts
- Viewing all workouts
- Viewing one workout (optionally including reps / sets / duration info per exercise)
- Creating exercises
- Deleting exercises
- Viewing all exercises
- Viewing one exercise (including which workouts use it)
- Adding an exercise to a workout (with reps / sets / duration)

No update/patch routes are required.

---

## Data Model

### Exercise
- `id` (integer, primary key)
- `name` (string)
- `category` (string)
- `equipment_needed` (boolean)

### Workout
- `id` (integer, primary key)
- `date` (date)
- `duration_minutes` (integer)
- `notes` (text)

### WorkoutExercise (Join Table)
- `id` (integer, primary key)
- `workout_id` (foreign key to Workout)
- `exercise_id` (foreign key to Exercise)
- `reps` (integer)
- `sets` (integer)
- `duration_seconds` (integer)

---

## Relationships

- A WorkoutExercise belongs to a Workout.
- A WorkoutExercise belongs to an Exercise.
- A Workout has many WorkoutExercises.
- An Exercise has many WorkoutExercises.
- A Workout has many Exercises through WorkoutExercises.
- An Exercise has many Workouts through WorkoutExercises.

These relationships must be represented in SQLAlchemy.

---

## Planned Routes (API Spec)

### Workouts
- `GET /workouts`  
  Return all workouts.
- `GET /workouts/<id>`  
  Return a single workout and its associated exercises.  
  Stretch goal: include reps / sets / duration info from the WorkoutExercise join records.
- `POST /workouts`  
  Create a new workout.
- `DELETE /workouts/<id>`  
  Delete a workout.  
  Stretch goal: also delete related WorkoutExercise rows.

### Exercises
- `GET /exercises`  
  Return all exercises.
- `GET /exercises/<id>`  
  Return a single exercise and the workouts it appears in.
- `POST /exercises`  
  Create a new exercise.
- `DELETE /exercises/<id>`  
  Delete an exercise.  
  Stretch goal: also delete related WorkoutExercise rows.

### Add Exercise to Workout
- `POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises`  
  Add an exercise to a specific workout, including reps / sets / duration info for that pairing.

---

## Validation Expectations

You will be graded on having working examples of:
- **Table Constraints**  
  Example: non-null columns, unique constraints, positive-number `CheckConstraint`, etc.

- **Model Validations**  
  Example: using `@validates` in a model to ensure `duration_minutes` is greater than 0, or `name` is not an empty string.

- **Schema Validations**  
  Example: Marshmallow field validators that reject invalid request JSON before creating a record.

All three layers must be present to earn full credit.

---

## Git Workflow Plan

This project will be developed using feature branches and pull requests to maintain clean history. The plan is:

1. `task-1-problem-definition`  
   - Add problem definition, feature scope, validation categories (this README work).
2. `task-2-design`  
   - Document data model, relationships, and endpoint spec.
3. `task-3-setup`  
   - Confirm Flask app scaffold (`server/app.py`), `server/models.py`, `seed.py`, Pipenv, and project layout.
4. `task-3-models`  
   - Implement SQLAlchemy models for Workout, Exercise, WorkoutExercise.
5. `task-3-relationships`  
   - Add SQLAlchemy relationships between models.
6. `task-3-validations`  
   - Add table constraints and `@validates` model methods.
7. `task-3-migrations`  
   - Initialize Flask-Migrate, generate and apply migrations.
8. `task-3-seed`  
   - Build and verify `seed.py` with working sample data.
9. `task-3-endpoints-skeleton`  
   - Scaffold all required routes in `server/app.py`.
10. `task-3-schemas`  
    - Create Marshmallow schemas.
11. `task-3-schema-validations`  
    - Add Marshmallow validation logic.
12. `task-3-endpoints-logic`  
    - Implement full endpoint logic using schemas (serialize + deserialize).
13. `task-4-test-debug`  
    - Verify seed script, run manual endpoint tests, clean comments.
14. `task-5-readme-and-final`  
    - Finalize README, ensure main branch is up to date.

Following this branching process and merging into `main` will directly support the “Git Workflow & Management” and “Code Structure & Maintainability” rubric criteria.

---

## Next Steps

We have completed `task-1-problem-definition` and merged it into `main`.

We are now on `task-2-design`. In this phase, we are documenting the data model and route structure directly in code comments (starting in `server/models.py`) so that intent is clear before implementing any SQLAlchemy models or migrations.

After Task 2 is merged, we will proceed to Task 3, where we will:
- Implement the actual SQLAlchemy models and relationships
- Add table constraints and model-level validations
- Initialize Flask-Migrate and generate the first database migration
- Seed the database and verify relationships/validations in `flask shell`
# Lab Submission: Flask SQLAlchemy Workout Application Backend

This repository contains my implementation for the Course 9 Summative Lab. The goal is to design and build a complete backend API for a workout tracking application using Flask, SQLAlchemy, and Marshmallow. The work here demonstrates relational database design, model and schema validation, data serialization, and RESTful API development following Flatiron’s rubric.

## Features

- Implements three relational models:
  - `Workout`
  - `Exercise`
  - `WorkoutExercise` (join table linking workouts and exercises)
- Provides full CRUD functionality:
  - Create, view, and delete workouts
  - Create, view, and delete exercises
  - Add an exercise to a workout with reps, sets, and duration
- Enforces multiple layers of validation:
  - Table constraints (e.g. NOT NULL, CHECK)
  - Model validations using `@validates`
  - Schema validations using Marshmallow
- Includes working seed data and migration scripts
- Clean branching and PR workflow using feature branches
- README includes setup, run, and endpoint documentation

## Environment

- Python 3.8.x (tested locally with 3.8.13)
- Flask 2.2.2
- Flask-Migrate 3.1.0
- Flask-SQLAlchemy 3.0.3
- Marshmallow 3.20.1
- macOS terminal with Pipenv for environment management

## Setup

Clone and enter the project directory:

```bash
git clone <https://github.com/walbeck85/workout-api-backend>
cd workout-api-backend
```

Install dependencies and activate the Pipenv shell:

```bash
pipenv install
pipenv shell
```

Set environment variables (once per session):

```bash
export FLASK_APP=server/app.py
export FLASK_RUN_PORT=5555
```

Run database migrations:

```bash
flask db upgrade
```

Seed the database with sample data:

```bash
python seed.py
```

Start the Flask development server:

```bash
pipenv run flask run
```

The API will be available at http://127.0.0.1:5555.

## Project Structure

```
.
├── Pipfile
├── Pipfile.lock
├── README.md
├── seed.py
├── server/
│   ├── __init__.py
│   ├── app.py
│   ├── models.py
│   └── schemas.py
└── migrations/
```

## How to Test the API

Once the server is running, you can use `curl` or Postman to test endpoints.

### Workouts
```bash
curl http://127.0.0.1:5555/workouts
curl http://127.0.0.1:5555/workouts/1
curl -X POST -H "Content-Type: application/json" \
  -d '{"date": "2025-10-25", "duration_minutes": 40, "notes": "Evening workout"}' \
  http://127.0.0.1:5555/workouts
curl -X DELETE http://127.0.0.1:5555/workouts/1
```

### Exercises
```bash
curl http://127.0.0.1:5555/exercises
curl http://127.0.0.1:5555/exercises/1
curl -X POST -H "Content-Type: application/json" \
  -d '{"name": "Lunges", "category": "Strength", "equipment_needed": false}' \
  http://127.0.0.1:5555/exercises
curl -X DELETE http://127.0.0.1:5555/exercises/1
```

### Add Exercise to Workout
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"reps": 12, "sets": 3, "duration_seconds": 60}' \
  http://127.0.0.1:5555/workouts/1/exercises/2/workout_exercises
```

### Health Check
```bash
curl http://127.0.0.1:5555/
```

## Rubric Alignment

- **Models**: Defined according to the provided entity relationships.
- **Relationships**: Fully mapped through SQLAlchemy ORM relationships.
- **Table Constraints**: Includes multiple `CheckConstraint` and `nullable=False` rules.
- **Model Validations**: Validates exercise names and positive durations using `@validates`.
- **Schema Validations**: Marshmallow enforces non-empty strings and positive numeric fields.
- **Serialization**: Uses Marshmallow schemas to serialize and deserialize nested relationships.
- **Endpoints**: All routes implemented and tested with proper status codes and error handling.
- **Seed File**: Creates starter data for all models without error.
- **Code Structure**: Modular structure with clear separation of concerns.
- **Git Workflow**: Organized feature branches merged through PRs.
- **README**: Includes setup instructions, endpoint documentation, and rubric coverage.

## Instructor Checklist

1. Clone the repository and install dependencies using Pipenv.
2. Activate the environment and run migrations:
   ```bash
   pipenv shell
   flask db upgrade
   ```
3. Seed the database with:
   ```bash
   python seed.py
   ```
4. Start the server:
   ```bash
   pipenv run flask run
   ```
5. Use the endpoint examples above to test functionality.
6. Confirm valid and invalid data handling in POST routes.
7. Review the models, schemas, and app routes for code clarity and rubric coverage.