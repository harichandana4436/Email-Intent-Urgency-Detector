# 1. Title

# 📧 Email Intent & Urgency Detector

An AI-powered application that analyzes email content and classifies it based on **Intent, Urgency, and Tone** using Google Gemini and LangChain.

---

# 2. Problem Statement of the Project

Emails are one of the most common forms of communication in organizations. A large number of emails can make it difficult to quickly understand the purpose, urgency, and emotional tone of each message.

Manually analyzing emails is time-consuming and can lead to delays in responding to important messages.

This project solves this problem by using an AI model to automatically analyze an email and identify:

- What the sender wants (**Intent**)
- How urgent the email is (**Urgency**)
- How the email sounds (**Tone**)

---

# 3. Main Objective of the Project

The main objective of this project is to develop an AI-based email analysis system that can automatically classify email messages into structured categories.

The system aims to:

- Detect the intent of an email.
- Identify the urgency level.
- Determine the tone of the email.
- Produce a structured JSON response.
- Provide an easy-to-use interface through Streamlit.

---

# 4. Features

- 📧 Email text input
- 🤖 AI-powered email analysis
- 🎯 Intent classification
- 🚨 Urgency detection
- 😊 Tone detection
- 📋 Structured JSON output
- 🌐 Streamlit web interface
- 💻 Command-line version
- 🔐 Environment variable support for API credentials

### Intent Categories

- Request
- Complaint
- Information
- Inquiry
- Appreciation
- Follow-up
- Other

### Urgency Categories

- High
- Medium
- Low

### Tone Categories

- Urgent
- Professional
- Neutral
- Friendly
- Frustrated
- Appreciative

---

# 5. Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **Streamlit** | Web application interface |
| **LangChain** | LLM application framework |
| **Google Gemini 2.5 Flash** | AI model used for email analysis |
| **Pydantic** | Structured data validation |
| **python-dotenv** | Loading environment variables |

---

# 6. Work Architecture / Work Flow of the Project

```text
             User
               │
               ▼
        Enter Email Text
               │
               ▼
        Streamlit / CLI
               │
               ▼
        Prompt Template
               │
               ▼
      Google Gemini 2.5 Flash
               │
               ▼
       JSON Output Generation
               │
               ▼
       Pydantic JSON Parser
               │
               ▼
     Structured Analysis Result
               │
               ▼
     Intent | Urgency | Tone
```

### LangChain Chain

The project connects the components using a LangChain pipeline:

```text
Prompt → LLM → Output Parser
```

The email is passed through the prompt, analyzed by Gemini, and then converted into a structured output using the Pydantic-based JSON parser.

---

# 7. How It Works

### Step 1: User enters an email

The user enters an email message into the Streamlit text area.

### Step 2: Prompt processing

The email is inserted into a predefined prompt that instructs the AI to classify the message.

### Step 3: AI analysis

Google Gemini 2.5 Flash analyzes the email and determines:

- Intent
- Urgency
- Tone

### Step 4: Output parsing

The generated response is processed using a Pydantic model.

The expected structure is:

```json
{
  "intent": "Request",
  "urgency": "High",
  "tone": "Professional"
}
```

### Step 5: Display result

The structured result is displayed to the user as JSON in the Streamlit application.

---

# 8. Project Structure

```text
Email-Intent-Urgency-Detector/
│
├── app.py
│   └── Streamlit web application
│
├── main.py
│   └── Command-line application
│
├── model.py
│   └── Google Gemini model configuration
│
├── prompt.py
│   └── Email classification prompt
│
├── email_parser.py
│   └── Pydantic model and JSON output parser
│
├── .env
│   └── Google API key
│
├── .gitignore
│   └── Files excluded from Git
│
└── README.md
    └── Project documentation
```

---

# 9. Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/your-username/email-intent-urgency-detector.git
```

### Step 2: Open the project directory

```bash
cd email-intent-urgency-detector
```

### Step 3: Create a virtual environment

```bash
python -m venv venv
```

### Step 4: Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### Step 5: Install required packages

```bash
pip install streamlit langchain langchain-google-genai pydantic python-dotenv
```

### Step 6: Configure the API key

Create a `.env` file in the project directory:

```env
GOOGLE_API_KEY=your_google_api_key
```

Do not upload your `.env` file to GitHub.

Add it to `.gitignore`:

```text
.env
venv/
__pycache__/
```

---

# 10. Running the Application

## Run the Streamlit Application

Start the web application using:

```bash
streamlit run app.py
```

The application will open in your browser.

Enter an email into the text box and click the **Analyze** button.

## Run the Command-Line Application

You can also run the CLI version:

```bash
python main.py
```

Enter the email when prompted.

The analysis result will then be displayed in the terminal.

---

# 11. Example

### Input

```text
Subject: Urgent Project Update

Hi Team,

Please send me the latest project report as soon as possible.
The client meeting is scheduled for today, so I need the report urgently.

Thanks.
```

### Output

```json
{
  "intent": "Request",
  "urgency": "High",
  "tone": "Urgent"
}
```

### Another Example

**Input:**

```text
Thank you for your quick response and for helping me resolve the issue.
I really appreciate your support.
```

**Output:**

```json
{
  "intent": "Appreciation",
  "urgency": "Low",
  "tone": "Appreciative"
}
```