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
            
    def find_route(self, origin, destination):
        route = []
        visited = set()
        stack = [origin]
        while stack:
            point_of_interest = stack.pop()
            if point_of_interest not in visited:
                visited.add(point_of_interest)
                route.append(point_of_interest)
                if point_of_interest == destination:
                    break
                for neighbor in self.links[point_of_interest]:
                    if neighbor not in visited:
                        stack.append(neighbor)
        return route
    
    def sort_points_of_interest(self):
        # Insertion sort algorithm to sort the points of interest by name
        for i in range(1, len(self.points_of_interest)):
            point_of_interest = self.points_of_interest[i]
            j = i - 1
            while j >= 0 and self.points_of_interest[j].name > point_of_interest.name:
                self.points_of_interest[j + 1] = self.points_of_interest[j]
                j -= 1
            self.points_of_interest[j + 1] = point_of_interest
    
    def add_link(self, point_of_interest1, point_of_interest2):
        self.links[point_of_interest1] = point_of_interest2
        self.links[point_of_interest2] = point_of_interest1
        
def main():
    manager = PointsOfInterestManager()
    
     # Hard-coded data for points of interest and links
    railway_station = PointOfInterest("Railway Station", "Transportation", "A busy train station.")
    park_cafe = PointOfInterest("Park Cafe", "Food", "A cozy cafe with outdoor seating.")
    war_memorial = PointOfInterest("War Memorial", "Historical", "A monument honoring fallen soldiers.")
    white_horse_pub = PointOfInterest("White Horse Pub", "Food and Drink", "A traditional British pub.")
    museum = PointOfInterest("Museum", "Cultural", "A museum with exhibits on local history.")
    concert_hall = PointOfInterest("Concert Hall", "Entertainment", "A venue for live music and performances.")
    movie_theater = PointOfInterest("Movie Theater", "Entertainment", "A place to watch the latest films.")

    manager.add_point_of_interest(railway_station)
    manager.add_point_of_interest(park_cafe)
    manager.add_point_of_interest(war_memorial)
    manager.add_point_of_interest(white_horse_pub)
    manager.add_point_of_interest(museum)
    manager.add_point_of_interest(concert_hall)
    manager.add_point_of_interest(movie_theater)
    
    manager.add_link(railway_station, park_cafe)
    manager.add_link(park_cafe, war_memorial)
    manager.add_link(war_memorial, white_horse_pub)
    manager.add_link(railway_station, museum)
    manager.add_link(white_horse_pub, railway_station)
    manager.add_link(museum, concert_hall)
    manager.add_link(concert_hall, movie_theater)
    manager.add_link(concert_hall,railway_station)
    manager.add_link(museum, movie_theater)
    manager.add_link(museum, white_horse_pub)
    manager.add_link(park_cafe, movie_theater)
    manager.add_link(movie_theater, railway_station)
    manager.add_link(war_memorial, railway_station)
    manager.add_link(park_cafe, white_horse_pub)
    manager.add_link(museum, park_cafe)
    manager.add_link(concert_hall, park_cafe)
    manager.add_link(concert_hall, war_memorial)
    manager.add_link(museum, war_memorial)
    manager.add_link(war_memorial, movie_theater)
    manager.add_link(white_horse_pub, movie_theater)
    manager.add_link(white_horse_pub, concert_hall)