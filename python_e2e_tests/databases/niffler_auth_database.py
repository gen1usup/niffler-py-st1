from python_e2e_tests.databases.base_database import BaseDatabase

from sqlalchemy import select

from python_e2e_tests.models.user_auth import UserAuth, Authority


class NifflerAuthDB(BaseDatabase):
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
            query = select(UserAuth)
            result = session.execute(query).scalars().all()
            return result
        except Exception as e:
            print(f"Ошибка при получении пользователей: {e}")
        finally:
            session.close()

    def get_user_by_id(self, user_id):
        session = self.get_session()
        try:
            user = session.get(UserAuth, user_id)
            return user
        except Exception as e:
            print(f"Ошибка при получении пользователя: {e}")
        finally:
            session.close()

    def delete_user(self, user_id):
        session = self.get_session()
        try:
            user = session.get(UserAuth, user_id)
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

    def delete_user_data_by_username(self, username):
        user_id = self.get_session().query(UserAuth.id).filter(UserAuth.username == username).scalar()
        authority_ids = self.get_session().query(Authority.id).filter(Authority.user_id == user_id).all()
        for authority_id in authority_ids:
            self.delete_by_id(Authority, authority_id)
        self.delete_by_id(UserAuth, user_id)