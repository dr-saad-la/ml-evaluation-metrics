import numpy as np
from numpy.typing import ArrayLike

def accuracy_score(y_true: ArrayLike, y_pred: ArrayLike) -> float:
    """
    Calculate accuracy classification score.

    Parameters
    ----------
    y_true : array-like
        Ground truth (correct) labels
    y_pred : array-like
        Predicted labels

    Returns
    -------
    float
        Accuracy score

    Examples
    --------
    >>> y_true = [0, 1, 2, 3]
    >>> y_pred = [0, 2, 1, 3]
    >>> accuracy_score(y_true, y_pred)
    0.5
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    if y_true.shape != y_pred.shape:
        raise ValueError("y_true and y_pred must have the same shape")

    return np.mean(y_true == y_pred)
