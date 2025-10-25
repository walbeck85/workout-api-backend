from flask import Flask, request, jsonify, make_response
from flask_migrate import Migrate
from server.models import db, Workout, Exercise, WorkoutExercise

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

# ---------------------------
# Workouts routes
# ---------------------------

@app.get("/workouts")
def get_workouts():
    # List all workouts
    return make_response(jsonify({"message": "GET /workouts placeholder"}), 200)

@app.get("/workouts/<int:workout_id>")
def get_workout_by_id(workout_id):
    # Show a single workout (optionally include its exercises + reps/sets/duration)
    return make_response(jsonify({
        "message": "GET /workouts/<id> placeholder",
        "workout_id": workout_id
    }), 200)

@app.post("/workouts")
def create_workout():
    # Create a workout
    return make_response(jsonify({"message": "POST /workouts placeholder"}), 201)

@app.delete("/workouts/<int:workout_id>")
def delete_workout(workout_id):
    # Delete a workout (stretch goal: delete related WorkoutExercise rows)
    return make_response(jsonify({
        "message": "DELETE /workouts/<id> placeholder",
        "workout_id": workout_id
    }), 204)

# ---------------------------
# Exercises routes
# ---------------------------

@app.get("/exercises")
def get_exercises():
    # List all exercises
    return make_response(jsonify({"message": "GET /exercises placeholder"}), 200)

@app.get("/exercises/<int:exercise_id>")
def get_exercise_by_id(exercise_id):
    # Show an exercise and associated workouts
    return make_response(jsonify({
        "message": "GET /exercises/<id> placeholder",
        "exercise_id": exercise_id
    }), 200)

@app.post("/exercises")
def create_exercise():
    # Create an exercise
    return make_response(jsonify({"message": "POST /exercises placeholder"}), 201)

@app.delete("/exercises/<int:exercise_id>")
def delete_exercise(exercise_id):
    # Delete an exercise (stretch goal: delete related WorkoutExercise rows)
    return make_response(jsonify({
        "message": "DELETE /exercises/<id> placeholder",
        "exercise_id": exercise_id
    }), 204)

# ---------------------------
# Add Exercise to Workout
# ---------------------------

@app.post("/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises")
def add_exercise_to_workout(workout_id, exercise_id):
    # Add an exercise to a workout with reps/sets/duration data
    return make_response(jsonify({
        "message": "POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises placeholder",
        "workout_id": workout_id,
        "exercise_id": exercise_id
    }), 201)

# ---------------------------
# Entry point for direct run
# ---------------------------

if __name__ == "__main__":
    app.run(port=5555, debug=True)