import dlt
from source import coupe_du_monde


pipeline = dlt.pipeline(
    pipeline_name="coupe_du_monde",
    destination=dlt.destinations.postgres(
        "postgresql://tsadmin:strongpassword123@localhost:5433/tsdb"
    ),
    dataset_name="coupe_du_monde",
)

if __name__ == "__main__":
    load_info = pipeline.run(coupe_du_monde())
    print(load_info)