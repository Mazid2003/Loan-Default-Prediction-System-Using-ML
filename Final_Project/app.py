from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the saved Random Forest model
model = joblib.load('random_forest_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract data from form
    try:
        age = float(request.form['Age'])
        experience = float(request.form['Experience'])
        income = float(request.form['Income'])
        family = int(request.form['Family'])
        ccavg = float(request.form['CCAvg'])
        education = int(request.form['Education'])
        mortgage = float(request.form['Mortgage'])
        securities_account = int(request.form['SecuritiesAccount'])
        cd_account = int(request.form['CDAccount'])
        online = int(request.form['Online'])
        creditcard = int(request.form['CreditCard'])

        # Put into numpy array
        features = np.array([[age, experience, income, family, ccavg,
                              education, mortgage, securities_account,
                              cd_account, online, creditcard]])

        # Make prediction
        prediction = model.predict(features)[0]

        result = "✅ Approved (Repay Expected)" if prediction == 1 else "❌ Rejected (Default Risk)"
        return render_template('index.html', prediction=result)

    except Exception as e:
        return render_template('index.html', prediction=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)
