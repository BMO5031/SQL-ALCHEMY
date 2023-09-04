from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.associationproxy import association_proxy

Base=declarative_base()

class Restaurant(Base):
    __tablename__='restaurants'

    id=Column(Integer(),primary_key=True)
    name=Column(String())
    price=Column(Integer())
    reviews = relationship('Review', back_populates='restaurant')
    customers=association_proxy('reviews','customer',creator=lambda us: Review(customer=us))

class Customer(Base):
    __tablename__='customers'

    id=Column(Integer(),primary_key=True)
    first_name=Column(String())
    last_name=Column(String())
    reviews = relationship('Review', back_populates='customer')
    restaurants=association_proxy('reviews','restaurant',creator=lambda gm: Review(customer=gm))


class Review(Base):
    __tablename__='reviews'

    id=Column(Integer(),primary_key=True)
    comment=Column(String())
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))

    restaurant=relationship("Restaurant",back_populates='reviews')
    customer=relationship("Customer",back_populates='reviews')