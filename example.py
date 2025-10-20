import requests

BASE_URL = 'https://synthea-proxy-389841612478.us-central1.run.app/'

def fetch_observations_for_subject(subject, start_date=None, end_date=None):
    url = f"{BASE_URL}Observation?subject={subject}"
    if start_date: url += f"&date=ge{start_date}"
    if end_date: url += f"&date=le{end_date}"
    
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def fetch_medication_administrations_for_subject(subject, start_date=None, end_date=None):
    url = f"{BASE_URL}MedicationAdministration?subject={subject}"
    if start_date: url += f"&effective-time=ge{start_date}"
    if end_date: url += f"&effective-time=le{end_date}"
    
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    for subject in ['a','b','c','d','e','f','g','h','i']:
        observations = fetch_observations_for_subject(subject=subject)
        med_admins = fetch_medication_administrations_for_subject(subject=subject)

        print(f"Observations for subject '{subject}': {len(observations)}")
        print(f"MedicationAdministrations for subject '{subject}': {len(med_admins)}\n")
