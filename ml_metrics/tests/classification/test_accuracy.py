import pytest
import numpy as np
from ml_metrics.classification.accuracy import accuracy_score

def test_accuracy_score():
    y_true = [0, 1, 2, 3]
    y_pred = [0, 2, 1, 3]
    assert accuracy_score(y_true, y_pred) == 0.5

    y_true = [0, 0, 1, 1]
    y_pred = [0, 0, 1, 1]
    assert accuracy_score(y_true, y_pred) == 1.0

    with pytest.raises(ValueError):
        accuracy_score([0, 1], [0, 1, 2])
