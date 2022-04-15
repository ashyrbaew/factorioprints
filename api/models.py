from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy_imageattach.entity import Image, image_attachment

class Prints(Base):
    __tablename__ = 'printparser_prints'
    id = Column(Integer, primary_key=True, index=True)
    key = Column(String)
    author = Column(String)
    details = Column(String)
    blueprint = Column(String)
    created_at = Column(String)
    updated_at = Column(String)
    favorites = Column(String)
    # image = image_attachment('UserPicture')
