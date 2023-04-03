"""Module representing class BaseModel that defines all 
common attributes/methods for other classes
"""
import uuid
from datetime import datetime

class BaseModel:
    """Base class from which other classes can inherite"""

    def __init__(self):
        """class constructor method for creating objects
        Args:
             id (str): assign with an uuid when an instance is created
             created_at (date): assign with the current datetime when an 
                               instance is created
             updated_at (date): assign with the current datetime when an 
                               instance is created and it will be updated 
                               every time you change your object
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Method that prints string representation of Basemodel
        in the format [<class name>] (<self.id>) <self.__dict__>

        Returns:
                return formatted string if succesful
        """
        
        return "[{}] {} {}"./
        format(self.__class__.__name__,  self.id, self.__dict__)

    def save(self):
        """Method that pdates the public instance attribute updated_at 
        with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Method returns a dictionary containing all keys/values of
         __dict__ of the instance
        """
        my_dict = {}
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
