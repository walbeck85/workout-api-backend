from flask import Flask, request, jsonify, make_response
from flask_migrate import Migrate
from server.models import db, Workout, Exercise, WorkoutExercise
from server.schemas import WorkoutSchema, ExerciseSchema, WorkoutExerciseSchema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

# Instantiate schemas
workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)
exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)
workout_exercise_schema = WorkoutExerciseSchema()
workout_exercises_schema = WorkoutExerciseSchema(many=True)


# ---------------------------
# Workouts Routes
# ---------------------------

@app.get("/workouts")
def get_workouts():
    """List all workouts"""
    workouts = Workout.query.all()
    return make_response(workouts_schema.dump(workouts), 200)


@app.get("/workouts/<int:workout_id>")
def get_workout_by_id(workout_id):
    """Get a single workout and its associated exercises"""
    workout = Workout.query.get(workout_id)
    if not workout:
        return make_response({"error": "Workout not found"}, 404)
    return make_response(workout_schema.dump(workout), 200)


@app.post("/workouts")
def create_workout():
    """Create a new workout"""
    try:
        data = request.get_json()
        validated = workout_schema.load(data)
    except Exception as e:
        return make_response({"error": str(e)}, 400)

    new_workout = Workout(**validated)
    db.session.add(new_workout)
    db.session.commit()

    return make_response(workout_schema.dump(new_workout), 201)


@app.delete("/workouts/<int:workout_id>")
def delete_workout(workout_id):
    """Delete a workout"""
    workout = Workout.query.get(workout_id)
    if not workout:
        return make_response({"error": "Workout not found"}, 404)

    db.session.delete(workout)
    db.session.commit()
    return make_response({}, 204)


# ---------------------------
# Exercises Routes
# ---------------------------

@app.get("/exercises")
def get_exercises():
    """List all exercises"""
    exercises = Exercise.query.all()
    return make_response(exercises_schema.dump(exercises), 200)


@app.get("/exercises/<int:exercise_id>")
def get_exercise_by_id(exercise_id):
    """Get one exercise with its associated workouts"""
    exercise = Exercise.query.get(exercise_id)
    if not exercise:
        return make_response({"error": "Exercise not found"}, 404)
    return make_response(exercise_schema.dump(exercise), 200)


@app.post("/exercises")
def create_exercise():
    """Create a new exercise"""
    try:
        data = request.get_json()
        validated = exercise_schema.load(data)
    except Exception as e:
        return make_response({"error": str(e)}, 400)

    new_exercise = Exercise(**validated)
    db.session.add(new_exercise)
    db.session.commit()

    return make_response(exercise_schema.dump(new_exercise), 201)


@app.delete("/exercises/<int:exercise_id>")
def delete_exercise(exercise_id):
    """Delete an exercise"""
    exercise = Exercise.query.get(exercise_id)
    if not exercise:
        return make_response({"error": "Exercise not found"}, 404)

    db.session.delete(exercise)
    db.session.commit()
    return make_response({}, 204)


# ---------------------------
# Add Exercise to Workout
# ---------------------------

@app.post("/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises")
def add_exercise_to_workout(workout_id, exercise_id):
    """Add an exercise to a workout with reps, sets, and duration"""
    workout = Workout.query.get(workout_id)
    exercise = Exercise.query.get(exercise_id)

    if not workout or not exercise:
        return make_response({"error": "Workout or Exercise not found"}, 404)

    try:
        data = request.get_json() or {}
        validated = workout_exercise_schema.load({
            **data,
            "workout_id": workout_id,
            "exercise_id": exercise_id
        })
    except Exception as e:
        return make_response({"error": str(e)}, 400)

    new_we = WorkoutExercise(**validated)
    db.session.add(new_we)
    db.session.commit()

    return make_response(workout_exercise_schema.dump(new_we), 201)


# ---------------------------
# Root / Healthcheck
# ---------------------------

@app.get("/")
def index():
    return make_response({"message": "Workout API is running"}, 200)


if __name__ == "__main__":
    app.run(port=5555, debug=True)