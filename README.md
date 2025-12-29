# 📧 Spam Detection App

A sleek and efficient web application that detects whether a message is **spam** or **not spam** using a trained machine learning model. Built with **Python**, **scikit-learn**, and **Streamlit**, the app offers a fast, interactive, and visually appealing user experience.

🔗 **Live App**: [Click here to try it out](https://mail-spam-detector-app.streamlit.app/)

---

## ✨ Features

- 🤖 AI-powered message classification  
- ⚡ Real-time predictions  
- 🎯 High accuracy using a trained Naive Bayes model  
- 🔒 Privacy-focused: all processing happens locally  
- 💻 Modern UI with responsive layout and dark theme  

---

## 📂 Project Structure

- `Spam_Classifier.ipynb` – Jupyter notebook for training and evaluating the model  
- `spam_classifier_model.pkl` – Trained classification model (saved with joblib)  
- `vectorizer.pkl` – Fitted TfidfVectorizer for text processing  
- `spam_detector_app.py` – Streamlit web application script  
- `requirements.txt` – Project dependencies
- `spam.csv` – contains data of our project
- `README.md` – Project documentation (this file)

---

## 🚀 Getting Started

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/spam-detection-app.git
cd spam-detection-app
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the Streamlit app**
```bash
streamlit run spam_detector_app.py
```

---

## 🛠️ How It Works

- Text input is vectorized using a pretrained `TfidfVectorizer`.  
- A **Multinomial Naive Bayes** model predicts whether the message is spam or not.  
- Results are displayed instantly with a clean UI.  

---

## 🧪 Requirements

Listed in `requirements.txt`:

- streamlit  
- joblib  
- scikit-learn  
- pandas  
- numpy  

---

## 🙋‍♂️ Author

**Karan Bhoriya**  
GitHub: [@Karanpr-18](https://github.com/Karanpr-18)  
LinkedIn: [karan-bhoriya-b5a3382b7](https://www.linkedin.com/in/karan-bhoriya-b5a3382b7)

---

## 📄 License

This project is licensed under the MIT License.
