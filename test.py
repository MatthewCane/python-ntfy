from python_ntfy import NtfyClient
from dotenv import load_dotenv

load_dotenv()
print(NtfyClient(topic="test").send(message="test"))
