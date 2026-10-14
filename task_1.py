"""Практическое занятие № 8, вариант 11, задача 1."""

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york",
}

print("Исходный словарь:", sample_dict)

# Перенос значения из старого ключа в новый.
if "city" in sample_dict:
    sample_dict["location"] = sample_dict.pop("city")

print("Изменённый словарь:", sample_dict)
