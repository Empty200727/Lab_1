import importlib
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


@pytest.fixture
def task():
    """Фикстура-загрузчик: task('05_zoo') возвращает модуль задания."""
    def _load(name):
        return importlib.import_module(f'python_lab_01.{name}')
    return _load
