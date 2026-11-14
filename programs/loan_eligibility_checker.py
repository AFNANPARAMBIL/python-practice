"""Demonstration loan eligibility checker; rules are illustrative only."""

def assess_loan(age, salary, score):
    if age < 21 or age > 60:
        return "Not eligible: age criteria (21–60)"
    if salary < 20000:
        return "Not eligible: monthly salary below ₹20,000"
    if score >= 750:
        return "Eligible under demo rules: Gold tier, illustrative 8% interest"
    if score >= 650:
        return "Eligible under demo rules: Silver tier, illustrative 11% interest"
    return "Not eligible: credit score below 650"


def main():
    print("----- LOAN ELIGIBILITY SYSTEM (DEMO) -----")
    name = input("Enter customer name: ").strip()
    try:
        age = int(input("Enter age: "))
        salary = float(input("Enter monthly salary: "))
        score = float(input("Enter credit score (300–900): "))
    except ValueError:
        print("Invalid input: use numbers for age, salary and credit score.")
        return
    if not 0 <= age <= 120 or salary < 0 or not 300 <= score <= 900:
        print("Invalid input: check age, salary and credit score ranges.")
        return
    print(f"Customer: {name}")
    print(assess_loan(age, salary, score))
    print("Note: This is a classroom example, not an actual loan offer.")

if __name__ == "__main__":
    main()
