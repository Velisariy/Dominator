# Доминатор — вычисление доминирующих цветов изображений

## Архитектура

```
start.py                  # ВХОД: консольный launcher, создаёт QApplication
├─ core/
│  ├─ core.py             # алгоритм: k-means clustering RGB из пикселей PIL
│  └─ design.py           # PyQt5 UI, иконки icons/, html из hello.html
└─ requirements.txt       # зависимости
```

## Запуск

```bash
python start.py
# или через pipenv/poetry — указать их если есть
```

## Критичные зависимости

**Иметь перед запуском:**
- `Pillow` (Image) — `PIL.Image.open()` для декодинга изображений
- `PyQt5` — UI (`QMainWindow`, `QThread`, `QPixmap`)
- `reportlab` (опц.) — экспорт в PDF, проверяется импортом
- `cx_Freeze` в `setup.py` — сборка standalone .exe

## Короткие команды для dev

```bash
# single test (если есть тесты) — пока нет, запускаем UI один раз:
python start.py

# собрать для Windows:
python setup.py build
```

## Локализация

UI на русском, иконки: `icons/fileopen.png`, `icons/save.png`, `icons/refresh.png`, `icons/exit.png`, `icons/icon.png` — должны лежать рядом с root.

## Тесты/CI

Не реализовано. Добавить `pytest` + `tox` если требуется. Пока только ручная проверка запуска в браузере/терминале.
