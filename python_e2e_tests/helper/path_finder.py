from pathlib import Path
import os

def find_project_root(current_path: Path, file_in_root: str = 'requirements.txt') -> Path:
    """
    Ищет корень проекта, поднимаясь вверх по дереву директорий, пока не найдет указанный маркер.
    """
    for parent in current_path.parents:
        if (parent / file_in_root).exists():
            return parent
    raise FileNotFoundError(f"Маркер '{file_in_root}' не найден в дереве директорий от {current_path}")

def get_path_to_file(filename: str, file_in_root: str = 'requirements.txt') -> Path:
    """
    Возвращает полный путь до файла относительно корня проекта, идентифицированного маркером.
    """
    # Определяем путь до текущего файла
    current_file = Path(__file__).resolve()

    # Определяем путь до корневой директории проекта
    project_root = find_project_root(current_file, file_in_root)

    # Ищем файл в корневой директории и всех подкаталогах
    for root, dirs, files in os.walk(project_root):
        for file in files:
            if file == filename:
                return Path(root) / file

    raise FileNotFoundError(f"Файл '{filename}' не найден в проекте.")

# Пример использования
# filename = 'lk2_methods.py'  # замените на имя нужного файла
# try:
#     file_path = get_full_path_from_project_root(filename)
#     print(file_path)
# except FileNotFoundError as e:
#     print(e)
