# PROJECT_ROOT = "digits_recogntion/"
# MODEL_PATH = PROJECT_ROOT + "models/random_forest_mnist_model.pkl"
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]
MODEL_PATH = BASE_DIR / "models" / "random_forest_mnist.pkl"