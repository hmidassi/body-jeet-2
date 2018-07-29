from persistence.entities import CategorieExercice,Exercice
from persistence.managers import CategorieExerciceEntityManager
from sqlalchemy.orm import Session,Query,sessionmaker
from sqlalchemy import create_engine


entityManager=CategorieExerciceEntityManager.CategorieExerciceManager(CategorieExercice.CategorieExercice)
engine=create_engine('sqlite:///dbAppliBodyJeet')
conn=engine.connect()
Session = sessionmaker(bind=engine)
sess=Session()

sess.query(CategorieExercice.CategorieExercice).get(1)

categorie=sess.query(Exercice.Exercice).get(3)
print(categorie.nom)
