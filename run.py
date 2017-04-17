from app import app as application, db, models
from populate import get_houses

if __name__ == "__main__":
    	application.run(debug=True)

