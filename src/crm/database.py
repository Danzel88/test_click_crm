from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from crm.settings import setting

engine = create_engine(setting.database_url,
                       # echo=True,
                       )


Session = sessionmaker(
    engine,
    autocommit=False,
    autoflush=False)


def get_session() -> Session:
    session = Session()
    try:
        yield session
    finally:
        session.close()
