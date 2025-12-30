
from pathlib import Path

ROOT = Path(__file__).parents[2]

def load_system_prompt(prompt_file; str = "SYSTEM_PROMPT.md" ):

    sys_prompt_path = ROOT /"source"/ "system" / "prompt" / prompt_file 

    try:
        with open(sys_prompt_path, "r", encoding="utf-8") as file:
            return file.read()

    except FileNotFoundError:
        print(f"Error: {sys_prompt_path} not found")

    except Exception as e:
        print(f"Error: {e}")

    return ""



