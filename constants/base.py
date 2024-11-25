import os
from pathlib import Path

DB_NAME: str = "db.json"
BASE_DIR: Path = Path(__file__).resolve().parent.parent
DATABASE_FILE_PATH: str = os.path.join(BASE_DIR, DB_NAME)
