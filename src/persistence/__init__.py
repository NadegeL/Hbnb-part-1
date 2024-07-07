#src/persistence/init.py:
import os
from utils.constants import REPOSITORY_ENV_VAR

# Default repository if no environment variable is set
default_repo = "memory"

def get_repository():
    repo_type = os.getenv(REPOSITORY_ENV_VAR, default_repo).lower()
    if repo_type == "db":
        from src.persistence.db import DBRepository
        return DBRepository()
    elif repo_type == "file":
        from src.persistence.file import FileStorage
        return FileStorage()
    elif repo_type == "pickle":
        from src.persistence.pickled import PickleRepository
        return PickleRepository()
    elif repo_type == "memory":
        from src.persistence.memory import MemoryRepository
        return MemoryRepository()
    else:
        raise ValueError(f"Unsupported repository type: {repo_type}")

try:
    repo = get_repository()
    print(f"Using {repo.__class__.__name__} as repository")
except ValueError as e:
    print(e)
    raise SystemExit(f"Failed to initialize repository due to an error: {e}")
