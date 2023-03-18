from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class News(Base):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(String(1024), nullable=True)
    published_at = Column(DateTime, nullable=False)
    url = Column(String(255), nullable=False)
    cryptocurrency = Column(String(32), nullable=False)
    analyzed = Column(Boolean)

    def __repr__(self):
        return f"<News(id={self.id}, title={self.title}, published_at={self.published_at}, cryptocurrency={self.cryptocurrency})>"
