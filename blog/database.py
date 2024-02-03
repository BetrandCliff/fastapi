from sqlalchemy import create_engine
from sqlalchemy.ext.decorative import declarative_base
from sqlalchemy.orm import sessionmaker

-
SQLCHEMY_DATABASE_URL ="sqlite:///./blog.db:"
ARGUMENT ="check_Same_thread"

engine = create_engine(SQLCHEMY_DATABASE_URL,connect_args={ARGUMENT:False})


sessionLocal = sessionmaker(bind=engine,autocommit=False, autoflush=False)


Base = declarative_base()