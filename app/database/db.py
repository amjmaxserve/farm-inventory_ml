from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import (
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    POSTGRES_HOST,
    POSTGRES_PORT,
    POSTGRES_DB
)

DATABASE_URL = (
    f"postgresql://"
    f"{POSTGRES_USER}:"
    f"{POSTGRES_PASSWORD}@"
    f"{POSTGRES_HOST}:"
    f"{POSTGRES_PORT}/"
    f"{POSTGRES_DB}"
)

print("\n===== DATABASE DEBUG =====")
print(f"POSTGRES_USER={POSTGRES_USER}")
print(f"POSTGRES_HOST={POSTGRES_HOST}")
print(f"POSTGRES_PORT={POSTGRES_PORT}")
print(f"POSTGRES_DB={POSTGRES_DB}")
print(f"DATABASE_URL={DATABASE_URL}")
print("==========================\n")




engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()