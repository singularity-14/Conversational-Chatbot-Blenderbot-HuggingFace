# Conversational Chatbot

This repository contains the code for a simple chatbot application using the Hugging Face API and Streamlit. The chatbot utilizes the `facebook/blenderbot-400M-distill` model to generate responses to user input.

## Features

- **Hugging Face Integration**: Utilizes the `facebook/blenderbot-400M-distill` model from Hugging Face.
- **Streamlit Frontend**: Interactive user interface built with Streamlit.
- **Environmental Variables**: Secure API token handling using `dotenv`.
- **Chat History**: Maintains chat history across user interactions.

## Installation

1. **Clone the repository**:

```bash
git clone https://github.com/yourusername/conversational-chatbot.git
cd conversational-chatbot
```

2. **Create and activate a virtual environment**:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. **Install the required packages**:

```bash
pip install -r requirements.txt
```

4. **Set up environmental variables**:

Create a `.env` file in the root directory of the project and add your Hugging Face API token:

```plaintext
HUGGINGFACEAPI=your_hugging_face_api_token
```

## Usage

1. **Run the Streamlit application**:

```bash
streamlit run app.py
```

2. **Interact with the chatbot**:

Open your web browser and go to `http://localhost:8501`. You can start interacting with the chatbot by typing your messages in the input box.

## Code Overview

### `app.py`

This file contains the main application code for the chatbot.

### `backend.py`

This file contains the backend logic for the chatbot.
