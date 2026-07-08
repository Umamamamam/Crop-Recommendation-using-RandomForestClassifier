# Crop Recommendation App

A simple web app that recommends the best crop to grow based on soil and climate values.

## What it does

- User enters values like Nitrogen, Phosphorus, and Rainfall.
- Flask backend runs the values through a prediction model.
- App shows the best matching crop plus a top-3 list with confidence percentages.

## Features

- Clean, simple form to enter soil and weather values
- Instant crop prediction on submit
- Top-3 crop matches shown with percentage bars
- Responsive design (works on mobile too)

## Tech Used

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS
- **Model:** scikit-learn (or your ML library of choice)

## Project Structure

```
crop-recommendation-app/
├── app.py              # Flask app and routes
├── model.pkl           # Trained ML model
├── templates/
│   └── index.html      # Main page
├── static/
│   └── style.css        # Styling
└── requirements.txt     # Python dependencies
```

## Requirements

- Python 3.8+
- Flask
- scikit-learn
- pandas
- numpy

## How to Run

1. Clone the repo
```bash
git clone https://github.com/yourusername/crop-recommendation-app.git
cd crop-recommendation-app
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the app
```bash
python app.py
```

4. Open your browser at `http://localhost:5000`

## How It Works

1. User fills in soil nutrients (N, P, K) and climate values (rainfall, temperature, humidity)
2. Form data is sent to the Flask backend via POST request
3. Backend loads the trained model and makes a prediction
4. Result (best crop + top matches) is sent back and shown on the page

## Future Improvements

- Add more crop types to the dataset
- Add user accounts to save past predictions
- Deploy to a live server (Render/Heroku)

## Author

Umamaheshwara Reddy
