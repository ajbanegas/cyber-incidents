class IncidentRepositoryMemory:
    def __init__(self):
        self.incidents = {}

    def save(self, incident):
        self.incidents[incident.id] = incident

    def find_all(self):
        return list(self.incidents.values())

    def find_by_id(self, incident_id):
        return self.incidents.get(incident_id)
