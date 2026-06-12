from datetime import date

# Simple in-memory representation of contracts (mirrors iSheet sampleRows)
contracts = [
    {
        "Contract ID": "C-2026-001",
        "Contract Type": "MSA",
        "Risk Level": "High",
        "Status": "Intake",
        "Assigned Reviewer": None
    },
    {
        "Contract ID": "C-2026-004",
        "Contract Type": "NDA",
        "Risk Level": "Low",
        "Status": "Intake",
        "Assigned Reviewer": None
    }
]

def assign_reviewer(contract):
    if contract["Risk Level"] == "High":
        return "senior.reviewer@company.com"
    if contract["Contract Type"] in ("MSA", "License"):
        return "commercial.reviewer@company.com"
    return "nda.reviewer@company.com"

def trigger_on_intake(contract):
    print(f"[WORKFLOW] New contract received: {contract['Contract ID']}")
    reviewer = assign_reviewer(contract)
    contract["Assigned Reviewer"] = reviewer
    contract["Status"] = "In Review"
    print(f"[ACTION] Assigned to {reviewer} and moved to 'In Review'.")

def trigger_on_status_change(contract, new_status):
    old_status = contract["Status"]
    contract["Status"] = new_status
    print(f"[WORKFLOW] Status change for {contract['Contract ID']}: {old_status} -> {new_status}")
    if new_status == "Approved":
        print(f"[NOTIFY] Business owner: Contract {contract['Contract ID']} approved on {date.today()}.")
    elif new_status == "Rejected":
        print(f"[NOTIFY] Business owner: Contract {contract['Contract ID']} rejected. Please review comments.")

if __name__ == "__main__":
    # Simulate intake triggers
    for c in contracts:
        trigger_on_intake(c)

    # Simulate a status change
    trigger_on_status_change(contracts[0], "Approved")
