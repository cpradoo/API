from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from modelos.base import Base


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    userId = Column(Integer, nullable=False)
    title = Column(String(255), nullable=False)
    body = Column(Text, nullable=False)
    comments = relationship("Comment", backref="post")


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    postId = Column(Integer, ForeignKey('posts.id'))
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    body = Column(Text, nullable=False)


class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)
    contrasena = Column(String(255), nullable=False)