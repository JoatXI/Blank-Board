class PointOfInterest:
    def __init__(self, name, type, description):
        self.name = name
        self.type = type
        self.description = description
        self.enquiries = []
    
    def add_enquiry(self, enquiry):
        self.enquiries.append(enquiry)
    
    def remove_enquiry(self, enquiry):
        self.enquiries.remove(enquiry)
    
    def answer_enquiry(self):
        if self.enquiries:
            return self.enquiries.pop(0)
        else:
            return None