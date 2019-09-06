import json
import requests


r = requests.get('http://localhost:7777/v1/doctors/' + "Jessica Wong")
data = r.json()
print = data

args = ["a","v","c","e","q","t"]
payload = {"doctor_name":' '.join(args[4:]), "timesolt":' '.join(args[:4])}
result = {}
massage = f"Reservation has been completed\nDoctor name:{result['doctor_name']}\nTime:{result['timesolt']}\nReservation number:{result['reservation_id']}"
