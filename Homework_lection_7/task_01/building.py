class Building:
    def __init__(self):
        self.policies = []

    def add_policy(self, policy):
        self.policies.append(policy)

    def list_policies(self):
        print("Building Policies:")
        for policy in self.policies:
            policy.display_policy()

    def check_compliance(self, tenant):
        print(f"Checking compliance for {tenant.name}: All tenants must comply with building policies.")