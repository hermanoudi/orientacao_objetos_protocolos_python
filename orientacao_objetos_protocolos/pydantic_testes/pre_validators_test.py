from pydantic import BaseModel, field_validator


class Pedidos(BaseModel):
    ids: list[int]

    @field_validator('ids', mode="before")
    def convert_ids(cls, v):
        return v.split(';')

    # @field_validator('ids', each_item=True)
    # def convert_ids(cls, v):
    #     if v < 0:
    #         raise ValueError()
    #     return v
