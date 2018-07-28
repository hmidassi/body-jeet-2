from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base=declarative_base()


class GenericEntity(Base):
    __tablename__=""


    def equals(self, obj):
        if not isinstance(obj,GenericEntity):
            return False
        else:
            for attr,value in self.__dict__.items():
                for attr2,value2 in obj.__dict__.items():
                    if attr==attr2 and value!=value2:
                        return False
            return True

