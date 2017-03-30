from app import app, db, models
from populate import get_houses, get_characters


if __name__ == "__main__":
    chars = models.Character.query.all()
    houses = models.House.query.all()
    for c in chars:
        db.session.delete(c)
    for h in houses:
        db.session.delete(h)
    get_houses()
    get_characters()
    app.run(debug=True)

