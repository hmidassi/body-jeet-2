from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

class Exercice(Base):
    __tablename__="EXERCICE"
    id_exercice = Column(Integer, primary_key=True)
    nom = Column(String)
    nb_reps_defaut=Column(Integer)
    id_categorie_exercice=Column(Integer, ForeignKey("categorie_exercice.id_categorie_exercice"))