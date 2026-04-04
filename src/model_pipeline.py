from time import time
from sklearn.metrics import accuracy_score, fbeta_score


def train_predict(learner, sample_size, X_train, y_train, X_test, y_test):
    results = {}

    X_train_sub = X_train[:sample_size]
    y_train_sub = y_train[:sample_size]

    start = time()
    learner.fit(X_train_sub, y_train_sub)
    end = time()
    results["train_time"] = end - start

    start = time()
    predictions_test = learner.predict(X_test)
    end = time()
    results["pred_time"] = end - start

    predictions_train = learner.predict(X_train[:300])

    results["acc_train"] = accuracy_score(y_train[:300], predictions_train)
    results["acc_test"]  = accuracy_score(y_test, predictions_test)
    results["f_train"]   = fbeta_score(y_train[:300], predictions_train, beta=0.5, zero_division=0)
    results["f_test"]    = fbeta_score(y_test, predictions_test,  beta=0.5, zero_division=0)

    print(f"{learner.__class__.__name__} trained on {sample_size} samples.")
    print(f"  Train time : {results['train_time']:.4f}s  |  Pred time : {results['pred_time']:.4f}s")
    print(f"  Acc (train): {results['acc_train']:.4f}  |  Acc (test) : {results['acc_test']:.4f}")
    print(f"  F0.5(train): {results['f_train']:.4f}  |  F0.5(test) : {results['f_test']:.4f}")
    print()

    return results
