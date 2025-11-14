import firebase_admin
from firebase_admin import credentials, analytics

# Initialize Firebase
cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

def log_event(event_name, params):
    """
    Log custom event to Firebase Analytics
    event_name: str
    params: dict
    """
    analytics.log_event(event_name, params)
    print(f"Logged event: {event_name} with {params}")

# Example usage
if __name__ == "__main__":
    log_event("product_view", {"product_id": 1, "price": 49.99})
    log_event("purchase", {"product_id": 1, "amount": 49.99})
