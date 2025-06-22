# 📅 Task Planning Agent using ChatGPT (OpenAI) — Colab-Compatible with .ics Download

# Run this in a separate cell before executing the code if using Google Colab:
# !pip install ics gradio openai

# Required packages: Run this command on the terminal if using Pycharm/VScode
#pip install gradio openai ics

import gradio as gr
import datetime
import openai
from ics import Calendar, Event

# 📅 Create .ics calendar file
def create_ics_file(tasks):
    calendar = Calendar()
    for task, due in tasks:
        try:
            date_obj = datetime.datetime.strptime(due, "%Y-%m-%d")
            event = Event()
            event.name = task
            event.begin = date_obj.strftime("%Y-%m-%dT09:00:00")
            event.duration = datetime.timedelta(hours=1)
            calendar.events.add(event)
        except Exception as e:
            print(f"Skipped: {task} - Reason: {e}")
            continue
    with open("planned_tasks.ics", "w", encoding="utf-8") as f:
        f.writelines(calendar.serialize_iter())

# 🧠 Plan tasks using GPT
def plan_tasks(input_text, api_key):
    try:
        client = openai.OpenAI(api_key=api_key)

        prompt = f"""
You are a task planning assistant.

Take the following unstructured to-dos, goals, or notes:
{input_text}

Organize them into a structured daily plan with:
1. Prioritized tasks (High, Medium, Low)
2. Suggested deadlines
3. Any reminders or follow-ups
4. Group similar tasks
5. Add short notes if needed to clarify

Also, for each task where possible, append a line in this format:
Task Name - Due: YYYY-MM-DD

Display output clearly with sections:
### Today's Plan
### Deadlines & Priorities
### Reminders
### Notes or Grouped Tasks
        """

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful and organized planning assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        output_text = response.choices[0].message.content.strip()

        # Extract lines with due dates
        tasks_with_dates = []
        for line in output_text.split("\n"):
            if " - Due:" in line:
                try:
                    task, due = line.split(" - Due:")
                    datetime.datetime.strptime(due.strip(), "%Y-%m-%d")
                    tasks_with_dates.append((task.strip(), due.strip()))
                except:
                    continue

        create_ics_file(tasks_with_dates)

        return output_text, "planned_tasks.ics"

    except Exception as e:
        return f"⚠️ Error: {str(e)}", None

# 🎛️ Gradio UI
def create_ui():
    with gr.Blocks() as demo:
        gr.Markdown("## 🧠 Task Planning Agent")
        api_key_input = gr.Textbox(label="🔑 OpenAI API Key", type="password")
        input_text = gr.Textbox(label="📝 Paste To-Dos, Notes or Goals", lines=10)
        output = gr.Textbox(label="📋 Structured Daily Plan Output", lines=25)
        download = gr.File(label="📅 Download .ics Calendar File")
        submit = gr.Button("📅 Plan My Day")
        submit.click(fn=plan_tasks, inputs=[input_text, api_key_input], outputs=[output, download])
    demo.launch(share=True)

if __name__ == "__main__":
    create_ui()
