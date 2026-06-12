from collections import Counter
from datetime import datetime

sample_rows = [
    {
        "Contract ID": "C-2026-001",
        "Status": "In Review",
        "Risk Level": "High",
        "Intake Date": "2026-06-10",
        "Actual Completion Date": None
    },
    {
        "Contract ID": "C-2026-002",
        "Status": "Approved",
        "Risk Level": "Low",
        "Intake Date": "2026-06-05",
        "Actual Completion Date": "2026-06-06"
    },
    {
        "Contract ID": "C-2026-003",
        "Status": "Intake",
        "Risk Level": "Medium",
        "Intake Date": "2026-06-12",
        "Actual Completion Date": None
    }
]

def parse_date(value):
    if not value:
        return None
    return datetime.strptime(value, "%Y-%m-%d").date()

def contracts_by_status(rows):
    return Counter(row["Status"] for row in rows)

def average_turnaround(rows):
    durations = []
    for row in rows:
        start = parse_date(row["Intake Date"])
        end = parse_date(row["Actual Completion Date"])
        if start and end:
            durations.append((end - start).days)
    if not durations:
        return None
    return sum(durations) / len(durations)

def high_risk_in_progress(rows):
    return [
        row for row in rows
        if row["Risk Level"] == "High" and row["Status"] in ("Intake", "In Review")
    ]

if __name__ == "__main__":
    status_counts = contracts_by_status(sample_rows)
    avg_tat = average_turnaround(sample_rows)
    high_risk = high_risk_in_progress(sample_rows)

    print("=== Contract Review Dashboard (Simulated) ===\n")
    print("Contracts by Status:")
    for status, count in status_counts.items():
        print(f" - {status}: {count}")

    print("\nAverage Turnaround Time (completed contracts):")
    if avg_tat is None:
        print(" - Not enough completed contracts to calculate.")
    else:
        print(f" - {avg_tat:.1f} days")

    print("\nHigh-Risk Contracts In Progress:")
    if not high_risk:
        print(" - None")
    else:
        for row in high_risk:
            print(f" - {row['Contract ID']} (Status: {row['Status']})")
