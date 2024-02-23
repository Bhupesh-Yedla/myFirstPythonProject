python3 -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate  # For Windows

pip install -r requirements.txt

pytest tests/test_bookstore_api.py
