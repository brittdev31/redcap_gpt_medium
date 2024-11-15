# Create a DataFrame for the PHQ-9 survey
phq9_data = {
    "Variable / Field Name": [
        "phq9_q1", "phq9_q2", "phq9_q3", "phq9_q4", "phq9_q5",
        "phq9_q6", "phq9_q7", "phq9_q8", "phq9_q9", "phq9_difficulty"
    ],
    "Form Name": [
        "phq9", "phq9", "phq9", "phq9", "phq9",
        "phq9", "phq9", "phq9", "phq9", "phq9"
    ],
    "Section Header": [
        "PHQ-9 Questions", None, None, None, None,
        None, None, None, None, None
    ],
    "Field Type": [
        "radio", "radio", "radio", "radio", "radio",
        "radio", "radio", "radio", "radio", "radio"
    ],
    "Field Label": [
        "Little interest or pleasure in doing things",
        "Feeling down, depressed, or hopeless",
        "Trouble falling or staying asleep, or sleeping too much",
        "Feeling tired or having little energy",
        "Poor appetite or overeating",
        "Feeling bad about yourself or that you are a failure",
        "Trouble concentrating on things",
        "Moving or speaking slowly, or being fidgety/restless",
        "Thoughts of being better off dead or hurting yourself",
        "Difficulty in work, home, or with others"
    ],
    "Choices, Calculations, OR Slider Labels": [
        "0, Not at all | 1, Several days | 2, More than half the days | 3, Nearly every day",
        "0, Not at all | 1, Several days | 2, More than half the days | 3, Nearly every day",
        "0, Not at all | 1, Several days | 2, More than half the days | 3, Nearly every day",
        "0, Not at all | 1, Several days | 2, More than half the days | 3, Nearly every day",
        "0, Not at all | 1, Several days | 2, More than half the days | 3, Nearly every day",
        "0, Not at all | 1, Several days | 2, More than half the days | 3, Nearly every day",
        "0, Not at all | 1, Several days | 2, More than half the days | 3, Nearly every day",
        "0, Not at all | 1, Several days | 2, More than half the days | 3, Nearly every day",
        "0, Not at all | 1, Several days | 2, More than half the days | 3, Nearly every day",
        "0, Not difficult at all | 1, Somewhat difficult | 2, Very difficult | 3, Extremely difficult"
    ],
    "Field Note": [
        None, None, None, None, None, None, None, None, None, None
    ],
    "Text Validation Type OR Show Slider Number": [None] * 10,
    "Text Validation Min": [None] * 10,
    "Text Validation Max": [None] * 10,
    "Identifier?": [None] * 10,
    "Branching Logic (Show field only if...)": [None] * 10,
    "Required Field?": ["y"] * 10,
    "Custom Alignment": [None] * 10,
    "Question Number (surveys only)": list(range(1, 11)),
    "Matrix Group Name": [None] * 10,
    "Matrix Ranking?": [None] * 10,
    "Field Annotation": [None] * 10
}

# Convert to DataFrame
phq9_df = pd.DataFrame(phq9_data)

# Save to CSV
output_path = "/mnt/data/PHQ9_REDCap_DataDictionary.csv"
phq9_df.to_csv(output_path, index=False)

output_path

# Add a calculated field for the PHQ-9 Total Score
calculated_field = {
    "Variable / Field Name": ["phq9_total_score"],
    "Form Name": ["phq9"],
    "Section Header": [None],
    "Field Type": ["calc"],
    "Field Label": ["PHQ-9 Total Score"],
    "Choices, Calculations, OR Slider Labels": [
        "[phq9_q1] + [phq9_q2] + [phq9_q3] + [phq9_q4] + [phq9_q5] + [phq9_q6] + [phq9_q7] + [phq9_q8] + [phq9_q9]"
    ],
    "Field Note": [None],
    "Text Validation Type OR Show Slider Number": [None],
    "Text Validation Min": [None],
    "Text Validation Max": [None],
    "Identifier?": [None],
    "Branching Logic (Show field only if...)": [None],
    "Required Field?": ["y"],
    "Custom Alignment": [None],
    "Question Number (surveys only)": [None],
    "Matrix Group Name": [None],
    "Matrix Ranking?": [None],
    "Field Annotation": [None]
}

# Append the calculated field to the PHQ-9 DataFrame
calculated_field_df = pd.DataFrame(calculated_field)
phq9_df = pd.concat([phq9_df, calculated_field_df], ignore_index=True)

# Save the updated DataFrame to a new CSV
updated_output_path = "/mnt/data/PHQ9_REDCap_DataDictionary_Updated.csv"
phq9_df.to_csv(updated_output_path, index=False)

updated_output_path
