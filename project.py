# Project: commercial web application
# Program prints the project team and developers' surnames

PROJECT_NAME = "Розробка комерційного вебдодатку"

# Team members: (surname, name, role, project stage)
team = [
    ("Зозуля",    "Діма",    "Team Lead / Аналітик", "Аналіз вимог"),
    ("Прізвище2", "Ім'я2",   "UI/UX-дизайнер",       "Дизайн UI/UX"),
    ("Прізвище3", "Ім'я3",   "Backend-розробник",    "Backend-розробка"),
    ("Прізвище4", "Ім'я4",   "QA-інженер",           "Тестування"),
    ("Прізвище5", "Ім'я5",   "DevOps-інженер",       "Деплой"),
]


def print_team(members):
    """Print the team as a formatted table."""
    print("=" * 70)
    print(f"Проєкт: {PROJECT_NAME}".center(70))
    print("=" * 70)
    print(f"{'№':<3}{'Прізвище та ім’я':<22}{'Роль':<24}{'Етап проєкту'}")
    print("-" * 70)
    for i, (surname, name, role, stage) in enumerate(members, start=1):
        print(f"{i:<3}{surname + ' ' + name:<22}{role:<24}{stage}")
    print("-" * 70)
    print(f"Усього учасників команди: {len(members)}")


def print_surnames(members):
    """Print only the developers' surnames."""
    surnames = sorted(m[0] for m in members)
    print("\nПрізвища розробників (за алфавітом):")
    print(", ".join(surnames))


if __name__ == "__main__":
    print_team(team)
    print_surnames(team)