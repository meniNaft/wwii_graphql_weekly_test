from sqlalchemy.orm import declarative_base

Base = declarative_base()
from .country import Country
from .city import City
from .target_type import TargetType
from .target import Target
from .mission import Mission
