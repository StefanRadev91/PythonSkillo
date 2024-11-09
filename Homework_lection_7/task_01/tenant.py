class Tenant:
    def __init__(self, name, contact_info, lease_start_date):
        self.name = name
        self.contact_info = contact_info
        self.lease_start_date = lease_start_date

    def display_tenant_info(self):
        print(f"Tenant: {self.name}")
        print(f"Contact Info: {self.contact_info}")
        print(f"Lease Start Date: {self.lease_start_date}")

    def update_contact_info(self, new_contact_info):
        self.contact_info = new_contact_info