from sklearn.linear_model import LogisticRegression
import pandas as pd
def train_model(X_train, y_train):
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model

def predict_and_add_column(model, X, y):
    probabilities = model.predict_proba(X)[:, 1]  
    predictions_df = pd.DataFrame(X)
    predictions_df['predictions'] = probabilities
    predictions_df['actual'] = y.reset_index(drop=True)  
    return predictions_df
