from python_e2e_tests.databases.base_database import BaseDatabase

from sqlalchemy import select

from python_e2e_tests.models.user_userdata import UserUserdata


class NifflerUserdataDB(BaseDatabase):
    def __init__(self, config):
        super().__init__(config)

    def add_user(self, user):
        session = self.get_session()
        try:
            session.add(user)
            session.commit()
            print(f"Пользователь {user.username} добавлен")
        except Exception as e:
            session.rollback()
            print(f"Ошибка при добавлении пользователя: {e}")
        finally:
            session.close()

    def get_all_users(self):
        session = self.get_session()
        try:
            query = select(UserUserdata)
            result = session.execute(query).scalars().all()
            return result
        except Exception as e:
            print(f"Ошибка при получении пользователей: {e}")
        finally:
            session.close()

    def get_user_by_id(self, user_id):
        session = self.get_session()
        try:
            user = session.get(UserUserdata, user_id)
            return user
        except Exception as e:
            print(f"Ошибка при получении пользователя: {e}")
        finally:
            session.close()

    def delete_user(self, user_id):
        session = self.get_session()
        try:
            user = session.get(UserUserdata, user_id)
            if user:
                session.delete(user)
                session.commit()
                print(f"Пользователь с ID {user_id} удален")
            else:
                print(f"Пользователь с ID {user_id} не найден")
        except Exception as e:
            session.rollback()
            print(f"Ошибка при удалении пользователя: {e}")
        finally:
            session.close()