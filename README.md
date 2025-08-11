# 🤖📋 HR-ASSIST Agentic AI System
This project implements a GenAI-powered MCP server equipped with intelligent HR management tools to streamline core HR processes.

1. **Employee Onboarding – Automates the entire onboarding workflow, including:**
   - 🗂️ Adding the new employee to the HRMS system.
   - ✉️ Sending a personalized welcome email with login credentials in a pre-defined format.
   - 📢 Notifying the assigned manager about the new joiner’s onboarding.
   - 💻 Raising service tickets for essential resources like a laptop, ID card, and other equipment.
   - 🗓️ Scheduling an introductory meeting between the new employee and their manager.

2. **Leave Management – Simplifies leave administration by enabling HR to:**
   - 📝 Apply for employee leaves through a conversational interface.
   - 📊 Instantly check and display remaining leave balances.

The system leverages AI for natural language interaction with Claude desktop as a client, automates repetitive HR tasks, reduces manual errors, and ensures a smooth, consistent employee experience from day one.

## 🛠️ Tech Stack

- Programming Language: Python
- AI & NLP: Claude
- Framework: MCP (Model Context Protocol) Server
- Used data creation is done in-memory for Employee details, Ticket Management and Leave Management.

## 🧪 Setup Instruction

To set up and run HR ASSIST, follow these steps:

- Configure claude_desktop_config.json
Add the following configuration to your claude_desktop_config.json file:

    ```json
    {
    "mcpServers": {
        "hr-assist": {
        "command": "YOUR PATH to uv COMMAND",
        "args": [
            "--directory",
            "YOUR PROJECT ROOT FOLDER PATH",
            "run",
            "server.py"
        ],
        "env": {
            "CB_EMAIL": "YOUR_EMAIL",
            "CB_EMAIL_PWD": "YOUR_APP_PASSWORD"
        }
        }
    }
    }
    ```
- Replace 'YOUR PATH to uv COMMAND' with the path where 'uv' package is downloaded in your PC.
- Replace 'YOUR PROJECT ROOT FOLDER PATH' with the root directory of this project after clonning it.
- Replace YOUR_EMAIL with your actual email.
- Replace YOUR_APP_PASSWORD with your email provider’s app-specific password (e.g., for Gmail).
- Run `uv init` and `uv add mcp[cli]` as per the video tutorial in the course.

## 📌 Usage
- Click on the `+` icon in CLaude Desktop and select the `Add from hrms-mcp-server` option, and send the request.

  <img width="880" height="553" alt="Screenshot 2025-08-11 at 11 59 02 AM" src="https://github.com/user-attachments/assets/83c0066b-559e-4bc0-b17c-05d0b147171e" />

- Alternatively, you can draft a custom prompt and let the agent take over while using specific tool in MCP server.

  <img width="893" height="658" alt="Screenshot 2025-08-11 at 11 58 03 AM" src="https://github.com/user-attachments/assets/7f05b0cb-5b0e-4804-a0f0-b6f76da64fc4" />
