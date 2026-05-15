import json


with open(
    "data/shl_catalog.json",
    "r",
    encoding="utf-8"
) as f:

    catalog = json.load(f)


skill_map = {

    "python": [
        "python",
        "django",
        "flask",
        "backend",
        "api",
        "programming"
    ],

    "java": [
        "java",
        "spring",
        "backend",
        "programming"
    ],

    ".net": [
        ".net",
        "c#",
        "asp.net",
        
    ],

    "leadership": [
        "leadership",
        "manager",
        "communication",
        "management"
    ],

    "communication": [
        "communication",
        "interpersonal",
        "speaking",
        "soft skills"
    ],

    "finance": [
        "finance",
        "accounting",
        "bookkeeping",
        "banking"
    ],

    "sales": [
        "sales",
        "account manager",
        "customer",
        "business development"
    ],

    "developer": [
        "developer",
        "coding",
        "software",
        
    ],

    "data": [
        "data",
        "analytics",
        "sql",
        "analysis"
    ]
}


for item in catalog:

    name = item["name"].lower()

    tags = set()


    for keyword, related_tags in skill_map.items():

        if keyword in name:

            tags.update(related_tags)


    if "engineer" in name:

        tags.update([
            "engineering",
            "technical",
            "developer"
        ])


    if "manager" in name:

        tags.update([
            "leadership",
            "management"
        ])


    if "developer" in name:

        tags.update([
            "programming",
            "software"
        ])


    if not tags:

        tags.update([
            "general",
            "assessment"
        ])


    item["tags"] = list(tags)


with open(
    "data/shl_catalog.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        catalog,
        f,
        indent=4
    )


print("Tags added successfully")