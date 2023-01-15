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
        

class PointsOfInterestManager:
    def __init__(self):
        self.points_of_interest = []
        self.links = {}
    
    def add_point_of_interest(self, point_of_interest):
        self.points_of_interest.append(point_of_interest)
    
    def search_point_of_interest(self, name):
        for point_of_interest in self.points_of_interest:
            if point_of_interest.name == name:
                return point_of_interest
        return None
    
    def delete_point_of_interest(self, name):
        point_of_interest = self.search_point_of_interest(name)
        if point_of_interest:
            self.points_of_interest.remove(point_of_interest)
    
    def save_points_of_interest(self, filename):
        with open(filename, 'w') as f:
            for point_of_interest in self.points_of_interest:
                f.write(f"{point_of_interest.name},{point_of_interest.type},{point_of_interest.description}\n")
    
    def load_points_of_interest(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                name, type, description = line.strip().split(',')
                point_of_interest = PointOfInterest(name, type, description)
                self.add_point_of_interest(point_of_interest)
        print("Points of interest loaded successfully!")
   
    def make_enquiry(self, point_of_interest, enquiry):
        point_of_interest.add_enquiry(enquiry)
        print("Enquiry made successfully!")
    
    def answer_enquiry(self, point_of_interest):
        enquiry = point_of_interest.answer_enquiry()
        if enquiry:
            print(f"Enquiry '{enquiry}' answered successfully!")
        else:
            print("No enquiries to answer.")