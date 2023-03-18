from sqlalchemy.orm import sessionmaker
from models import Base
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_DATABASE, DB_PORT

class Database:
    def __init__(self):
        if not all([DB_HOST, DB_USER, DB_PASSWORD, DB_DATABASE]):
            raise ValueError("Variáveis de ambiente para conexão com o banco de dados não foram configuradas.")

        self.engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}?charset=utf8mb4", echo=False)
        self.metadata = MetaData()
        self.Session = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)
