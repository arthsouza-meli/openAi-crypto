from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class HistoricalPrices(Base):
    __tablename__ = 'historical_prices'

    id = Column(Integer, primary_key=True)
    cryptocurrency = Column(String(50), nullable=False)
    date = Column(DateTime, nullable=False)
    open = Column(Float, nullable=False)
    high = Column(Float, nullable=False)
    low = Column(Float, nullable=False)
    close = Column(Float, nullable=False)
    volume = Column(Float, nullable=False)

    def __repr__(self):
        return f"<HistoricalPrices(id={self.id}, cryptocurrency='{self.cryptocurrency}', date='{self.date}', open={self.open}, high={self.high}, low={self.low}, close={self.close}, volume={self.volume})>"
