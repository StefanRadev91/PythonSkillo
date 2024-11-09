class TenantInformation:
    def __init__(self):
        self.tenants = []

    def add_tenant(self, tenant, apartment, rent):
        tenant_data = {
            "tenant": tenant,
            "apartment": apartment,
            "rent": rent
        }
        self.tenants.append(tenant_data)

    def update_lease_history(self, tenant, new_lease_start_date):
        for tenant_data in self.tenants:
            if tenant_data["tenant"] == tenant:
                tenant_data["tenant"].lease_start_date = new_lease_start_date
                print(f"Lease start date updated for {tenant.name}")
                return
        print(f"Tenant {tenant.name} not found.")

    def find_tenant(self, tenant_name):
        for tenant_data in self.tenants:
            if tenant_data["tenant"].name == tenant_name:
                return tenant_data
        return None

    def list_overdue_tenants(self):
        print("Overdue Rent Payments:")
        for tenant_data in self.tenants:
            if tenant_data["rent"].check_payment_status() == "overdue":
                tenant_data["tenant"].display_tenant_info()
                tenant_data["rent"].check_payment_status()