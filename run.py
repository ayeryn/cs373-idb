from app import app as application, db, models
from populate import get_alc

if __name__ == "__main__":
    # oldies = models.Episode.query.all()
    # for o in oldies:
    # 	db.session.delete(o)
    # db.session.commit()
    application.run(debug=True)

