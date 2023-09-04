from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base

if __name__ == '__main__':

    engine = create_engine('sqlite:///restaurants.db')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    
    import ipdb; ipdb.set_trace()