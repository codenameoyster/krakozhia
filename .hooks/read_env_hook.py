import json
import sys

tool_args = json.load(sys.stdin)
read_path = tool_args.get("tool_input", {}).get("file_path", "") or tool_args.get(
    "tool_input", {}
).get("path", "")
if ".env" in read_path:
    print("Error: Attempting to read .env file, which is not allowed.")
    sys.exit(2)
