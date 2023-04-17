from pydantic import BaseModel,validator


class RowInput(BaseModel):
    row:int

    @validator("row")
    def row_have_to_positive(cls,v):
        if v < 0:
            raise ValueError('row have to positive')
        return v

row_input = RowInput(
    row= -1
)

print(row_input)