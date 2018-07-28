from persistence.entities.genericEntity import *


class Exercice(GenericEntity):
    tablename="EXERCICE"
    id_exercice = Column(Integer, primary_key=True)
    nom = Column(String)
    nb_reps_defaut=Column(Integer)
    id_categorie_exercice=Column(Integer, foreign_key="categorie_exercice.id_categorie_exercice")