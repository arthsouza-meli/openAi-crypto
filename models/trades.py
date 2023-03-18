from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Trades(Base):
    __tablename__ = 'trades'

    id = Column(Integer, primary_key=True)
    buy_order_id = Column(String(255))
    sell_order_id = Column(String(255))
    symbol = Column(String(255))
    buy_price = Column(Float)
    sell_price = Column(Float)
    quantity = Column(Float)
    profit = Column(Float)
    fee = Column(Float)
    date = Column(DateTime)

    def __repr__(self):
        return f"<Trades(id={self.id}, symbol='{self.symbol}', buy_price={self.buy_price}, sell_price={self.sell_price}, quantity={self.quantity}, profit={self.profit}"
