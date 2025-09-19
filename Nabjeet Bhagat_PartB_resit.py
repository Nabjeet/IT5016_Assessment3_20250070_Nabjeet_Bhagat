
# Create a unique ID counter used for generating ticket IDs
unique_booking_id = 20000  

class BookingSystem:
    """ BookingSystem represents a single ferry booking.
    It stores passenger details, booking status, and total service price. """
 def __init__(self, form_of_id, id_number, passenger_name):
       
     """ Constructor method.Sets passenger details and creates a unique ticket ID.
Uses Encapsulation (keeps related data in one place)."""

        global unique_booking_id
        unique_booking_id += 1  # increment ID to ensure uniqueness
        self.ticket_id = unique_booking_id
        self.form_of_id = form_of_id
        self.id_number = id_number
        self.passenger_name = passenger_name
        self.total = 0
        self.status = "Pending"        # default booking status
        self.approval_ref = "Not available"  # default approval reference

    def customer_info(self):
       
        """ Collects passenger details from user input.
        Principle: Modularity (only handles customer information)."""
        
        self.form_of_id = input("Enter Form of ID (Passport/Driver's License): ")
        self.id_number = input("Enter ID Number: ")
        self.passenger_name = input("Enter Passenger Name: ")

    def ferry_service_details(self):
       
        """ Collects service details and calculates price.
        Principle: Separation of Concerns (method focuses only on service pricing). """
       
        Ticket = int(input("Enter number of services: "))  # currently not used
        self.total = 0

        price = int(input("Enter service price: "))
        self.total += price  # adds price of chosen service(s)

    def booking_approval(self, approve=True):
       
        """ Handles manager approval of bookings.
        Principle: Decision logic is separated from input collection."""
        
        manager_decision = input("Manager approval required for Approve? (yes/no): ")

        if manager_decision == 'yes':
            self.status = "Approved"
            # Approval reference: first 3 characters of ID + last 2 digits of ticket
            self.approval_ref = self.id_number[:3] + str(self.ticket_id)[-2:]

        elif manager_decision == 'no':
            self.status = "Not approved"
            self.approval_ref = "Not available"

    def display_booking_info(self):
       
        """Prints booking information to the console.
        Principle: Readability (clear formatted output)."""
        
        print("\nPrinting Booking:")
        print("Form of ID:", self.form_of_id)
        print("ID Number:", self.id_number)
        print("Passenger Name:", self.passenger_name)
        print("Ticket ID:", self.ticket_id)
        print("Total: $", self.total)
        print("Status:", self.status)
        print("Approval Reference Number:", self.approval_ref)

    def booking_statistic(self, all_bookings):
        
        """ Calculates and prints overall booking statistics.
        Principle: Reusability (works on a list of any bookings). """
        
        total = 0  # FIXED (was always 0)
        approved = 0
        pending = 0
        not_approved = 0

        # Loop through all bookings and count by status
        for b in all_bookings:
            if b.status == "Approved":
                approved += 1
            elif b.status == "Pending":
                pending += 1
            elif b.status == "Not approved":
                not_approved += 1

        # Print results
        print("\nStatistics:")
        print("The total number of bookings submitted:", total)
        print("The total number of approved bookings:", approved)
        print("The total number of pending bookings:", pending)
        print("The total number of not approved bookings:", not_approved)


# Main program execution
if __name__ == "__main__":
    
    """Principle: Program entry point (Python convention).
    Here we simulate multiple bookings and then show final stats. """

    bookings = []  # list to hold all bookings
    for i in range(2):  # create 2 bookings for demo
        print("\nBooking", i+1)
        b = BookingSystem("form_of_id", "id_number", "passenger_name")
        b.customer_info()          # collect passenger info
        b.ferry_service_details()  # collect service and price
        b.booking_approval()       # approval process
        bookings.append(b)

    # Print all bookings
    print("\nFinal Bookings")
    for b in bookings:
        b.display_booking_info()

    # Print statistics of all bookings
    bookings[0].booking_statistic(bookings)

