Blood Match Mini Project

Write a program the completes the following tasks:

* Get the IDs for two patients by making a GET request to `URL/get_patients/<name>`.  
Replace `<name>` with your Duke Net ID.  
This request will return a dictionary
in the following format:  
`{"Recipient": "<ID1>", "Donor": "<ID2>"}`.
* Obtain the blood type of the two patients by making GET requests to 
`URL/get_blood_type/<id>` where `<id>` is replaced by either `<ID1>` or `<ID2>`
from above.  
This request will return a string with the blood type of the given patient.
* Calculate whether it is an acceptable match for the recipient to receive
blood from the donor.
* Check your result by making a POST request to `URL/match_check`.  Send a
JSON with the following format:  
`{"Name": "<name>", "Match":  "<answer>"}`  
Replace `<name>` with your Duke Net ID and `<answer>` with either `Yes` or `No`.  
This request will return "Correct" or "Incorrect".
