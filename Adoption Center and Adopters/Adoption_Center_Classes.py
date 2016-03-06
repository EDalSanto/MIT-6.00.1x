import random as rand
import random
import string
import math


class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        self.name = name
        self.species_types = species_types #A string:integer dictionary that represents the number of specific pets that each adoption center holds
        self.location = location #A tuple (x, y) That represents the x and y as floating point coordinates of the adoption center location
    def get_name(self):
        return self.name
    def get_location(self):
        temp = [] #empty dict to temporarily store float values of location
        for cordinates in self.location:
            temp.append(float(cordinates))
        return tuple(temp) #returns self.location in a tuple of floating point values
    def get_species_count(self): #Returns a copy of the full list and count of the available species at the adoption center
        copy_dict = self.species_types.copy() 
        for key in copy_dict.copy():
            if copy_dict[key] == 0:
                copy_dict.pop(key)
        return copy_dict
    def get_number_of_species(self, animal):
        try:
            return self.get_species_count()[animal]
        except KeyError:
            return 0
    def adopt_pet(self, species):
        if self.species_types[species] > 0:
        	self.species_types[species] -= 1  

class Adopter:
    """ 
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        self.name = name
        self.desired_species = desired_species
    def get_name(self):
        return self.name
    def get_desired_species(self):
        return self.desired_species
    def get_score(self, adoption_center):
        score = 1 * adoption_center.get_number_of_species(self.desired_species)
        return float(score)
        
class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species) # initialize Adopter attributes
        self.considered_species = considered_species # a list of strings of alternative species that the person is interested in adopting
        
    def get_score(self, adoption_center):
        adopter_score = Adopter.get_score(self, adoption_center)
        num_other = 0 #number of considered anaimals available 
        for animal in self.considered_species: #loop through animals in considered list
            num_other += adoption_center.get_number_of_species(animal) 
        score = adopter_score + (.3 * num_other)
        return score

class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    def __init__(self, name, desired_species, feared_species):
        Adopter.__init__(self, name, desired_species) # initialize Adopter attributes
        self.feared_species = feared_species
        
    def get_score(self, adoption_center):
        adopter_score = Adopter.get_score(self, adoption_center)
        num_feared = 0 #number of feared animal at adoption center
        num_feared += adoption_center.get_number_of_species(self.feared_species)
        score = adopter_score - (.3 * num_feared)
        return max(0.0,score)
        
class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    def __init__(self, name, desired_species, allergic_species):
        Adopter.__init__(self, name, desired_species) # initialize Adopter attributes
        self.allergic_species = allergic_species
        
    def get_score(self, adoption_center):
        adopter_score = Adopter.get_score(self, adoption_center)
        num_allergic = 0
        for animal in self.allergic_species:
            num_allergic += adoption_center.get_number_of_species(animal) 
        if num_allergic > 0.0:
            return 0.0 #returns a value that is 0 if the adoption center has one or more of a species that the adopter is allergic to
        else:
            return adopter_score #otherwise returns normal adopter score from parent class Adopter


class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter. 
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary. 
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        AllergicAdopter.__init__(self, name, desired_species, allergic_species)
        self.medicine_effectiveness = medicine_effectiveness 
        #medicine_effectiveness is a dictionary of {string: float} of the medicines effectiveness to certain species. 
        #The effectiveness can range from 0.0 (no effectiveness against allergies) to 1.0 (full effectiveness against allergies).
        #For example, medicine_effectiveness may look like {"Dog": 0.5, "Cat": 0.0, "Horse": 1.0}, 
        #which means there is a medium effectiveness against dog allergies, no effectiveness against cat allergies, and full effectiveness against horse allergies
        
    def get_score(self, adoption_center):
        adopter_score = Adopter.get_score(self, adoption_center)
        least_effective_drug = 1.0 #assume drug 100% perfect for alergic animals
        for animal in self.allergic_species:
            if adoption_center.get_number_of_species(animal) > 0: #if adoption center has 1 or more animals to which the adopter is allergic
                if self.medicine_effectiveness[animal] < least_effective_drug: #if the adopters' medicine is less than fully effective(1.0)
                    least_effective_drug = self.medicine_effectiveness[animal] #least effective drug updated
        score = least_effective_drug * adopter_score
        return score

class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    def __init__(self, name, desired_species, location):
        Adopter.__init__(self, name, desired_species)
        self.location = location
      
        
    def get_linear_distance(self, adoption_center):
        """
        calculates linear distrance between two points 
        a and b are tuples containing each's x and y coordinates
        """
        coordinate_dif_squared = [math.pow(adoption_center.get_location()[0]-self.location[0], 2.0), math.pow(adoption_center.get_location()[1]-self.location[1], 2.0)]
        temp = 0
        for elm in coordinate_dif_squared:
            temp += elm
        return math.sqrt(temp)       
        
    def get_score(self, adoption_center): 
        adopter_score = Adopter.get_score(self, adoption_center)
        if self.get_linear_distance(adoption_center) < 1: #check if difference between an instance of a SluggishAdopter and a given adoption_center using above function is less than 1
            return 1 * adopter_score
        elif self.get_linear_distance(adoption_center) < 3:
            return random.uniform(.7, .9) * adopter_score
        elif self.get_linear_distance(adoption_center) < 5:
            return random.uniform(.5, .7) * adopter_score
        else:
            return random.uniform(.1, .5) * adopter_score
            
def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter 
    to the Adopter will be ordered from highest score to lowest score.
    """
    Ranking_of_Adoption_Centers = [] #list of lists that will contain pairs of adoption center: adoption center score
    best_Adoption_Centers = [] #final list that will contain only best adoption centers names in order of score and then name
    for adoption_center in list_of_adoption_centers: #loop through list of adoption centers by name
        adoption_center_score = adopter.get_score(adoption_center) #set adoption center score using get_score attribute 
        Ranking_of_Adoption_Centers.append([adoption_center.get_name(), adoption_center_score]) #append list of adoption center:adoption center score 
    Ranking_of_Adoption_Centers.sort(key = lambda x: (-x[1], x[0])) #sort by score descending order then name in case of tie
    for elm in Ranking_of_Adoption_Centers: #loop through elements of sorted adoption centers ranked by score then name
        best_Adoption_Centers.append(elm[0]) #appen the 0th elm of this sorted list of lists to best_adoption_centers final list
    return best_Adoption_Centers #return final list of best adoption centers for adopter

    
