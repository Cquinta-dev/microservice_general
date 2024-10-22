from .country_service import CountryService
from .departament_service import DepartamentService
from .municipality_service import MunicipalityService
from .currency_service import CurrencyService
from .company_service import CompanyService
from .person_service import PersonService

class ServiceManager:
    
    def __init__(self):
        self.country_service = CountryService()
        self.departament_service = DepartamentService()
        self.municipality_service = MunicipalityService()
        self.currency_service = CurrencyService()
        self.company_service = CompanyService()
        self.person_service = PersonService()

service_manager = ServiceManager()