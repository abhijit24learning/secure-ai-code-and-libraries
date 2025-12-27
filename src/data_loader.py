"""Data loading module - VULNERABLE VERSION"""
import pickle
from urllib.request import urlopen

class ModelLoader:
    # ⚠️ B301: Unsafe pickle.loads() - RCE vulnerability
    def load_model_from_url(self, model_url):
        """Load ML model from untrusted URL using pickle"""
        data = urlopen(model_url).read()
        # This can execute arbitrary Python code!
        model = pickle.loads(data)
        return model

    # ⚠️ B301: Unsafe pickle.load() - Deserialization vulnerability
    def load_training_data(self, filepath):
        """Load training data from pickle file"""
        with open(filepath, 'rb') as f:
            data = pickle.load(f)  # Can execute arbitrary code
        return data
