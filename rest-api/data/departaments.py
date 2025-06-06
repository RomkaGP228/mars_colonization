import sqlalchemy
import datetime
from .db_session import SqlAlchemyBase


class Departament(SqlAlchemyBase):
    __tablename__ = 'departament'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    chief = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    members = collaborators = sqlalchemy.Column(sqlalchemy.ARRAY, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey('users.email'))

