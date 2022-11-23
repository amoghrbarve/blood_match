from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

r = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/arb155")
print(r.status_code)
print(r.text)

read = r.json()
id_donor = read["Donor"]
id_recipient = read["Recipient"]


r_donor = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/"+id_donor)
print(r_donor.status_code)
print(r_donor.text)
donor_type = r_donor.json()


r_recipient = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/"+id_recipient)
print(r_recipient.status_code)
print(r_recipient.text)
donor_recipient = r_recipient.json()


out_data = {"Name": "arb155", "Match": "Yes"}
r_out = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check", json=out_data)
print(r_out.status_code)
print(r_out.text)
