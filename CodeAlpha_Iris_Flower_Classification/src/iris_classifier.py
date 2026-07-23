import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

# Create images folder
os.makedirs("../images", exist_ok=True)

# Load Dataset
data = pd.read_csv("../dataset/Iris.csv")

print("\nFirst Ten Rows")
print(data.head(10))

print("\nDataset Information")
print(data.info())

print("\nMissing Values")
print(data.isnull().sum())

print("\nStatistical Summary")
print(data.describe())

# Remove Id column
if "Id" in data.columns:
    data = data.drop("Id", axis=1)

# Encode Species
encoder = LabelEncoder()
data["Species"] = encoder.fit_transform(data["Species"])

print("\nEncoded Classes")
for i, label in enumerate(encoder.classes_):
    print(label, "=", i)

# Pairplot
pairplot = sns.pairplot(data, hue="Species")
pairplot.savefig("../images/pairplot.png")
plt.close()

# Histograms
data.hist(figsize=(10,8))
plt.tight_layout()
plt.savefig("../images/histograms.png")
plt.close()

# Features and Target
X = data.drop("Species", axis=1)
y = data["Species"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy")
print(accuracy)

# Classification Report
print("\nClassification Report")
print(classification_report(
    y_test,
    y_pred,
    target_names=encoder.classes_
))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6,5))
sns.heatmap(
    cm,
    annot=True,
    cmap="Blues",
    fmt="d",
    xticklabels=encoder.classes_,
    yticklabels=encoder.classes_
)

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.savefig("../images/confusion_matrix.png")
plt.close()

# Feature Importance
importance = model.feature_importances_

plt.figure(figsize=(8,5))
plt.bar(X.columns, importance)
plt.title("Feature Importance")
plt.savefig("../images/feature_importance.png")
plt.close()

# Sample Prediction
sample = pd.DataFrame(
    [[5.1, 3.5, 1.4, 0.2]],
    columns=X.columns
)

prediction = model.predict(sample)

species = encoder.inverse_transform(prediction)

print("\n========== SAMPLE PREDICTION ==========")
print("Input:")
print(sample)

print("\nPredicted Species:", species[0])

print("\nProject Completed Successfully")