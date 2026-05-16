# MedBuddy

### Medbuddy is a ML based web application that predicts the likelihood of Heart Disease using medical parameters provided by the user. The project uses a trained ML model with a FastAPI backend and Streamlit frontend for real-time predictions.

## Live Demo: https://medicalbuddy.streamlit.app/

### Tech Stack: 
```
Frontend: Streamlit
Backend: FastAPI, Uvicorn
Machine Learning Libraries: Scikit learn, NumPy, Pandas, Joblib
Deployment: Render
```

## Project Structure

```text
MEDBUDDY
│
├── backend
│   ├── model_dir
│   ├── main.py
│   ├── predictor.py
│   ├── requirements.txt
│   └── training.py
│
├── dataset
│   └── heart.csv
│
├── frontend
│   └── app.py
│
├── logs
│   └── app.log
│
├── notebook_files
│   └── medbuddy_notebook.ipynb
│
├── .env
├── .gitignore
├── env_template.txt
└── README.md

### Dataset: https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset

### Home/Prediction Page
<img width="514" height="630" alt="image" src="https://github.com/user-attachments/assets/1cb5e25b-8baa-4ab0-b47a-e0ec42be47ab" />

*Contributions are welcome!*
