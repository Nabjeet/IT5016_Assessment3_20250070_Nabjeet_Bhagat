
unique_booking_id = 20000

class BookingSystem:
    def __init__(self, form_of_id, id_number, passenger_name):
        global unique_booking_id
        unique_booking_id += 1
        self.ticket_id = unique_booking_id
        self.form_of_id = form_of_id
        self.id_number = id_number
        self.passenger_name = passenger_name
        self.total = 0
        self.status = "Pending"
        self.approval_ref = "Not available"

    def customer_info(self):
        self.form_of_id = input("Enter Form of ID (Passport/Driver's License): ")
        self.id_number = input("Enter ID Number: ")
        self.passenger_name = input("Enter Passenger Name: ")

    def ferry_service_details(self):
        Ticket = int(input("Enter number of services: "))
        self.total = 0
        
        price = int(input("Enter service price: "))
        self.total += price

    def booking_approval(self, approve=True):
        manager_decision = input("Manager approval required for Approve? (yes/no): ")
        
        if manager_decision == 'yes':
            self.status = "Approved"

            self.approval_ref = self.id_number[:3] + str(self.ticket_id)[-2:]

        elif manager_decision == 'no':
            self.status = "Not approved"
            self.approval_ref = "Not available"

    def display_booking_info(self):
        print("\nPrinting Booking:")
        print("Form of ID:", self.form_of_id)
        print("ID Number:", self.id_number)
        print("Passenger Name:", self.passenger_name)
        print("Ticket ID:", self.ticket_id)
        print("Total: $", self.total)
        print("Status:", self.status)
        print("Approval Reference Number:", self.approval_ref)

    def booking_statistic(self, all_bookings):
        total = 0
        approved = 0
        pending = 0
        not_approved = 0

        for b in all_bookings:
            
            if b.status == "Approved":
                approved += 1
            elif b.status == "Pending":
                pending += 1
            elif b.status == "Not approved":
                not_approved += 1

        print("\nStatistics:")
        print("The total number of bookings submitted:", total)
        print("The total number of approved bookings:", approved)
        print("The total number of pending bookings:", pending)
        print("The total number of not approved bookings:", not_approved)


if __name__ == "__main__":
    
    bookings = []
    for i in range(2):
        print("\nBooking", i+1)
        b = BookingSystem("form_of_id", "id_number", "passenger_name")
        b.customer_info()
        b.ferry_service_details()
        b.booking_approval()
        bookings.append(b)

    print("\nFinal Bookings")
    for b in bookings:
        b.display_booking_info()

    bookings[0].booking_statistic(bookings)
