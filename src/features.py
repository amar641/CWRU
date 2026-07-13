import numpy as np


def extract_features(window):
    features = {}

    features["mean"] = np.mean(window)
    features["std"] = np.std(window)
    features["rms"] = np.sqrt(np.mean(window ** 2))

    return features

features = extract_features(windows[0])

print(features)