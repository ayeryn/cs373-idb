from app import app as application, db, models
from populate import get_houses

if __name__ == "__main__":
    # oldies = models.House.query.all()
    # for o in oldies:
    # 	db.session.delete(o)
    # db.session.commit()
    # get_houses()
    application.run(debug=True)

