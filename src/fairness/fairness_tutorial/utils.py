from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import pandas as pd
import numpy as np


def predict_with_threshold(probabilities, threshold):
    """
    preidct classification class based on threshold t.
    @propabilities: classification propabilities of positive class.
    @threshold: classification threshold.
    """
    # clalculate the prediction based on the propabilities and thresholds.
    # hint: use pandas masking to effintiantly calculate predictions.
    prediction = (probabilities >= threshold) * 1
    return prediction


def compute_metric(y_pred, y_true, sensitive_feature):
    conf_matrix = confusion_matrix(y_true=y_true,
                                   y_pred=y_pred)
    conf_matrix = pd.DataFrame(conf_matrix)

    TN, FP, FN, TP = conf_matrix.values.ravel()

    acc_score = (TN + TP) / (TN + FP + FN + TP)
    precision_score = TP / (TP + FP)
    recall_score = TP / (TP + FN)
    f1_score = 2 * (precision_score * recall_score) / (precision_score + recall_score)

    demographic_metric, _ = demographic_parity_difference(y_pred,
                                                          sensitive_feature)

    equalized_opportunities_metric, _ = equalized_opportunities_difference(y_pred,
                                                                           y_true,
                                                                           sensitive_feature)
    equalized_odds_metrics, _ = equalized_odds_difference(y_pred,
                                                          y_true,
                                                          sensitive_feature)

    return {
        "accuracy": acc_score,
        "precision": precision_score,
        "recall": recall_score,
        "f1_score": f1_score,
        "demographic_metric": demographic_metric,
        "equalized_opportunities": equalized_opportunities_metric,
        "equalized_odds": equalized_odds_metrics
    }


def equalized_odds_difference(predictions, actual, sensitive_attribute):
    """
    Implementation of equalized odds difference for different groups of sensitive attribute
    1. For each group calculate the TPR.
    2. Find the maximum and the minim group.
    3. Calcaulte the difference.
    """
    # 1. For each group calculate the TPR.
    unique_groups = np.sort(sensitive_attribute.unique())
    true_positive_rates = []
    false_positive_rates = []
    for group in unique_groups:
        pred_group = predictions[sensitive_attribute == group]
        actual_group = actual[sensitive_attribute == group]
        conf_matrix = confusion_matrix(y_true=actual_group,
                                       y_pred=pred_group)
        TN, FP, FN, TP = conf_matrix.ravel()

        true_positive_rate = TP / (TP + FN)
        false_positive_rate = FP / (FP + TN)

        true_positive_rates += [true_positive_rate]
        false_positive_rates += [false_positive_rate]

    # 2. Find the maximum and the minimum accepted_rate.
    maximum_tpr = max(true_positive_rates)
    minimum_tpr = min(true_positive_rates)

    maximum_fpr = max(false_positive_rates)
    minimum_fpr = min(false_positive_rates)

    # 3. Calculate the different.
    difference_tpr = maximum_tpr - minimum_tpr
    difference_fpr = maximum_fpr - minimum_fpr
    difference = difference_tpr + difference_fpr

    return difference, (true_positive_rates, false_positive_rates)


def equalized_opportunities_difference(predictions, actual, sensitive_attribute):
    """
    Implementation of equalized opportunities difference for different groups of sensitive attribute
    1. For each group calculate the TPR.
    2. Find the maximum and the minim group.
    3. Calculate the difference.
    """
    # 1. For each group calculate the TPR.
    unique_groups = np.sort(sensitive_attribute.unique())
    true_positive_rates = []
    for group in unique_groups:
        pred_group = predictions[sensitive_attribute == group]
        actual_group = actual[sensitive_attribute == group]
        conf_matrix = confusion_matrix(y_true=actual_group,
                                       y_pred=pred_group)
        TN, FP, FN, TP = conf_matrix.ravel()

        true_positive_rate = TP / (TP + FN)
        true_positive_rates += [true_positive_rate]

    # 2. Find the maximum and the minimum accepted_rate.
    maximum_tpr = max(true_positive_rates)
    minimum_tpr = min(true_positive_rates)

    # 3. Calculate the different.
    difference = maximum_tpr - minimum_tpr

    return difference, true_positive_rates


def demographic_parity_difference(predictions, sensitive_attribute):
    """
    Implementation of demographic parity difference for different groups of sensitive attribute
    1. For each group calculate the propotion of accepted rate.
    2. Find the maximum and the minim group.
    3. Calcaulte the difference.
    """
    # 1. For each group calculate the proportion of accepted rate.
    unique_groups = np.sort(sensitive_attribute.unique())
    proportion_of_accepted_rate = []
    for group in unique_groups:
        pred_group = predictions[sensitive_attribute == group]
        accepted_rate = (pred_group == 1).sum() / pred_group.shape[0]
        proportion_of_accepted_rate += [accepted_rate]

    # 2. Find the maximum and the minimum accepted_rate.
    maximum_accepted_rate = max(proportion_of_accepted_rate)
    minimum_accepted_rate = min(proportion_of_accepted_rate)

    # 3. Calculate the different.
    difference = maximum_accepted_rate - minimum_accepted_rate

    return difference, proportion_of_accepted_rate