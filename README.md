# LLM CV Chat Bot

A FastAPI-based chatbot that answers questions about your CV using an LLM.

## Project Structure

- `app/` - Main application code
  - `main.py` - FastAPI entry point
  - `llm_interface.py` - Handles LLM communication
  - `cv_data/` - Your CV data (e.g., `cv.json`)
- `tests/` - Unit tests
- `requirements.txt` - Python dependencies

## Getting Started

1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Run the app:
   ```sh
   uvicorn app.main:app --reload
   ```

## Add your CV

Place your CV data in `app/cv_data/cv.json` or similar format.
