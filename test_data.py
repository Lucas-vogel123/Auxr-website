from models import *
from database import init_db, db_session

init_db()
user = Ambassador("lucasvogel1050@gmail.com", "12345")
db_session.add(user)
db_session.commit()