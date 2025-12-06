#!/usr/bin/python3
"""
Generates personalized invitation files from a template and a list of attendees.
Handles missing data and invalid inputs gracefully.
"""

import os

def generate_invitations(template, attendees):
    # Check input types
    if not isinstance(template, str):
        print(f"Error: Template must be a string, got {type(template).__name__}")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: Attendees must be a list of dictionaries, got {type(attendees).__name__}")
        return

    # Check for empty template
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Check for empty attendees list
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for idx, attendee in enumerate(attendees, start=1):
        # Replace placeholders, use "N/A" for missing values
        invitation = template
        for placeholder in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(placeholder)
            if value is None:
                value = "N/A"
            invitation = invitation.replace(f"{{{placeholder}}}", str(value))

        # Write to output file
        output_filename = f"output_{idx}.txt"
        try:
            with open(output_filename, 'w') as f:
                f.write(invitation)
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")
