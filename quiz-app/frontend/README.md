# AI-Powered Quiz Generator

This project uses Natural Language Processing (NLP) and the FLAN-T5 model to generate Multiple Choice Questions (MCQs) from input text.

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Download spaCy model: `python -m spacy download en_core_web_sm`

## Running the Application

- To run the Streamlit app: `streamlit run app/main.py`
- To run the FastAPI server: `uvicorn api.endpoints:app --reload`

## Project Structure

- `app/`: Contains the core application logic
- `api/`: Holds the FastAPI endpoints
- `models/`: For any custom ML models (if needed)
- `data/`: Stores sample texts or datasets
- `tests/`: Contains unit and integration tests
- `static/` and `templates/`: For frontend assets

## Evaluation Criteria

1. Functionality: The project generates MCQs from input text.
2. Code Quality: The code is modular, readable, and well-documented.
3. GenAI Integration: Uses FLAN-T5 for question generation.
4. Creativity: Implements a user-friendly interface with Streamlit.
5. Scalability: Can handle various text inputs and generate multiple questions.
