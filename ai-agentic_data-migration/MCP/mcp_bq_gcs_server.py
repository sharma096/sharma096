from mcp.server.fastmcp import FastMCP

from google.cloud import bigquery, storage

import pyarrow as pa

import pyarrow.parquet as pq

import pandas as pd

import uuid

mcp = FastMCP("bq-gcs-migration")

@mcp.tool()

def bq_to_gcs_parquet(project: str, dataset: str, table: str, bucket: str):

    bq = bigquery.Client(project=project)

    gcs = storage.Client()

    query = f"SELECT * FROM `{project}.{dataset}.{table}`"

    df = bq.query(query).to_dataframe()

    file_name = f"export_{uuid.uuid4()}.parquet"

    local_path = f"/tmp/{file_name}"

    pq.write_table(pa.Table.from_pandas(df), local_path)

    bucket_ref = gcs.bucket(bucket)

    blob = bucket_ref.blob(f"exports/{file_name}")

    blob.upload_from_filename(local_path)

    return {

        "rows": len(df),

        "gcs_path": f"gs://{bucket}/exports/{file_name}"

    }

def run_bq_to_gcs(project, dataset, table, bucket):
   return bq_to_gcs_parquet(
       project=project,
       dataset=dataset,
       table=table,
       bucket=bucket
   )
if __name__ == "__main__":

    mcp.run()
 