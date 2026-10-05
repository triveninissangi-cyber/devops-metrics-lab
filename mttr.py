from datetime import datetime

incidents = [
    {
        "name": "Database Failure",
        "start": "2026-10-04T10:00:00",
        "recovery": "2026-10-04T10:30:00"
    },
    {
        "name": "Server Failure",
        "start": "2026-10-04T11:00:00",
        "recovery": "2026-10-04T11:20:00"
    },
    {
        "name": "Application Error",
        "start": "2026-10-04T12:00:00",
        "recovery": "2026-10-04T13:10:00"
    }
]

total_minutes = 0

for incident in incidents:
    start = datetime.fromisoformat(incident["start"])
    recovery = datetime.fromisoformat(incident["recovery"])

    duration = (recovery - start).total_seconds() / 60

    total_minutes += duration

    print(incident["name"], ":", duration, "minutes")

mttr = total_minutes / len(incidents)

print("Total Recovery Time:", total_minutes, "minutes")
print("MTTR:", round(mttr, 2), "minutes")