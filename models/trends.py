from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Trends(Base):
    __tablename__ = 'trends'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, nullable=False)
    trend = Column(String(10), nullable=False)  # 'subir' or 'descer'


    def __repr__(self):
        return f"<Trends(id={self.id}, timestamp='{self.timestamp}', trend='{self.trend}') , sentiment_score={self.sentiment_score}>"
