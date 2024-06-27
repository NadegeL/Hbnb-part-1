# src/persistence/__init__.py

import os
from utils.constants import REPOSITORY_ENV_VAR

from src.persistence.repository import Repository

repo: Repository

if os.getenv(REPOSITORY_ENV_VAR) == "db":
    from src.persistence.db import DBRepository
    repo = DBRepository()
elif os.getenv(REPOSITORY_ENV_VAR) == "file":
    from src.persistence.file import FileStorage
    repo = FileStorage()
elif os.getenv(REPOSITORY_ENV_VAR) == "pickle":
    from src.persistence.pickled import PickleRepository
    repo = PickleRepository()
else:
    from src.persistence.memory import MemoryRepository
    repo = MemoryRepository()

print(f"Using {repo.__class__.__name__} as repository")
