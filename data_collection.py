from pymongo import MongoClient
import random
import os
from dotenv import load_dotenv

load_dotenv()

class DataCollection:
    def __init__(self):
        self.client = MongoClient(os.getenv("mongo_server"))
        self.db = self.client[os.getenv("mongo_db")]

    def __set_collection(self, collection): 
        self.col = self.db[collection]
    
    def __get_data_array(self):
        if not self.col:
            raise Exception("Collection not set!")
        document = self.col.find()[0]
        return document['items']
    
    def __get_random_from_collection(self, collection):
        self.__set_collection(collection)

        my_temp_list = self.__get_data_array()
        my_random_index = random.randrange(0, len(my_temp_list))
        random.shuffle(my_temp_list)

        return my_temp_list[my_random_index]
    
    def __create_array_of_random_items(self, collection, size):
        my_array = []
        for i in range(size):
            my_array.append(self.__get_random_from_collection(collection))
        
        return my_array

    def get_player(self): return self.__get_random_from_collection("players")
    def get_salty_card(self): return self.__get_random_from_collection("salt")
    def get_top_lands(self): return self.__get_random_from_collection("lands")
    def get_top_card(self): return self.__get_random_from_collection("topcards")
    def get_reaction(self): return self.__get_random_from_collection("reactions")
    def get_top_instant(self): return self.__get_random_from_collection("instants")
    def get_top_sorcery(self): return self.__get_random_from_collection("sorceries")
    def get_top_artifact(self): return self.__get_random_from_collection("artifacts")
    def get_top_creature(self): return self.__get_random_from_collection("creatures")
    def get_instant_phase(self): return self.__get_random_from_collection("instantphases")
    def get_top_enchantment(self): return self.__get_random_from_collection("enchantments")
    
    def get_player_array(self, size): return self.__create_array_of_random_items("players", size)
    def get_salty_card_array(self, size): return self.__create_array_of_random_items("salt", size)
    def get_top_lands_array(self, size): return self.__create_array_of_random_items("lands", size)
    def get_top_card_array(self, size): return self.__create_array_of_random_items("topcards", size)
    def get_reaction_array(self, size): return self.__create_array_of_random_items("reactions", size)
    def get_top_instant_array(self, size): return self.__create_array_of_random_items("instants", size)
    def get_top_sorcery_array(self, size): return self.__create_array_of_random_items("sorceries", size)
    def get_top_artifact_array(self, size): return self.__create_array_of_random_items("artifacts", size)
    def get_top_creature_array(self, size): return self.__create_array_of_random_items("creatures", size)
    def get_instant_phase_array(self, size): return self.__create_array_of_random_items("instantphases", size)
    def get_top_enchantment_array(self, size): return self.__create_array_of_random_items("enchantments", size)
