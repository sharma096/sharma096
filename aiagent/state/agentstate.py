from typing import TypedDict, Optional, Dict, Any


class MigrationState(TypedDict):
    project: str
    dataset: str
    table: str
    bucket: str

    plan: Optional[Dict[str, Any]]
    validation: Optional[Dict[str, Any]]
    execution_result: Optional[Dict[str, Any]]

    logs: list[str]
    status: str
    