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

*Contributions are welcome!*
