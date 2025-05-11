class Person:
    # List of allowed jobs
    APPROVED_JOBS = ["Sales", "Engineering", "ITC"]

    def __init__(self, name="Guido", job="Sales"):
        # Validate name: must be a string between 1 and 25 characters
        if not isinstance(name, str) or len(name) == 0 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
            return
        self.name = name.title()

        # Validate job: must be in the approved list
        if job in Person.APPROVED_JOBS:
            self.job = job
        else:
            print("Job must be in list of approved jobs.")
            self.job = "Unknown"
