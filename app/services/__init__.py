from .person_service import PersonService

class ServiceManager:
    def __init__(self):
        self.person_service = PersonService()

service_manager = ServiceManager()