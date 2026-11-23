"""Проверка обязательных полей учебного тест-кейса."""

REQUIRED = ("id", "title", "steps", "expected")


def validate_case(case):
    """Вернуть список отсутствующих или пустых обязательных полей."""
    return [key for key in REQUIRED if not case.get(key)]


def main():
    cases = [
        {
            "id": "TC-01",
            "title": "Открытие главной страницы",
            "steps": ["Открыть страницу приложения"],
            "expected": "Главная страница отображается",
        },
        {
            "id": "TC-02",
            "title": "Проверка пустого результата",
            "steps": ["Нажать кнопку поиска"],
            "expected": "",
        },
    ]
    for case in cases:
        missing = validate_case(case)
        result = "полный" if not missing else "нет полей: " + ", ".join(missing)
        print(f"{case['id']}: {result}")


if __name__ == "__main__":
    main()
