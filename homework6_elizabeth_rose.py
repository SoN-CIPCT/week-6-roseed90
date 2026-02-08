

# -----------------------------
# 1) Conditional Lists
# -----------------------------

# List of existing website users (5+ usernames)
web_users = ["wounddoc", "nightshiftNP", "surgqueen", "chartmaster", "debridePro"]

# New users attempting to register (5 usernames; 2 overlap with web_users, 3 unique)
new_users = ["surgqueen", "chartmaster", "freshstartMD", "woundwizard", "snfrounds"]

# Make username checks case-insensitive (common website behavior)
web_users_lower = [user.lower() for user in web_users]

for user in new_users:
    if user.lower() in web_users_lower:
        print("This user name is already in use. Please choose a different user name.")
    else:
        print("This user name is available.")


print("\n" + "-" * 40 + "\n")


# -----------------------------
# 2) Nested Dictionaries
# -----------------------------

cities = {
    "Seattle": {
        "country": "United States",
        "population": 750000,  # approximate city population
        "fact": "Seattle is known as the 'Emerald City' and is home to the Space Needle."
    },
    "Paris": {
        "country": "France",
        "population": 2160000,  # approximate city population
        "fact": "Paris is famous for the Eiffel Tower and is often called the 'City of Light'."
    },
    "Tokyo": {
        "country": "Japan",
        "population": 14000000,  # approximate city population (Tokyo proper)
        "fact": "Tokyo is one of the largest metropolitan areas in the world."
    }
}

# Print in the requested format:
# City: <city>
# Country: <country>
# Population: <population>
# Fact: <fact>
for city_name, info in cities.items():
    print(f"City: {city_name}")
    print(f"Country: {info['country']}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}")
    print()  # blank line between cities
