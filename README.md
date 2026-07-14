# 🚀 Job Hunter Agent MVP

An AI-powered Job Hunter Agent that automatically searches jobs from multiple providers, filters relevant opportunities, and exports the results to Excel.

This project demonstrates how AI agents can automate job discovery using a modular provider architecture and a local Large Language Model (LLM).

---

## ✨ Features

- 🔍 Search jobs from multiple job providers
- 🤖 AI-powered job filtering using a Local LLM
- 📄 Export job listings to Excel
- 📅 Includes Job Posted Date
- 📅 Includes Job Expiry Date (if available)
- ⚡ Fast and lightweight Python application
- 🧩 Modular provider architecture for easy extension
- 📊 Clean Excel output for job tracking

---

# 🛠️ Tech Stack

- Python 3.11
- FastAPI
- Pandas
- OpenPyXL
- Pydantic
- Requests
- Ollama (Local LLM)

---

# 📂 Project Structure

```
job-hunter-agent-mvp-partial/
│
├── providers/         # Job provider integrations
├── services/          # Business logic
├── utils/             # Utility functions
├── exports/           # Generated Excel reports
├── models/            # Data models
├── app.py             # Application entry point
├── config.py          # Configuration
├── requirements.txt
└── README.md
```

---

# 📋 Prerequisites

Before running the project, make sure you have:

- Python 3.11
- Git
- Ollama installed
- A local LLM downloaded in Ollama

---

# ⚠️ Python Version

This project uses **Pydantic**, which may have compatibility issues with newer Python versions.

**Recommended version: Python 3.11**

---

# 🐍 Install Python 3.11 (Windows)

```powershell
py install 3.11
```

Verify installation:

```powershell
py -3.11 --version
```

---

# 📦 Create Virtual Environment

```powershell
py -3.11 -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\activate
```

---

# ⬆️ Upgrade pip

```powershell
python -m pip install --upgrade pip
```

---

# 📥 Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

---

# 🤖 Install Ollama

Download and install Ollama from:

https://ollama.com/download

Verify installation:

```bash
ollama --version
```

---

# 📥 Download a Local LLM

Example:

```bash
ollama pull llama3.2
```

or

```bash
ollama pull qwen3
```

Ensure the model configured in your project is available locally before running the application.

---

# ▶️ Run the Application

Start the application with:

```bash
python app.py
```

If everything is configured correctly, the application will start and begin fetching jobs based on your configured providers.

---

---

# 📸 Sample Output

After running the application:

```
python app.py
```

The console output will look similar to:

====================================================
🚀 Job Hunter Agent Started
====================================================

🔍 Fetching jobs from RemoteOK...
✅ Retrieved 25 jobs

🔍 Fetching jobs from Greenhouse...
✅ Retrieved 18 jobs

🔍 Fetching jobs from Lever...
✅ Retrieved 12 jobs

🤖 Filtering jobs using Local LLM...

✅ Total Jobs Processed : 55
✅ Matching Jobs Found : 21

📄 Exporting results to Excel...

✅ Report saved successfully!

Location:
exports/job_report_2026-07-14.xlsx

🎉 Job search completed successfully.
```

---

# 📊 Sample Excel Output

| Company | Job Title | Location | Employment Type | Posted Date | Expiry Date | Apply Link |
|---------|-----------|----------|-----------------|------------|-------------|------------|
| RemoteOK | AI Engineer | Remote | Full-Time | 14-Jul-2026 | 14-Aug-2026 | https://example.com/job1 |
| OpenAI | Full Stack Engineer | Remote | Full-Time | 13-Jul-2026 | 13-Aug-2026 | https://example.com/job2 |
| Stripe | Software Engineer | Bangalore | Full-Time | 12-Jul-2026 | N/A | https://example.com/job3 |
| Atlassian | Frontend Engineer | Hyderabad | Full-Time | 11-Jul-2026 | 11-Aug-2026 | https://example.com/job4 |

The generated Excel report contains:

- Company Name
- Job Title
- Location
- Employment Type
- Posted Date
- Expiry Date (if available)
- Apply URL

Reports are automatically saved in the `exports/` directory.

---
# 🔧 Extending the Project

Adding a new job provider is simple:

1. Create a new provider inside the `providers/` directory.
2. Implement the provider interface.
3. Register it in the application.

This modular architecture makes it easy to support additional job platforms.

---

# 🚀 Roadmap

- ✅ RemoteOK Integration
- ⏳ LinkedIn Integration
- ⏳ Naukri Integration
- ⏳ Greenhouse Jobs
- ⏳ Lever Jobs
- ⏳ AI Resume Matching
- ⏳ Job Match Score
- ⏳ Daily Scheduled Job Search
- ⏳ Email Notifications
- ⏳ Multi-Agent Workflow
- ⏳ Web Dashboard

---

# 🤝 Contributing

Contributions, suggestions, and feature requests are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Submit a Pull Request

---

# 📜 License

This project is licensed under the MIT License.

---

If you found this project helpful, consider giving it a ⭐ on GitHub!
