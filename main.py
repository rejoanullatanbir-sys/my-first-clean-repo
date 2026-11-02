"""A tiny program that reads its settings from a .env file.

It shows that configuration comes from the environment,
not from values hard-coded in this source file.
"""

import os
import sys

from dotenv import load_dotenv

# Step 1: read the .env file and put its values into the environment.
load_dotenv()

# Step 2: read the two variables we need.
app_name = os.getenv("APP_NAME")
api_key = os.getenv("API_KEY")

# Step 3: if something is missing, stop with a clear message (no crash).
missing = []
if not app_name:
    missing.append("APP_NAME")
if not api_key:
    missing.append("API_KEY")

if missing:
    print("Error: missing required setting(s): " + ", ".join(missing))
    print("Fix: copy .env.example to .env and fill in the values.")
    sys.exit(1)

# Step 4: print the plain setting, but NEVER print the secret itself.
print(f"App name: {app_name}")
print(f"API_KEY loaded: {api_key is not None}")
