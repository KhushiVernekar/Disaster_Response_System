# 🌍 Disaster Response System

This project is designed to aid in quick decision-making during earthquake disasters by integrating machine learning, real-time APIs, and Telegram-based communication. It helps users instantly alert authorities with geolocation and severity prediction.

---

### 🧰 Technologies Used

* **Backend**: Python 3.9, Flask
* **Frontend**: HTML, CSS, Bootstrap
* **Database**: SQLite
* **Machine Learning**: scikit-learn (Random Forest)
* **APIs**: Google Gemini AI, Telegram Bot API
* **Libraries**: Pandas, NumPy, telepot, google-generativeai

---

### 📂 Project Structure

* `app.py` – Main Flask app; handles routes and integrates ML predictions
* `RouteMap.py` – Route generation and visualization based on geolocation
* `benchmarks.py` – Compares different ML model performances
* `crowd.py` – Simulates or analyzes crowd data for density during disaster
* `detect.py` – Detects earthquakes using seismic data
* `export.py` – Exports filtered data or reports (e.g., to CSV or JSON)
* `train.py` – Trains the Random Forest model using the dataset
* `val.val` – Model validation parameters/configuration
* `data.csv` – Dataset used to train and test the ML model
* `requirements.txt` – Lists all Python dependencies
* `best.pt` – (Optional) A saved PyTorch model, if deep learning was explored
* `user_data.db` – SQLite DB storing user/location data
* `templates/` – HTML frontend files
* `static/` – CSS, JS, image assets
* `model/dtt.pkl` – Trained Random Forest model

---

### ⚙️ Installation

**Prerequisites:**

* Python 3.9
* SQLite
* Telegram Bot Token
* Google Gemini API Key

**Steps:**

1. Clone the repository:

```
git clone https://github.com/KhushiVernekar/Disaster_Response_System.git
cd Disaster_Response_System
```

2. Create and activate a virtual environment:

```
python3.9 -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Configure API Keys:
   Replace the Telegram Bot Token and Gemini API key in `app.py`:

```
bot = telepot.Bot("YOUR_TELEGRAM_BOT_TOKEN")
genai.configure(api_key='YOUR_GEMINI_API_KEY')
```

Alternatively, use a `.env` file with `python-dotenv`.

5. Prepare the Model:
   Ensure `model/dtt.pkl` (Random Forest model) is in the model directory.
   If missing, train the model using `train.py` with the Kaggle Earthquake dataset and save it as `dtt.pkl`.

---

### ▶️ Running the Project

You can run the project using IDLE 3.9 or the command line.

**Using IDLE 3.9**
Open `app.py` in IDLE and press F5 or go to `Run > Run Module`.

**Using Command Line**

```
source venv/bin/activate        # On Windows: venv\Scripts\activate
python app.py
```

Open your browser and visit:
[http://localhost:5000](http://localhost:5000)

---

### 📱 Telegram Integration

* User sends message via Telegram bot
* Bot fetches user location and context
* ML model predicts severity
* Gemini AI responds with instructions or alerts
* Optionally, system notifies higher authorities

---

### 📊 ML Model Info

* Dataset: Earthquake Management (Kaggle)
* Model: Random Forest Classifier
* Accuracy: \~85%
* Features used: Magnitude, Depth, Latitude, Longitude
* Output: Severity classification

---

### 📌 Key Features

* Real-time response using Telegram bot
* Map-based route guidance for emergency services
* Earthquake severity prediction
* Gemini AI-based intelligent assistance
* Simple and interactive UI
* Offline ML model support

---
