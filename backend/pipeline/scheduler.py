import schedule
import time
import dlt
from source import coupe_du_monde

def run_pipeline():
    print("🔄 Extraction en cours...")
    pipeline = dlt.pipeline(
        pipeline_name="coupe_du_monde",
        destination=dlt.destinations.postgres(
            "postgresql://tsadmin:strongpassword123@localhost:5433/tsdb"
        ),
        dataset_name="coupe_du_monde",
    )
    load_info = pipeline.run(coupe_du_monde())
    print(f"✅ Terminé : {load_info}")

if __name__ == "__main__":
    # Lance une première fois immédiatement
    run_pipeline()

    schedule.every(10).minutes.do(run_pipeline)

    print("⏰ Scheduler démarré, Ctrl+C pour arrêter")
    while True:
        schedule.run_pending()
        time.sleep(1)