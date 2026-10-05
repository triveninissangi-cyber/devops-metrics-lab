from datetime import datetime

def calculate_lead_time(commit, deployment):
    commit_time = datetime.fromisoformat(commit)
    deployment_time = datetime.fromisoformat(deployment)

    difference = deployment_time - commit_time

    minutes = difference.total_seconds() / 60

    print("Lead Time:", round(minutes, 2), "minutes")

commit = input("Enter commit time: ")
deployment = input("Enter deployment time: ")

calculate_lead_time(commit, deployment)
