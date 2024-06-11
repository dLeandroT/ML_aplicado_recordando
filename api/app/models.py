from pydantic import BaseModel

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

class PredictionResponse(BaseModel):
    worldwide_gross: float