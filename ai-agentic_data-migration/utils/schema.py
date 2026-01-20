
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional, Literal
from datetime import datetime


class UserIntent(BaseModel):
    project_id: str
    bq_table: str  # fully qualified: project.dataset.table OR dataset.table (project inferred)
    gcs_uri_prefix: str  # e.g., gs://my-bucket/exports/mytable/run_{timestamp}/part-*.parquet
    location: str = "US"
    fmt: Literal["PARQUET"] = "PARQUET"
    compression: Literal["SNAPPY"] = "SNAPPY"
    overwrite: bool = False
    # optional filters you might apply in your own export SQL
    partition_filter: Optional[str] = None  # e.g., "_PARTITIONDATE='2025-01-01'"

class PlanStep(BaseModel):
    name: str
    tool: Literal["get_bq_table_metadata", "run_bq_export_job", "verify_latest_export"]
    args: dict

class Plan(BaseModel):
    steps: List[PlanStep]

class ValidationResult(BaseModel):
    ok: bool
    warnings: List[str] = Field(default_factory=list)
    errors: List[str] = Field(default_factory=list)

class ToolCallResult(BaseModel):
    ok: bool
    data: Optional[dict] = None
    error: Optional[str] = None

class RunResult(BaseModel):
    started_at: datetime
    finished_at: Optional[datetime] = None
    plan: Plan
    steps_results: List[ToolCallResult] = Field(default_factory=list)
    summary: Optional[str] = None
    success: Optional[bool] = None
