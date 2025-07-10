# exercise-track-app
🏃‍♂️ Exercise Tracker – Nutritionix & Google Sheets API
This is a simple Python project that lets you track your workouts by sending your exercise data to the Nutritionix API and automatically logging the results to a Google Sheet. It’s a great way to practice working with APIs, environment variables, and POST requests.

🚀 Features
✅ Accepts natural language input (e.g., “I ran 3 miles and did 20 push-ups”)
✅ Sends your input to the Nutritionix API to get calories burned and duration
✅ Logs each exercise with date and time to a Google Sheet via Sheety API
✅ Uses environment variables to store sensitive credentials (.env file)

📁 Project Structure
📦 exercise-tracker/
├── main.py         # Main script for collecting, processing, and posting workout data
├── .env            # Stores your API keys and tokens (not committed to version control)

🛠️ How It Works
Nutritionix API

Parses your natural language input to extract exercise details.

Requires APP_ID and API_KEY.

Sheety API

Posts each exercise log to your connected Google Sheet.

Requires a bearer TOKEN and SHEET_POST_ENDPOINT.

Environment Variables

Stored in a .env file and loaded using python-dotenv.

▶️ How to Use
1. Clone the repo
  git clone https://github.com/yourusername/exercise-tracker.git
  cd exercise-tracker
2. Install dependencies
   pip install requests python-dotenv
3. Create a .env file
   APP_ID=your_nutritionix_app_id
  API_KEY=your_nutritionix_api_key
  TOKEN=your_sheety_bearer_token
  SHEET_POST_ENDPOINT=https://api.sheety.co/your_sheety_endpoint
4. Run the script
   python main.py
5. Check your Google Sheet!
  Each exercise will be logged with date, time, name, duration, and calories burned.

📌 Requirements
Python 3.x

requests

python-dotenv
