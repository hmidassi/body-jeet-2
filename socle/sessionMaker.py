from sqlalchemy.orm import Session,Query,sessionmaker
from sqlalchemy import create_engine
from contextlib import contextmanager



engine=create_engine('sqlite:///dbAppliBodyJeet')

class SessionBuilder(object):
    session=Session()

    @contextmanager
    def session_scope(self):
        session = sessionmaker()
        sess=Session()
        session=session.configure(bind=engine)
        try:
            yield session
            sess.commit()
        except:
            sess.rollback()
            raise
        finally:
            sess.close()


