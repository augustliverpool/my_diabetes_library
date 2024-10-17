

from sklearn.metrics import roc_auc_score
def compute_roc_auc(model, X, y):
    
    probabilities = model.predict_proba(X)[:, 1]
    return roc_auc_score(y, probabilities)

def print_roc_auc(model, X_train, y_train, X_test, y_test):
    train_roc_auc = compute_roc_auc(model, X_train, y_train)
    test_roc_auc = compute_roc_auc(model, X_test, y_test)
    
    print(f"Train ROC AUC: {train_roc_auc:.4f}")
    print(f"Test ROC AUC: {test_roc_auc:.4f}")
