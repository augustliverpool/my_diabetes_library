from sklearn.metrics import roc_auc_score

def compute_roc_auc(model, X, y):
    y_pred_proba = model.predict_proba(X)[:, 1]  
    return roc_auc_score(y, y_pred_proba)
