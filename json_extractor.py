# textutils/json_extractor.py

import re
import json

def extract_json_from_string(text):
    """
    Функция для извлечения всех JSON-объектов из строки.
    
    Аргументы:
    text (str): Входная строка, содержащая JSON-объекты.
    
    Возвращает:
    list: Список словарей, представляющих JSON-объекты.
    """
    # Регулярное выражение для поиска JSON между тройными кавычками ```json ... ```
    matches = re.findall(r'```json(.*?)```', text, re.DOTALL)

    json_objects = []
    for match in matches:
        try:
            # Удаляем пробелы и загружаем JSON
            json_obj = json.loads(match.strip())
            json_objects.append(json_obj)
        except json.JSONDecodeError:
            # Если JSON не может быть декодирован, просто продолжаем
            continue

    return json_objects