def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """
    top_n_pairs = [] #list of lists that will contain lists of adopters:adopter_score
    top_n_adopters = [] #list of only top adopters, no score
    for adopter in list_of_adopters: #loop through list of provided adopters
        adopter_score = adopter.get_score(adoption_center) #set adopter_score = get_score method
        top_n_pairs.append([adopter.get_name(),adopter_score]) #append adopter:adopter_score to list as list
    top_n_pairs.sort(key = lambda x: (-x[1],x[0])) #sort first by score, then alphabetically in case of tie
    for elm in top_n_pairs: #for elm in sorted top_n_pairs sorted first by -value of adoption score(descending order) and then name
        top_n_adopters.append(elm[0]) #append adopter to final list of best adopters by score, sorted alphabetically
    return top_n_adopters[:n] #return final list of top adopters to nth one desired
        

  
ac = AdoptionCenter('b e', {'Dog': 8, 'Cat': 17,'Tiger':11,'Hourse':5,'Dog2': 11, 'Cat2': 17,'Tiger2':11,'Hourse2':5,'fish':17}, (1,0))

ad = [Adopter('jack v','Tiger'),Adopter('Dode v','Cat'),Adopter('jack r','Tiger'),Adopter('jack e3','Tiger'),Adopter('jack e','Cat2'),
Adopter('jack w','Dog'),Adopter('Gifaffe v','Dog'),Adopter('jack a','Tiger'),
Adopter('jack t','Cat'),Adopter('jack t','Cat2'),
SluggishAdopter("Five","Cat", (1,2)),SluggishAdopter("Five","Cat", (3,2)),
Adopter('jack t','fish')]

get_adopters_for_advertisement(ac,ad,5) #test for top 5 adopters
#The name of the adopter result should looks like below :
#Dode v  -  jack e  -  jack t  -  jack t  -  jack t  -  Five  -  Five  -  jack a  -  jack e3  -  jack r  -  jack v  -  Gifaffe v  -  jack w 