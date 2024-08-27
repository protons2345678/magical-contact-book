class MagicalContact:
    def __init__(self, name, email=None, phone_number=None):
        self.name=name
        self.email=email
        self.phone_number=phone_number

    def get_name(self):
        return self.name
    def get_email(self):
        return self.email
    def get_phone_number(self):
        return self.phone_number
    def set_email(self, email):
        self.email=email
    def set_phone_number(self, phone_number):
        self.phone_number=phone_number
    def describe(self):
        return f"Name: {self.name}, Email: {self.email}, Phone Number: {self.phone_number}"
    
class WizardOrWitch(MagicalContact):
    VALID_HOUSES=["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    def __init__(self, name, email=None, phone_number=None):
        super().__init__(name, email, phone_number)
        if house not in self.VALID_HOUSES:
            raise ValueError(f"Invalid house: {house}. Must be one of {self.VALID_HOUSES}")
        self.__wand=wand if wand else {"core": None, "wood": None, "length": None}
        self.__house=house

    def get_wand(self):
        return self.__wand
    def get_house(self):
        return self.__house
    def describe(self):
        wand_describtion=f"Wand - Core: {self.__wand['core']}, Wood: {self.__wand['wood']}, length: {self.__wand['length']}"
        return f"{super().describe()}, House: {self.__house},{wand_describtion}"
    
class MagicalCreature(MagicalContact):
    def __init__(self, name, email=None, phone_number=None):
        super().__init__(name, email, phone_number)
        self.__species=species
        self.__is_tame=is_tame
    
    def get_species(self):
        return self.__species
    def __is_tame(self):
        return self.__is_tame
    def describe(self):
        tame_status="Tame" if self.__is_tame else "Wlid"
        return f"{super().describe()}, Species: {self.__species}, Status: {tame_status}"
    
class MagicalContactBook:
    def __init__(self):
        self.__contacts=[]
    def add_contact(self, contact):
        if not isinstance(contact, MagicalContact):
            raise TypeError("Contact must be an instance of MagicalContact or its subclasses")
        self.__contacts.append(contact)
    def list_contacts(self):
        return [contact.describe() for contact in self.__contacts]
    def find_contact(self, name):
        for contact in self.__contacts:
            if contact.get_name() == name:
                return contact.describe()
        return"Contact not found"