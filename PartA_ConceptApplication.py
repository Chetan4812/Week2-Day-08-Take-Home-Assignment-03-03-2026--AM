def validate_inputs(entrance_score, gpa, has_recommendation, category, extracurricular_score):
    # Validate entrance score
    if not (0 <= entrance_score <= 100):
        return False, "Entrance score must be between 0 and 100."

    # Validate GPA
    if not (0 <= gpa <= 10):
        return False, "GPA must be between 0 and 10."

    # Validate recommendation
    if has_recommendation not in ["yes", "no"]:
        return False, "Recommendation must be 'yes' or 'no'."

    # Validate category
    if category not in ["general", "obc", "sc_st"]:
        return False, "Category must be 'general', 'obc', or 'sc_st'."

    # Validate extracurricular score
    if not (0 <= extracurricular_score <= 10):
        return False, "Extracurricular score must be between 0 and 10."

    return True, None


def admission_decision(entrance_score, gpa, has_recommendation, category, extracurricular_score):

    # Merit Rule (Auto Admit with Scholarship)
    if entrance_score >= 95:
        return (
            "\nADMITTED (Scholarship)\n"
            f"Reason: Entrance score {entrance_score} ≥ 95 (Merit-based auto admission)."
        )

    # GPA Requirement
    if gpa < 7.0:
        return (
            "\nREJECTED\n"
            f"Reason: GPA requirement not met ({gpa} < 7.0)."
        )

    # Bonus Rules
    bonus = 0
    bonus_details = []

    if has_recommendation == "yes":
        bonus += 5
        bonus_details.append("+5 (recommendation)")

    if extracurricular_score > 8:
        bonus += 3
        bonus_details.append("+3 (extracurricular)")

    effective_score = entrance_score + bonus

    category_cutoffs = {
        "general": 75,
        "obc": 65,
        "sc_st": 55
    }

    required_cutoff = category_cutoffs[category]

    # Final Decision
    if effective_score >= required_cutoff:
        result = "ADMITTED (Regular)"
        reason = (
            f"Meets {category.capitalize()} cutoff "
            f"({effective_score} ≥ {required_cutoff}) "
            f"and GPA requirement ({gpa} ≥ 7.0)."
        )
    elif effective_score >= required_cutoff - 5:
        result = "WAITLISTED"
        reason = (
            f"Close to {category.capitalize()} cutoff "
            f"({effective_score} < {required_cutoff})."
        )
    else:
        result = "REJECTED"
        reason = (
            f"Entrance score below {category.capitalize()} cutoff "
            f"({effective_score} < {required_cutoff})."
        )

    bonus_info = " + ".join(bonus_details) if bonus_details else "No bonus applied"

    return (
        f"\nBonus Applied: {bonus_info}\n"
        f"Effective Score: {effective_score}\n"
        f"\n{result}\n"
        f"Reason: {reason}"
    )


# ===== MAIN PROGRAM =====
if __name__ == "__main__":

    try:
        entrance_score = float(input("Enter Entrance Score (0-100): "))
        gpa = float(input("Enter GPA (0-10): "))
        has_recommendation = input("Has Recommendation (yes/no): ").strip().lower()
        category = input("Category (general/obc/sc_st): ").strip().lower()
        extracurricular_score = float(input("Extracurricular Score (0-10): "))

        # Validate inputs
        valid, error = validate_inputs(
            entrance_score, gpa, has_recommendation, category, extracurricular_score
        )

        if not valid:
            print("\nREJECTED")
            print("Reason:", error)
        else:
            result = admission_decision(
                entrance_score, gpa, has_recommendation, category, extracurricular_score
            )
            print(result)

    except ValueError:
        print("\nREJECTED")
        print("Reason: Invalid numeric input. Please enter numbers in correct format.")