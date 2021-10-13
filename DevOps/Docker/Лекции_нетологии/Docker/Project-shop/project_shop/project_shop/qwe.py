import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_ROOT = os.path.join(BASE_DIR, 'project_shop/static/')
w = 0