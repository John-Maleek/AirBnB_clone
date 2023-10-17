"""
    Module defines a Base model class
    defines all common attributes/methods for other classes
"""

import uuid
from datetime import datetime


class SampleBaseModel:
    # id = None
    # created_at = None
    # updated_at = None
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        return self.__dict__


# ex1 = SampleBaseModel()
# print(ex1.id)
# # print(type(ex1.id))
# print(ex1.created_at)
# print(ex1.updated_at)
# ex1.save()

# print(ex1.to_dict())
# ex1.save()
# print(ex1.to_dict())
