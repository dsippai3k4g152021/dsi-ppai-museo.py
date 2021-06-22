from sqlalchemy.orm import sessionmaker

from utilitarios.Connection import engine
from utilitarios.Singletons import Singletons


class DBSession(metaclass=Singletons):
    session = sessionmaker(engine)
    session = session()

    def get_db_session(self):
        return self.session
