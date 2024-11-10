import pytest
from apartament import Apartment
from rent import Rent
from maitenance_requests import MaintenanceRequest
from policy import Policy
from tenant_Information import TenantInformation
from building import Building
from tenant import Tenant

@pytest.fixture
def setup_system():
    tenant1 = Tenant("Stefan Radev", "123-456-7890", "2024-01-01")
    tenant2 = Tenant("McDonald Trump 2024", "987-654-3210", "2023-07-15")

    apartment1 = Apartment(101, 750, 1200)
    apartment2 = Apartment(102, 800, 1400)

    rent1 = Rent(1200, "2024-10-01")
    rent2 = Rent(1400, "2024-10-01")

    tenant_information = TenantInformation()
    tenant_information.add_tenant(tenant1, apartment1, rent1)
    tenant_information.add_tenant(tenant2, apartment2, rent2)

    policy1 = Policy(1, "No loud noises after 10 PM", "2024-01-01")
    policy2 = Policy(2, "No pets allowed", "2024-01-01")

    building = Building()
    building.add_policy(policy1)
    building.add_policy(policy2)

    return {
        "tenant1": tenant1,
        "tenant2": tenant2,
        "apartment1": apartment1,
        "apartment2": apartment2,
        "rent1": rent1,
        "rent2": rent2,
        "tenant_information": tenant_information,
        "policy1": policy1,
        "policy2": policy2,
        "building": building
    }

def test_tenant_info_display(setup_system):
    tenant1 = setup_system["tenant1"]
    tenant2 = setup_system["tenant2"]

    tenant1.display_tenant_info()
    tenant2.display_tenant_info()

def test_rent_payment(setup_system):
    rent1 = setup_system["rent1"]
    rent1.record_payment()
    assert rent1.check_payment_status() == "paid"

def test_list_overdue_tenants(setup_system):
    tenant_information = setup_system["tenant_information"]
    rent2 = setup_system["rent2"]

    rent2.payment_status = "overdue"

    tenant_information.list_overdue_tenants()

def test_policy_management(setup_system):
    building = setup_system["building"]

    building.list_policies()

    building.check_compliance(setup_system["tenant1"])

def test_maintenance_request(setup_system):
    request1 = MaintenanceRequest(1, "Leaky faucet in apartment 101", "2024-11-01")
    request1.record_request()
    request1.update_status("resolved")
    assert request1.status == "resolved"

def test_add_tenant(setup_system):
    tenant_information = setup_system["tenant_information"]

    assert len(tenant_information.tenants) == 2

    tenant3 = Tenant("Pasha Hristova", "555-1234", "2024-05-20")
    rent3 = Rent(1300, "2024-11-01")
    tenant_information.add_tenant(tenant3, setup_system["apartment1"], rent3)

    assert len(tenant_information.tenants) == 3