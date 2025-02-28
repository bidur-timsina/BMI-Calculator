# BMI Calculator

## Description
This is a simple **BMI (Body Mass Index) Calculator** built using **Streamlit**. It allows users to input their weight (in kilograms) and height (in centimeters) to calculate their BMI and display the corresponding BMI category.

## Features
- User-friendly interface using **Streamlit**.
- Accepts weight in **kilograms (kg)** and height in **centimeters (cm)**.
- Calculates **BMI** using the formula:
  
  \[ BMI = \frac{weight (kg)}{(height (m))^2} \]
  
- Provides a classification of BMI based on standard BMI categories.

## BMI Categories
| BMI Range | Category |
|-----------|----------------------|
| < 16.0   | Severely Underweight |
| 16.0 - 18.4 | Underweight |
| 18.5 - 24.9 | Normal |
| 25.0 - 29.9 | Overweight |
| 30.0 - 34.9 | Moderately Obese |
| 35.0 - 39.9 | Severely Obese |
| > 40.0 | Morbidly Obese |

## Installation
### Prerequisites
Ensure you have **Python 3.x** installed along with **Streamlit**.

### Steps
1. Clone this repository:
   ```sh
   git clone https://github.com/YOUR-USERNAME/REPO-NAME.git
   cd REPO-NAME
   ```
2. Install dependencies:
   ```sh
   pip install streamlit
   ```
3. Run the Streamlit app:
   ```sh
   streamlit run app.py
   ```

## File Structure
```
📂 BMI-Calculator
│── app.py              # Main Streamlit app
│── bmi_operation.py    # Functions for BMI calculation and categorization
│── README.md           # Documentation
```

## Usage
1. Open the web interface.
2. Enter your **weight in KG** and **height in CM**.
3. Click on **"Calculate BMI"**.
4. View your **BMI value and category**.

## Author
**Bidur Timsina**

