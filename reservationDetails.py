class Reservation:
    def __init__(self, patronId, priorityNumber, timeOfReservation):
        self.patronId = patronId
        self.priorityNumber = priorityNumber
        self.timeOfReservation = timeOfReservation

    def __lt__(self, other):
        # Custom comparison for sorting based on priorityNumber and timeOfReservation
        if self.priorityNumber == other.priorityNumber:
            return self.timeOfReservation < other.timeOfReservation
        return self.priorityNumber < other.priorityNumber
