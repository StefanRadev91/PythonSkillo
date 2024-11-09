class Policy:
    def __init__(self, policy_id, description, effective_date):
        self.policy_id = policy_id
        self.description = description
        self.effective_date = effective_date

    def display_policy(self):
        print(f"Policy ID: {self.policy_id}")
        print(f"Description: {self.description}")
        print(f"Effective Date: {self.effective_date}")