class Config:
    DARK_MODE_CSS = """
        <style>
            body { background-color: #2E2E2E; color: white; }
            .chat-bubble { color: white; }
            .chat-bubble.user { background-color: #2C3E50; }
            .chat-bubble.ai { background-color: #34495E; }
            .chat-icon.user { background-color: #1ABC9C; }
            .chat-icon.ai { background-color: #3498DB; }
        </style>
    """

    LIGHT_MODE_CSS = """
        <style>
            body { background-color: #FFFFFF; color: black; }
            .chat-bubble.user { background-color: #DCF8C6; }
            .chat-bubble.ai { background-color: #ECECEC; }
            .chat-icon.user { background-color: #34B7F1; }
            .chat-icon.ai { background-color: #00BFA5; }
        </style>
    """

    SAFETY_SETTINGS = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    ]
