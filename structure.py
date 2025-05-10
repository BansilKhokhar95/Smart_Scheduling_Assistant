import os

# Define directory and file structure
structure = {
    "app": [
        "main.py",
        "config.py",
        "langgraph_flow.py",
        "scheduler.py",
        "reminders.py",
    ],
    "app/terminal_ui": [
        "input_handler.py",
        "display.py",
    ],
    "app/telegram_bot": [
        "bot.py",
        "handlers.py",
    ],
    "app/services/calendar": [
        "google_calendar.py",
    ],
    "app/services/notifications": [
        "telegram_notify.py",
    ],
    "app/services/contacts": [
        "contact_lookup.py",
    ],
    "app/agents": [
        "intent_parser.py",
        "time_extractor.py",
        "slot_filler.py",
    ],
    "app/models": [
        "schemas.py",
        "event.py",
    ],
    "app/utils": [
        "oauth.py",
        "time_utils.py",
        "logger.py",
    ],
    "tests": [
        "test_scheduler.py",
        "test_google_calendar.py",
        "test_langgraph_flow.py",
    ]
}

# Create folders and empty files
for folder, files in structure.items():
    os.makedirs(folder, exist_ok=True)
    for file in files:
        file_path = os.path.join(folder, file)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                f.write("")

# Root-level files
root_files = ["requirements.txt", ".env", "README.md", "run_terminal.sh"]
for file in root_files:
    if not os.path.exists(file):
        with open(file, 'w') as f:
            f.write("")

print("✅ Project structure created successfully.")
