# HugAI Connect

This folder contains applications and notebooks related to HuggingFace integrations, including SmartSheet OAuth.

## Files

- `smartsheet.py`: A Flask application that handles OAuth authentication with SmartSheet, allowing integration with SmartSheet APIs for reading and writing sheets.
- `huggingface.ipynb`: A Jupyter notebook (content not detailed, but likely related to HuggingFace models or tasks).
- `us_census/`: A subdirectory containing PDF files related to US Census data, possibly used for HuggingFace-based processing.

## How to Run

### SmartSheet Integration (smartsheet.py)
1. Install dependencies: `pip install flask requests`.
2. Update the CLIENT_ID, CLIENT_SECRET, and REDIRECT_URI with your SmartSheet app credentials.
3. Run the Flask app: `python smartsheet.py`.
4. Open `http://localhost:5000/` in your browser and click "Click here to login with SmartSheet" to start OAuth flow.

### HuggingFace Notebook (huggingface.ipynb)
1. Ensure you have Jupyter Notebook installed: `pip install jupyter`.
2. Install required dependencies as per the notebook's imports (e.g., `pip install transformers datasets`).
3. Run the notebook: `jupyter notebook huggingface.ipynb`.
4. Execute the cells to explore HuggingFace models and tasks.
