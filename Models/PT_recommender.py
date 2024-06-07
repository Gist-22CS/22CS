from typing import Literal

from pydantic import BaseModel, Field

from sqlalchemy import Column, Integer, String, Text, DateTime

from database.database import Base, engine

MAX_LENGTH = 20
MIN_LENGTH = 2

class UserInfo(Base):
    __tablename__="userinfo"

    id = Column(Integer, primary_key=True)
    name_i = Column(String, nullable=False)
    age_i = Column(Integer, nullable=False)
    interest_i = Column(Integer, primary_key=False)
    region_i = Column(Integer, primary_key=False)

#Create all tables in the engine
Base.metadata.create_all(bind=engine)


class InputModel(BaseModel):
    name: str = Field(
        alias='name',
        description='Type your name(Either Korean and English are fine)!',
        default='User',
        min_length=MIN_LENGTH,
        max_length=MAX_LENGTH,
        pattern=rf'^[a-z|A-Z|가-힣]{{{MIN_LENGTH},{MAX_LENGTH}}}$',
    )

    age: int = Field(
        alias='age',
        description='Type your age!',
        default='20',
        gt=0,
        lt=100,
    )

    interest: int = Field(
        alias='interest',
        description='Choose your interest!',
        default='1',
        gt=0,
        lt=5,
    )

    region: int = Field(
        alias='region',
        description='Choose where you live!',
        default='1',
        gt=0,
        lt=96,
    )


class OutputModel(BaseModel):
    output1: str = Field(
        description='Recommending User1',
    )

    output2: str = Field(
        description='Recommending User2',
    )

    output3: str = Field(
        description='Recommending User3',
    )
