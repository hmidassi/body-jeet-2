from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


Base=declarative_base()


class CategorieExercice(Base):
        __tablename__="CATEGORIE_EXERCICE"

        id_categorie_exercice=Column(Integer, primary_key=True)
        nom=Column(String)

