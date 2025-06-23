# 📅 Task Planning Agent — AI-Powered Daily Scheduler with .ics Export (Python 3.13 Compatible)

*Turn your scattered to-dos and goals into a structured plan with calendar-ready tasks.*

---

## 🌍 Project Description

The Task Planning Agent uses **OpenAI GPT-4** to convert raw task notes into a structured plan. It also auto-generates a `.ics` file compatible with calendar apps like Google Calendar, Outlook, and Apple Calendar.

---

## 📁 Table of Contents

* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)
* [Project Structure](#project-structure)
* [License](#license)

---

## ✨ Features

| Feature                 | Details                                           |
| ----------------------- | ------------------------------------------------- |
| 🧠 GPT-4 Planner        | Converts notes into structured tasks              |
| 📅 .ics Calendar Export | Compatible with most calendar applications        |
| 🔑 API Key Secure       | Uses OpenAI API key via secure textbox            |
| 🖼️ Gradio Interface    | Simple and interactive web UI                     |
| 🧪 PyCharm Ready        | Compatible with Python 3.13 and local development |

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourname/task-planning-agent.git
cd task-planning-agent
```

### 2. Create and activate virtual environment

```bash
python3.13 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install gradio openai ics
```

> ✅ If you're using Google Colab, use this command instead:

```python
!pip install gradio openai ics
```

---

## 💻 Usage

Run the following command to launch the app:

```bash
python app.py
```

You will see a Gradio interface where you can:

* Paste task notes or goals
* Enter your OpenAI API key
* Get a detailed task plan + download the `.ics` file

---

## 📂 Project Structure

```
task-planning-agent/
├── app.py               # Main script with UI and logic
├── planned_tasks.ics    # Auto-generated calendar file (output)
└── README.md            # This file
```

---

## 📝 Notes

* Make sure to use a valid OpenAI API key
* `.ics` file includes all tasks with valid due dates
* The model used is `gpt-4` but can be changed in code
* Ideal for personal planning, productivity coaching, and time-blocking

---

## 📜 License

MIT License — Free to use and modify. Attribution appreciated.

---

## 🙌 Acknowledgements

* [OpenAI](https://openai.com/)
* [Gradio](https://gradio.app/)
* [ics.py](https://icspy.readthedocs.io/)
