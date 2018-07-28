from persistence.entities.genericEntity import GenericEntity
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from socle.sessionMaker import *
from sqlalchemy.orm import *

Base = declarative_base()



class GenericEntityManager(object):
    sessionBuilder=SessionBuilder()
    session=sessionBuilder.session_scope()
    def __init__(self,type):
        if(issubclass(type,GenericEntity)):
            self.type=type


        else:
            raise TypeError("Un manager doit obligatoirement correspondre à une entité, merci de vérifier votre code")
        engine=create_engine



    def create(self,entity):

        return entity

    def update(self,entity):
        return entity

    def delete(self,entity):
        return None

    def getById(self,id):
        with self.sessionBuilder.session_scope() as session:
            return session.Query(self.type).get(id)

