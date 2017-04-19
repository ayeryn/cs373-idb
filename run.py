from app import app as application, db, models
from populate import get_episodes

if __name__ == "__main__":
    # oldies = models.Episode.query.all()
    # for o in oldies:
    # 	db.session.delete(o)
    # db.session.commit()
    # get_episodes()
    application.run(debug=True)

