from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from socle.sessionMaker import *
from sqlalchemy.orm import *

Base = declarative_base()



class CategorieExerciceManager(object):
    sessionBuilder=SessionBuilder()
    session=sessionBuilder.session_scope()
    def __init__(self,type):

        self.type=type






    def create(self,entity):

        return entity

    def update(self,entity):
        return entity

    def delete(self,entity):
        return None

    def getById(self,id):
        with self.sessionBuilder.session_scope() as session:
            return session.query(self.type).get(id)