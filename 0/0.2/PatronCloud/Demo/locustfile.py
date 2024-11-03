from locust import HttpUser, task, between
import json
import uuid

class AppointmentUser(HttpUser):
    wait_time = between(1, 3) 
    appointment_ids = []  
    @task
    def create_appointment(self):
        appointment_data = {
            'id': str(uuid.uuid4()),  
        }
        response = self.client.post('/appointments', json=appointment_data)
        

        if response.status_code == 201:  
            self.appointment_ids.append(appointment_data['id'])
