#!/usr/bin/python3

import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template is not a string")
        return
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees should be a list of dictionaries")
        return
    
    if not template:
        print("Template is empty, no output files generated")
        return
    if not attendees:
        print("No data provided, no output files generated")
        return

    for i, attendee in enumerate(attendees, start=1):
        personalized_invitation = template

        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key, "N/A") or "N/A"
            placeholder = "{" + key + "}"
            personalized_invitation = personalized_invitation.replace(placeholder, value)
        
        output_filename = f"output_{i}.txt"
        with open(output_filename, 'w') as file:
            file.write(personalized_invitation)
        print(f"Generated invitation: {output_filename}")