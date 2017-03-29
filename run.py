from app import app, db, models
from populate import get_characters

if __name__ == "__main__":
    app.run(debug=True)
