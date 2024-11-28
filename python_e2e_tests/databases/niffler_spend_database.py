from sqlalchemy import select
from sqlalchemy.orm import joinedload

from python_e2e_tests.databases.base_database import BaseDatabase
from python_e2e_tests.models.category import Category
from python_e2e_tests.models.spend import Spend


class NifflerSpendDB(BaseDatabase):
    def __init__(self, config):
        super().__init__(config)

    # Методы для работы с таблицей Category
    def add_category(self, category_name, username):
        """Добавление новой категории"""
        session = self.get_session()
        try:
            new_category = Category(category=category_name, username=username)
            session.add(new_category)
            session.commit()
            print(f"Категория {category_name} успешно добавлена.")
        except Exception as e:
            session.rollback()
            print(f"Ошибка при добавлении категории: {e}")
        finally:
            session.close()

    def get_all_categories(self):
        """Получение всех категорий"""
        session = self.get_session()
        try:
            query = select(Category)
            categories = session.execute(query).scalars().all()
            return categories
        except Exception as e:
            print(f"Ошибка при получении категорий: {e}")
        finally:
            session.close()

    # Методы для работы с таблицей Spend
    def add_spend(self, username, spend_date, currency, amount, description, category_id):
        """Добавление новой записи о расходе"""
        session = self.get_session()
        try:
            new_spend = Spend(
                username=username,
                spend_date=spend_date,
                currency=currency,
                amount=amount,
                description=description,
                category_id=category_id
            )
            session.add(new_spend)
            session.commit()
            print(f"Расход в размере {amount} {currency} успешно добавлен.")
        except Exception as e:
            session.rollback()
            print(f"Ошибка при добавлении расхода: {e}")
        finally:
            session.close()

    def get_spend_by_category(self, category_id):
        """Получение всех расходов по категории"""
        session = self.get_session()
        try:
            query = select(Spend).where(Spend.category_id == category_id).options(joinedload(Spend.category))
            spend = session.execute(query).scalars().all()
            return spend
        except Exception as e:
            print(f"Ошибка при получении расходов по категории: {e}")
        finally:
            session.close()

    def get_spend_by_user(self, username):
        """Получение всех расходов по пользователю"""
        session = self.get_session()
        try:
            query = select(Spend).where(Spend.username == username).options(joinedload(Spend.category))
            spend = session.execute(query).scalars().all()
            return spend
        except Exception as e:
            print(f"Ошибка при получении расходов пользователя {username}: {e}")
        finally:
            session.close()

    def delete_Spend_by_id(self, Spend_id):
        """Удаление записи о расходе по её ID"""
        session = self.get_session()
        try:
            spend = session.get(Spend, Spend_id)
            if spend:
                session.delete(spend)
                session.commit()
                print(f"Запись о расходе с ID {Spend_id} успешно удалена.")
            else:
                print(f"Запись о расходе с ID {Spend_id} не найдена.")
        except Exception as e:
            session.rollback()
            print(f"Ошибка при удалении записи о расходе: {e}")
        finally:
            session.close()
