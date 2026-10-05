import csv
import os
from datetime import datetime, timedelta

FILE = "data/deployments.csv"

os.makedirs("data", exist_ok=True)

def record_deployment(status):
    now = datetime.now()

    file_exists = os.path.exists(FILE)

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["time", "status"])

        writer.writerow([now.isoformat(), status])

    print("Deployment recorded:", status)

def calculate_frequency():
    if not os.path.exists(FILE):
        print("No deployment records found")
        return

    with open(FILE, newline="") as f:
        reader = csv.DictReader(f)
        deployments = list(reader)

    week_ago = datetime.now() - timedelta(days=7)

    successful = [
        row for row in deployments
        if row["status"] == "SUCCESS"
        and datetime.fromisoformat(row["time"]) >= week_ago
    ]

    print("Successful deployments in last 7 days:",
          len(successful))
    print("Deployment frequency per day:",
          round(len(successful) / 7, 2))

print("1. Record successful deployment")
print("2. Record failed deployment")
print("3. Calculate frequency")

choice = input("Enter choice: ")

if choice == "1":
    record_deployment("SUCCESS")
elif choice == "2":
    record_deployment("FAILED")
elif choice == "3":
    calculate_frequency()
else:
    print("Invalid choice")