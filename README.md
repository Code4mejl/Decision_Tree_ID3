# 🎾 Play Tennis Predictor (ID3 Decision Tree)

A simple **Machine Learning Web Application** that predicts whether a tennis match should be played based on weather conditions using the **ID3 Decision Tree algorithm**.

The model is trained using the classic **Play Tennis dataset** and deployed using **Flask**, with a simple **HTML + CSS frontend**.

---

# 📌 Project Overview

This project demonstrates the complete pipeline of a Machine Learning application:

Dataset → Model Training → Model Serialization → Web API → Frontend → Deployment

The application takes the following weather conditions as input:

* Outlook
* Temperature
* Humidity
* Wind

Based on these features, the ML model predicts:

* **Yes** → Play Tennis
* **No** → Do not Play

---

# 🧠 Machine Learning Algorithm

This project uses:

**ID3 (Iterative Dichotomiser 3)**

Implemented using:

`DecisionTreeClassifier(criterion="entropy")`

Entropy is used to measure **information gain**, which helps build the decision tree.

---

# 📂 Project Structure

```
ID3
│
├── app.py
├── id3_model.pkl
├── play_tennis.csv
├── requirements.txt
├── Procfile
│
├── templates
│   └── index.html
│
└── static
    └── style.css
```

---

# ⚙️ Technologies Used

* Python
* Scikit-learn
* Pandas
* Flask
* HTML
* CSS
* Gunicorn
* Render (Deployment)
* Git & GitHub

---

# 📊 Dataset

The dataset used is the classic **Play Tennis dataset**.

Features:

| Feature     | Description             |
| ----------- | ----------------------- |
| Outlook     | Sunny / Overcast / Rain |
| Temperature | Hot / Mild / Cool       |
| Humidity    | High / Normal           |
| Wind        | Weak / Strong           |

Target:

```
PlayTennis → Yes / No
```

---

# 🧪 Model Training

Model training was done in **Jupyter Notebook**.

Steps:

1. Load dataset using Pandas
2. Separate features and target
3. Convert categorical values using **One-Hot Encoding**
4. Train Decision Tree with **Entropy**
5. Save trained model using **Pickle**

Example training code:

```python
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

data = pd.read_csv("play_tennis.csv")

X = data.drop("PlayTennis", axis=1)
y = data["PlayTennis"]

X = pd.get_dummies(X)

model = DecisionTreeClassifier(criterion="entropy")
model.fit(X, y)

columns = X.columns

pickle.dump((model, columns), open("id3_model.pkl", "wb"))
```

---

# 🌐 Web Application

The web application was built using **Flask**.

Workflow:

```
User Input Form
      ↓
Flask Backend
      ↓
Load Pickle Model
      ↓
Prediction
      ↓
Display Result
```

The frontend collects weather data and sends it to the Flask backend for prediction.

---

# 🎨 Frontend

The frontend was created using:

* HTML
* CSS

Features:

* Dropdown weather selection
* Styled UI
* Responsive card layout
* Prediction result display

---

# 🚀 Deployment

The project is deployed using **Render**.

Deployment steps:

1. Push project to GitHub
2. Create `requirements.txt`
3. Create `Procfile`
4. Connect repository to Render
5. Deploy web service

Example Procfile:

```
web: gunicorn app:app
```

---

# ⚠️ Errors Encountered & Solutions

##  Model Not Defined Error

Error:

```
NameError: name 'model' is not defined
```

Cause:

The model variable was not created before saving with pickle.

Solution:

Train the model first before saving:

```
model.fit(X,y)
```

---


---

##  Feature Names Mismatch Error

Error:

```
ValueError: The feature names should match those that were passed during fit
```

Cause:

During training, categorical data was converted using **get_dummies**, which created additional columns.

During prediction, those columns were missing.

Solution:

Save the training columns and reindex the prediction data:

```python
input_data = input_data.reindex(columns=columns, fill_value=0)
```

This ensures prediction data matches training data.

---



# 📸 Application Preview

Example Input:

```
Outlook: Sunny
Temperature: Hot
Humidity: High
Wind: Weak
```

Prediction:

```
Do Not Play Tennis
```

---

# 📦 Installation

Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/ID3-project.git
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

# 📈 Future Improvements

Possible improvements:

* Add Decision Tree Visualization
* Add REST API endpoint
* Improve UI with Bootstrap
* Add model accuracy metrics
* Deploy with Docker

---

# 👨‍💻 Author

Developed as part of a **Machine Learning mini project** demonstrating end-to-end ML application development.


Give it a ⭐ on GitHub!
