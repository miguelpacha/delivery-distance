from sqlalchemy import Column, Integer, String, Float

from app.db import Base, engine


class SearchItem(Base):
    __tablename__ = "search_item"
    id = Column(Integer, primary_key=True)
    origin = Column(String(30))
    destination = Column(String(30))
    distance = Column(Float())
    
    def __repr__(self):
        return f"SearchItem(id={self.id!r}, origin={self.origin!r}, destination={self.destination!r})"

Base.metadata.create_all(engine)
