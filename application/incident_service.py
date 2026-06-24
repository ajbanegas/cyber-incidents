class IncidentService:
    def __init__(self, repository):
        self.repository = repository

    def create_incident(self, incident):
        self.repository.save(incident)

    def list_incidents(self):
        return self.repository.find_all()

    def find_incident(self, incident_id):
        return self.repository.find_by_id(incident_id)

    def change_status(self, incident_id, new_status):
        incident = self.repository.find_by_id(incident_id)

        if incident is None:
            return None

        incident.status = new_status
        self.repository.save(incident)
        return incident
