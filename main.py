from domain.incident import Incident
from application.incident_service import IncidentService
from infrastructure.incident_repository_json import IncidentRepositoryMemory

repository = IncidentRepositoryMemory()
service = IncidentService(repository)
incident = Incident(
    id=1,
    title="Intento de acceso no autorizado",
    description="Se detectaron múltiples intentos fallidos de login",
    level="alto"
)
service.create_incident(incident)

# prueba de cambio de estado de la incidencia
service.change_status(1, "en análisis")
print(service.find_incident(1))

for item in service.list_incidents():
    print(item)
