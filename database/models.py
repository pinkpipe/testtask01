from db import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True, index=True)
    name_person = Column(String, unique=True, nullable=False)
    birth_date = Column(DateTime, nullable=False)
    phone_number = Column(String, nullable=False, unique=True)
    med_card = Column(Integer, nullable=False, unique=True)
    inn = Column(Integer, nullable=False, unique=True)

    is_patient = Column(Boolean, nullable=False, default=False)
    is_employee = Column(Boolean, nullable=False, default=False)


from sqlalchemy.schema import CreateTable
print(CreateTable(Person.__table__))
