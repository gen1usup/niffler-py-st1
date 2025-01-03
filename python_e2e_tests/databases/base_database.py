import os

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker


class BaseDatabase:
    def __init__(self, config):
        # Инициализация движка и сессии
        for key, value in config.items():
            setattr(self, key, value)
        self.db_url = f'postgresql://{self.user}:{self.password}@{self.host_in_docker}:{self.port}/{self.db_name}'
        self.engine = create_engine(self.db_url)
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        """Создает и возвращает новую сессию"""
        return self.Session()

    def add(self, instance):
        """Добавление записи в таблицу"""
        session = self.get_session()
        try:
            session.add(instance)
            session.commit()
            print(f"Запись {instance} успешно добавлена.")
        except Exception as e:
            session.rollback()
            print(f"Ошибка при добавлении записи: {e}")
        finally:
            session.close()

    def add_multiple(self, instances):
        """Добавление нескольких записей"""
        session = self.get_session()
        try:
            session.add_all(instances)
            session.commit()
            print(f"{len(instances)} записей успешно добавлено.")
        except Exception as e:
            session.rollback()
            print(f"Ошибка при добавлении записей: {e}")
        finally:
            session.close()

    def get_all(self, model_class):
        """Получение всех записей для указанной модели"""
        session = self.get_session()
        try:
            query = select(model_class)
            result = session.execute(query).scalars().all()
            return result
        except Exception as e:
            print(f"Ошибка при получении записей: {e}")
        finally:
            session.close()

    def get_by_id(self, model_class, record_id):
        """Получение записи по её ID"""
        session = self.get_session()
        try:
            instance = session.get(model_class, record_id)
            return instance
        except Exception as e:
            print(f"Ошибка при получении записи: {e}")
        finally:
            session.close()

    def delete_by_id(self, model_class, record_id):
        """Удаление записи по ID"""
        session = self.get_session()
        try:
            instance = session.get(model_class, record_id)
            if instance:
                session.delete(instance)
                session.commit()
                print(f"Запись с ID {record_id} успешно удалена.")
            else:
                print(f"Запись с ID {record_id} не найдена.")
        except Exception as e:
            session.rollback()
            print(f"Ошибка при удалении записи: {e}")
        finally:
            session.close()

    def update_instance(self, instance, updates):
        """Обновление существующей записи"""
        session = self.get_session()
        try:
            for key, value in updates.items():
                setattr(instance, key, value)
            session.commit()
            print(f"Запись {instance} успешно обновлена.")
        except Exception as e:
            session.rollback()
            print(f"Ошибка при обновлении записи: {e}")
        finally:
            session.close()









