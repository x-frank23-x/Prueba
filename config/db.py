from sqlalchemy import create_engine, MetaData


DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://postgres:tu_password@localhost:5432/alarms_db",
)

engine= create_engine(DATABASE_URL)

meta = MetaData()