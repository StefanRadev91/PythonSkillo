class MaintenanceRequest:
    def __init__(self, request_id, description, date_reported):
        self.request_id = request_id
        self.description = description
        self.status = "open"
        self.date_reported = date_reported

    def record_request(self):
        print(f"Maintenance Request {self.request_id}: {self.description} reported on {self.date_reported}")

    def update_status(self, new_status):
        self.status = new_status
        print(f"Maintenance request {self.request_id} status updated to {self.status}")

    def list_open_requests(self):
        if self.status == "open":
            print(f"Request {self.request_id}: {self.description} - Status: {self.status}")