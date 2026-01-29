import csv

class DistanceList:

    #create DistanceList constructor
    def __init__(self, distance_list):
        self.distance_list = distance_list

    #create method to get the index for searched address, iterate through list until a match is found.
    def get_index(self, address_to_search,):
        index = -1
        for location in (self.distance_list):
            if address_to_search in location[0]:
                return index + 1
            index += 1
        return index

    #create method to get distance between both addresses, call get index method,
    def get_distance(self, start_address, end_address):
        start_index = self.get_index(start_address)
        end_index = self.get_index(end_address)

        # flip comparison if start index is higher to account for bottom heavy table
        if start_index > end_index:
            distance = self.distance_list[start_index][end_index+1]
        else:
           distance = self.distance_list[end_index][start_index+1]
        return float(distance)

