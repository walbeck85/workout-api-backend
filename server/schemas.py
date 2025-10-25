# server/schemas.py

from marshmallow import Schema, fields, validates, ValidationError

# NOTE:
# We are intentionally not importing db/models here.
# Schemas should describe shape and rules. In the next step,
# the routes will import both models and these schemas together.

class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    workout_id = fields.Int(required=True)
    exercise_id = fields.Int(required=True)
    reps = fields.Int(allow_none=True)
    sets = fields.Int(allow_none=True)
    duration_seconds = fields.Int(allow_none=True)

    @validates("reps")
    def validate_reps(self, value):
        # schema validation: reps must be >= 0
        if value is not None and value < 0:
            raise ValidationError("reps must be non-negative")

    @validates("sets")
    def validate_sets(self, value):
        # schema validation: sets must be >= 0
        if value is not None and value < 0:
            raise ValidationError("sets must be non-negative")

    @validates("duration_seconds")
    def validate_duration_seconds(self, value):
        # schema validation: duration_seconds must be >= 0
        if value is not None and value < 0:
            raise ValidationError("duration_seconds must be non-negative")


class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str()
    equipment_needed = fields.Bool(required=True)

    # nested workouts shown on GET /exercises/<id>
    # We don't include all join fields here, just high-level workout info
    workouts = fields.List(
        fields.Nested(
            lambda: WorkoutSchema(exclude=("exercises", "workout_exercises"))
        ),
        dump_only=True
    )

    @validates("name")
    def validate_name(self, value):
        # schema validation: non-empty string
        if not value or value.strip() == "":
            raise ValidationError("Exercise name cannot be empty.")


class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date(required=True)
    duration_minutes = fields.Int(required=True)
    notes = fields.Str(allow_none=True)

    # For GET /workouts and GET /workouts/<id>, we want to be able to show:
    # - exercises (high-level info)
    # - optionally the join info (reps/sets/duration)
    exercises = fields.List(
        fields.Nested(
            lambda: ExerciseSchema(exclude=("workouts",))
        ),
        dump_only=True
    )

    workout_exercises = fields.List(
        fields.Nested(WorkoutExerciseSchema),
        dump_only=True
    )

    @validates("duration_minutes")
    def validate_duration_minutes(self, value):
        # schema validation: duration_minutes must be > 0
        if value is None or value <= 0:
            raise ValidationError("Workout duration must be positive.")