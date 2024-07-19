import logging
import os
from collections import defaultdict

class DefaultDict(defaultdict):
    def __missing__(self, key):
        return f"{key}: N/A"

def generate_invitations(template, attendees):
    # Check if the template is a string
    if not isinstance(template, str):
        logging.error(f"Invalid input type for template: Expected str, got {type(template).__name__}")
        return

    # Check if attendees is a list of dictionaries
    if not (isinstance(attendees, list) and all(isinstance(attendee, dict) for attendee in attendees)):
        logging.error(f"Invalid input type for attendees: Expected list of dictionaries, got {type(attendees).__name__}")
        return

    if not (isinstance(attendees, list) and all(isinstance(attendee, dict) for attendee in attendees)):
        raise TypeError("attendees must be a list of dictionaries")

    for index, attendee in enumerate(attendees, start=1):
        # Use DefaultDict to handle missing data
        safe_attendee = DefaultDict(lambda: "N/A", attendee)
        
        # Substitute placeholders with actual values or "N/A"
        invitation = template
        for key in safe_attendee:
            placeholder = f"{{{key}}}"
            if placeholder in template:
                invitation = invitation.replace(placeholder, f"{safe_attendee[key]}")
            else:
                # If the placeholder is not in the template, add it with its value or "N/A"
                invitation += f"\n{key}: {safe_attendee[key]}"

        filename = f"output_{index}.txt"
        try:
            if os.path.exists(filename):
                logging.warning(f"File {filename} already exists. Skipping to avoid overwriting.")
                continue

            with open(filename, "w") as file:
                file.write(invitation)
        except IOError as e:
            logging.error(f"Failed to write to {filename}: {e}")