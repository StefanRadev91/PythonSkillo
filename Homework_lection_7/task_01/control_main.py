from apartament import Apartment
from rent import Rent
from maitenance_requests import MaintenanceRequest
from policy import Policy
from tenant_Information import TenantInformation
from building import Building
from tenant import Tenant


# Create some instances of the classes
tenant1 = Tenant("John Doe", "123-456-7890", "2024-01-01")
tenant2 = Tenant("Jane Smith", "987-654-3210", "2023-07-15")

apartment1 = Apartment(101, 750, 1200)
apartment2 = Apartment(102, 800, 1400)

rent1 = Rent(1200, "2024-10-01")
rent2 = Rent(1400, "2024-10-01")

tenant_information = TenantInformation()
tenant_information.add_tenant(tenant1, apartment1, rent1)
tenant_information.add_tenant(tenant2, apartment2, rent2)

# Create and manage building policies
policy1 = Policy(1, "No loud noises after 10 PM", "2024-01-01")
policy2 = Policy(2, "No pets allowed", "2024-01-01")

building = Building()
building.add_policy(policy1)
building.add_policy(policy2)

tenant1.display_tenant_info()
tenant2.display_tenant_info()
apartment1.display_apartment_details()
apartment2.display_apartment_details()

rent1.record_payment()

tenant_information.list_overdue_tenants()

request1 = MaintenanceRequest(1, "Leaky faucet in apartment 101", "2024-11-01")
request1.record_request()
request1.update_status("resolved")

building.list_policies()

building.check_compliance(tenant1)