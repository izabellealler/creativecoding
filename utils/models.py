from pydantic import BaseModel, Field


class Instagram(BaseModel):
    post_width: int = Field(default=1080)
    post_height: int = Field(default=1080)
    story_width: int = Field(default=1080)
    story_height: int = Field(default=1920)

class A1(BaseModel):
    width: int = Field(default=7016)
    height: int = Field(default=9933)

class A2(BaseModel):
    width: int = Field(default=4961)
    height: int = Field(default=7016)

class A3(BaseModel):
    width: int = Field(default=3508)
    height: int = Field(default=4961)

class A4(BaseModel):
    width: int = Field(default=2480)
    height: int = Field(default=3508)

class A5(BaseModel):
    width: int = Field(default=1748)
    height: int = Field(default=2480)