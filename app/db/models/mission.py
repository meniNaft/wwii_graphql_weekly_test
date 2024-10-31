from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.models import Base


class Mission(Base):
    __tablename__ = "missions"
    mission_id = Column(Integer, primary_key=True, autoincrement=True)
    mission_date = Column(Date)
    airborne_aircraft = Column(Integer, nullable=True)
    attacking_aircraft = Column(Integer, nullable=True)
    bombing_aircraft = Column(Integer, nullable=True)
    aircraft_returned = Column(Integer, nullable=True)
    aircraft_failed = Column(Integer, nullable=True)
    aircraft_damaged = Column(Integer, nullable=True)
    aircraft_lost = Column(Integer, nullable=True)
    target = relationship("Target", uselist=False, cascade="all,delete", back_populates="mission")
