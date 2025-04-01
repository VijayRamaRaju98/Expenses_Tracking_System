# Expense management System

This project is an expense management system that consists of a streamlit frontend and FastAPI backend server.


## Project Structure


- **fontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend server code.
- **tests/**:Contais the test cases for the frontend and backend.
- **requirements.txt/**:List of the required python packages.
- **README.md/**:Provides an Overview and instructions for the project.

## Setup Instructions

1. **Clone the repository:**
```bash
git clone [git address]
cd project_expense_tracking
```


2. **Install dependencies:**:

```bash
pip install -r requirements.txt
```

3. **Run the FastAPI server:**:
```commandline
uvicorn server:app --reload
```

4. **Run the Streamlit App:**:
```commandline
stremlit run frontend/app.py
```