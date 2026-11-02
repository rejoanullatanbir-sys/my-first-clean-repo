# My First Clean Repository

A small Python program that reads its settings from a `.env` file. It prints the app name and confirms that the API key was loaded, without ever printing the key itself.

## Requirements

- Python 3.8 or newer
- Git

## Setup

1. Clone the repository and go into the folder:

   ```bash
   git clone https://github.com/<your-username>/my-first-clean-repo.git
   cd my-first-clean-repo
   ```

2. Create and activate a virtual environment:

   **macOS / Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   **Windows (PowerShell)**
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Copy the example file to `.env`:

```bash
cp .env.example .env        # macOS / Linux
copy .env.example .env      # Windows
```

Then open `.env` and fill in the values:

| Variable   | Required | What it is |
|------------|----------|------------|
| `APP_NAME` | Yes      | The name the program prints. Any text works, e.g. `My First Clean Repo`. |
| `API_KEY`  | Yes      | A secret key. For this demo any value works, e.g. `abc123`. The program only checks that it exists and never prints it. |

`.env` is listed in `.gitignore`, so your real values stay on your computer and are never committed.

## Run

```bash
python main.py
```

Expected output:

```
App name: My First Clean Repo
API_KEY loaded: True
```

If a variable is missing, the program stops with a clear message instead of crashing:

```
Error: missing required setting(s): API_KEY
Fix: copy .env.example to .env and fill in the values.
```
