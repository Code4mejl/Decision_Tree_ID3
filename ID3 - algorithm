# 🧠 ID3 Algorithm Implementation

In this project, the **ID3 (Iterative Dichotomiser 3)** algorithm was first implemented **manually from scratch** to understand how decision trees work internally.

The manual implementation included:

* Entropy calculation
* Information Gain computation
* Recursive tree construction
* Feature selection based on maximum information gain

Example components implemented manually:

* `entropy()` function
* `information_gain()` function
* `build_tree()` recursive function

This helped in understanding how the **decision tree chooses the best attribute at each node**.

---

# ⚠️ Why the Manual ID3 Model Was Not Deployed

Although the manual ID3 implementation worked correctly in the notebook, it was **not suitable for deployment** for the following reasons:

1. The custom tree structure was **not easily serializable using pickle**.
2. The prediction function required **custom recursive traversal**, making it harder to integrate with Flask.
3. The manual implementation was **less optimized and harder to maintain**.

Because of these limitations, the deployed version uses **Scikit-learn's DecisionTreeClassifier**.

---

# ✅ Deployed Model

For the deployed web application, the following model was used:

```python
DecisionTreeClassifier(criterion="entropy")
```

This configuration behaves similarly to the **ID3 algorithm** because:

* ID3 uses **Information Gain**
* Information Gain is based on **Entropy**
* Setting `criterion="entropy"` replicates ID3 behavior

This allowed the project to:

* Maintain the **ID3 learning principle**
* Provide **stable predictions**
* Enable **easy model serialization using pickle**
* Integrate smoothly with **Flask deployment**

---

# 🔍 Summary

| Implementation                      | Purpose                                  |
| ----------------------------------- | ---------------------------------------- |
| Manual ID3 Algorithm                | Learning and understanding the algorithm |
| Scikit-learn DecisionTreeClassifier | Production deployment                    |

Thus, the project demonstrates both:

* **Algorithm-level understanding**
* **Practical ML deployment using industry tools**
