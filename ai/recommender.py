# ai/recommender.py

# Dummy volunteer dataset
volunteers = [
    {
        "name": "Aisha",
        "skills": ["teaching", "mentoring", "english"],
        "location": "Hyderabad",
        "causes": ["education", "children"]
    },
    {
        "name": "Riya",
        "skills": ["first aid", "rescue", "counseling"],
        "location": "Chennai",
        "causes": ["disaster relief", "healthcare"]
    },
    {
        "name": "Fatima",
        "skills": ["fundraising", "social media", "organizing"],
        "location": "Delhi",
        "causes": ["women empowerment", "fundraising", "community"]
    },
    {
        "name": "Sara",
        "skills": ["plantation", "awareness", "sustainability"],
        "location": "Mumbai",
        "causes": ["climate change", "environment"]
    }
]


def match_volunteer(description: str):
    """
    Simple keyword-based matching:
    - Scan NGO description for keywords
    - Find the volunteer whose skills/causes overlap the most
    - Return the best match
    """
    description = description.lower()
    best_match = None
    best_score = 0

    for volunteer in volunteers:
        score = 0
        # Check for skill overlap
        for skill in volunteer["skills"]:
            if skill in description:
                score += 2  # give higher weight to skills
        # Check for cause overlap
        for cause in volunteer["causes"]:
            if cause in description:
                score += 1

        if score > best_score:
            best_score = score
            best_match = volunteer

    if best_match:
        return f"Best match: {best_match['name']} (Skills: {', '.join(best_match['skills'])}, Location: {best_match['location']})"
    else:
        return "No specific match found, but volunteers are ready to help."
    