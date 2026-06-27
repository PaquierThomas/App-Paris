import dlt
from source import classement_coupe_du_monde


pipeline = dlt.pipeline(
    pipeline_name="sportsdb_cdm",
    destination=dlt.destinations.postgres(
        "postgresql://tsadmin:strongpassword123@localhost:5433/tsdb"
    ),
    dataset_name="coupe_du_monde",
    dev_mode=True       # ← repart de zéro à chaque fois
)

if __name__ == "__main__":
    load_info = pipeline.run(classement_coupe_du_monde())
    print(load_info)