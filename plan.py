from memory import Memory


class Plan(Memory):
    def __init__(
        self, description: str, location: str, starting_time: str, duration: str
    ):
        super().__init__(description)

        self.location = location
        self.starting_time = starting_time
        self.duration = duration

    def __str__(self):
        return "for 180 minutes from 9am, February 12th, 2023, at Oak Hill College Dorm: Klaus Mueller’s room: desk, read and take notes for research paper."
