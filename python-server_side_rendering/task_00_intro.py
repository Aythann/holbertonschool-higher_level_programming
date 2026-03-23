def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print(f"Invalid input type for template: expected str, got {type(template).__name__}.")
        return

    if not isinstance(attendees, list):
        print(f"Invalid input type for attendees: expected list, got {type(attendees).__name__}.")
        return

    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Invalid input type for attendees: expected a list of dictionaries.")
        return

    if template == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        content = template

        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            content = content.replace("{" + key + "}", str(value))

        filename = f"output_{index}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
