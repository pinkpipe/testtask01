from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Создаем базовый класс для декларативных моделей
Base = declarative_base()


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


# Создание движка базы данных
engine = create_engine('postgresql://ama_user:12345@localhost/test_db', echo=True)

# Создание таблиц в базе данных
Base.metadata.create_all(engine)

# Создание сессии
SessionLocal = sessionmaker(bind=engine)


# Функция для добавления нового человека
def add_person(session, person_data):
    try:
        new_person = Person(**person_data)
        session.add(new_person)
        session.commit()
        logger.info(f"Person added successfully: {person_data['name_person']}")
    except Exception as e:
        session.rollback()
        logger.error(f"Failed to add person: {person_data['name_person']}. Error: {e}")


# Данные для добавления
person_data1 = {
    'name_person': 'Дмитриев К.А',
    'birth_date': datetime(1998, 10, 5),
    'phone_number': '+7 999 111 22 00',
    'med_card': 12345,
    'inn': 10,
    'is_employee': True
}

person_data2 = {
    'name_person': 'Жужов А.А',
    'birth_date': datetime(1990, 11, 5),
    'phone_number': '+7 999 111 33 00',
    'med_card': 6543,
    'inn': 40,
    'is_patient': True
}

# Добавление объектов в базу данных
with SessionLocal() as session:
    add_person(session, person_data1)
    add_person(session, person_data2)
