"""fast_api models."""
from fast_api.db.models.dummy_model import DummyModel
from fast_api.db.models.models import User, Weather,Base
import pkgutil
from pathlib import Path


def load_all_models() -> None:
    """Load all models from this folder."""
    package_dir = Path(__file__).resolve().parent
    modules = pkgutil.walk_packages(
        path=[str(package_dir)],
        prefix="fast_api.db.models.",
    )
    for module in modules:
        __import__(module.name)
