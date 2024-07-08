from database import engine ,Base
from models import User,Category,Books,Book_Author,Author,Review

Base.metadata.create_all(bind=engine)               