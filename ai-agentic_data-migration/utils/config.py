
import os
from dotenv import load_dotenv
load_dotenv()

MCP_SERVER_URL = os.getenv("MCP_SERVER_URL", "http://127.0.0.1:9000")
DEFAULT_PROJECT_ID = os.getenv("GCP_PROJECT_ID", "agenticaisolution")
DEFAULT_LOCATION = os.getenv("BQ_LOCATION", "US")
ORCHESTRATOR_ENV = os.getenv("ORCHESTRATOR_ENV", "dev")
