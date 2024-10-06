import json
from datetime import datetime
from bson import ObjectId

# Define the dictionary
data = {
    "booking_id": 12345,
    "arrival_date": "2025-03-11T14:00:00.000+10:00",
    "departure_date": "2025-03-13T10:00:00.000+10:00",
    "listing_id": "10083468",  # Reference to "Be Happy in Porto"
    "client_id": str(ObjectId("670232f5563825de0da55f81")),  # Reference to Brodie Mackrell
    "deposit_paid": 10,
    "balance_due": 20,
    "balance_due_date": "2025-03-01T00:00:00.000+10:00",
    "number_of_guests": 2,
    "guests": [
        {
            "name": "Brodie",
            "age": 44
        },
        {
            "name": "John",
            "age": 44
        }
    ]
}

# Convert dictionary to JSON and write to a file
with open("booking.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("Data saved to booking1.json")
