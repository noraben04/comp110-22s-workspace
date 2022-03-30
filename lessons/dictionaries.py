"""Demonstrations of dictionary capabilities."""


# Declaring the type of a dictionary
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()

# Set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NSCU"] = 26150

# Print a dictionary literal representation
print(schools)

# Access a vlaue by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")

# Remove a key-value pair from a dictonary
# by its key.
schools.pop("Duke")

# Test for the existence of a key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

print(schools)