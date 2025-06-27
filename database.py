import sqlalchemy as sa
from sqlalchemy.orm import DeclarativeBase, Mapped, sessionmaker, mapped_column

db = sa.create_engine("sqlite:///db/shrt_urls.sqlite")
Session = sessionmaker(bind=db)

class Base(DeclarativeBase):
    pass

class Urls(Base):
    __tablename__ = 'urls'

    id: Mapped[int] = mapped_column(primary_key=True)
    short_url: Mapped[str]
    original_url: Mapped[str]

Base.metadata.create_all(db)
