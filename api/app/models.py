from pydantic import BaseModel, field_validator

class PredictionRequest(BaseModel):
    production_budget: float
    title_year: int
    aspect_ratio: float
    duration: int
    cast_total_facebook_likes: float
    budget: float
    imdb_score: float
    opening_gross: float
    screens: float

    # Para evitar que se ingresen valores en 0
    @field_validator('*')
    def no_zero_values(cls, v):
        if v == 0:
            raise ValueError('Value cannot be zero')
        return v

class PredictionResponse(BaseModel):
    worldwide_gross: float