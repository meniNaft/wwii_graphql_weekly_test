from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.models import Base


class Target(Base):
    __tablename__ = "targets"
    target_id = Column(Integer, primary_key=True, autoincrement=True)
    target_industry = Column(String, nullable=False)
    target_priority = Column(Integer)
    city_id = Column(Integer, ForeignKey("cities.city_id"))
    city = relationship("City", back_populates="targets")
    mission_id = Column(Integer, ForeignKey("missions.mission_id"))
    mission = relationship("Mission", uselist=False, back_populates="target")
    target_type_id = Column(Integer, ForeignKey("targettypes.target_type_id"))
    target_type = relationship("TargetType", back_populates="targets")  #


