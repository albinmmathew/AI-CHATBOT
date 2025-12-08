# AI Chatbot

A simple, interactive web-based chatbot application powered by Google's Gemini AI. This project uses Flask for the backend and Bootstrap for the frontend to provide a clean and responsive user interface.

## Features

*   **Interactive Chat Interface:** A user-friendly web interface to interact with the AI.
*   **Gemini AI Integration:** Powered by Google's advanced Gemini generative AI models via the `amm_geminiassist` library.
*   **Chat History:** Keeps track of previous queries and responses within the current session for context.
*   **Responsive Design:** styled with Bootstrap 5 to look good on desktop and mobile.

## Prerequisites

Before you begin, ensure you have the following installed:

*   **Python 3.x**: Make sure Python is installed on your system.
*   **Gemini API Key**: You need a valid API key from Google AI Studio.

> [!IMPORTANT]
> You **MUST** create a `.env` file in the project root directory and add your Gemini API key to it. The application will not function without this key.

## Installation

1.  **Clone the repository** (if applicable) or navigate to the project directory.

2.  **Install Dependencies:**
    This project requires `Flask`, `python-dotenv`, `google-generativeai` and `amm_geminiassist`.

    ```bash
    pip install flask python-dotenv google-generativeai amm_geminiassist
    ```

3.  **Configure Environment Variables:**
    Create a file named `.env` in the root directory (same level as `app.py`). Add your API key as follows:

    ```env
    GEMINI_API_KEY=your_actual_api_key_here
    ```

## Usage

1.  **Run the Application:**
    Open your terminal or command prompt in the project directory and run:

    ```bash
    python app.py
    ```

2.  **Access the Chatbot:**
    Open your web browser and go to:
    `http://127.0.0.1:5000` or `http://localhost:5000`

3.  **Start Chatting:**
    Type your message in the input box and click "Ask Gemini". The AI's response will appear below, followed by your chat history.
