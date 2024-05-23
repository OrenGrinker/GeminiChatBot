# Chatbot with Gemini Models

This project is a Streamlit-based chatbot application utilizing various Gemini models for natural language processing. Users can switch between light and dark modes and configure model settings to customize their interactions.

## Features

- Toggle between light and dark mode.
- Choose from three different Gemini models: `Gemini 1.5 Flash`, `Gemini 1.5 Pro`, and `Gemini 1.0 Pro`.
- Adjust model parameters such as temperature, top-p, top-k, and maximum output tokens.
- Securely input and use the Gemini API key.
- Interactive chat interface with history.

## Installation

To get started, clone the repository and install the required packages:

```bash
git clone https://github.com/OrenGrinker/geminiChatBot.git
cd geminiChatBot
pip install -r requirements.txt
```

## Usage

Run the Streamlit application with:

```bash
streamlit run app.py
```

## Configuration

The application settings can be adjusted via the sidebar:

- Dark Mode: Toggle between light and dark mode.
- Choose Model: Select from Gemini 1.5 Flash, Gemini 1.5 Pro, or Gemini 1.0 Pro.
- Temperature: Adjust the creativity of the model's responses.
- Top P: Control the cumulative probability for token selection.
- Top K: Limit the number of tokens considered.
- Max Output Tokens: Set the maximum number of tokens in the response.

## License

his project is licensed under the MIT License. See the LICENSE file for details.

