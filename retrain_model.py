{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "4231d011-1850-443e-bea8-79290fccf720",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Model and encoders saved successfully.\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "import joblib\n",
    "\n",
    "# Create sample dataset\n",
    "data = {\n",
    "    'Age': [25, 45, 65, 34, 55, 29, 62, 48, 36, 50, 30, 40, 52, 60, 28],\n",
    "    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female',\n",
    "               'Male', 'Female', 'Male', 'Female', 'Male'],\n",
    "    'Symptom': ['Fatigue', 'Fever', 'Chest Pain', 'Cough', 'Headache', 'Nausea', 'Shortness of Breath',\n",
    "                'Dizziness', 'Back Pain', 'Vomiting', 'Fatigue', 'Chest Pain', 'Nausea', 'Back Pain', 'Fever'],\n",
    "    'Recommended_Test': ['CBC', 'COVID Test', 'ECG', 'X-Ray', 'MRI', 'Liver Function', 'Pulmonary Function',\n",
    "                         'MRI', 'X-Ray', 'Liver Function', 'CBC', 'ECG', 'Liver Function', 'X-Ray', 'COVID Test']\n",
    "}\n",
    "\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "# Encode\n",
    "le_gender = LabelEncoder()\n",
    "le_symptom = LabelEncoder()\n",
    "le_test = LabelEncoder()\n",
    "\n",
    "df['Gender'] = le_gender.fit_transform(df['Gender'])\n",
    "df['Symptom'] = le_symptom.fit_transform(df['Symptom'])\n",
    "df['Recommended_Test_Label'] = le_test.fit_transform(df['Recommended_Test'])\n",
    "\n",
    "X = df[['Age', 'Gender', 'Symptom']]\n",
    "y = df['Recommended_Test_Label']\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)\n",
    "\n",
    "model = RandomForestClassifier(n_estimators=100, random_state=42)\n",
    "model.fit(X_train, y_train)\n",
    "\n",
    "# Save model and encoders\n",
    "joblib.dump(model, \"model.pkl\")\n",
    "joblib.dump(le_gender, \"le_gender.pkl\")\n",
    "joblib.dump(le_symptom, \"le_symptom.pkl\")\n",
    "joblib.dump(le_test, \"le_test.pkl\")\n",
    "\n",
    "print(\"✅ Model and encoders saved successfully.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7756e5b2-30de-4184-8855-906dc0fa4863",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
