from pydantic import BaseModel, Field

from pydantic import BaseModel, Field

class InputModel(BaseModel):
    trainer_name: str = Field(default="", alias="트레이너 이름", description="검색할 트레이너의 이름을 입력하세요.")


class OutputModel(BaseModel):
    output: str = Field(
        description="검색 결과"
    )
