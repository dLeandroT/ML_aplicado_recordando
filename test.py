from fastapi.testclient import TestClient

from api.main import app


client = TestClient(app)


def test_null_prediction():
    response = client.post('v1/prediction', json = {
                                    "production_budget": 0,
                                    "title_year": 0,
                                    "aspect_ratio": 0,
                                    "duration": 0,
                                    "cast_total_facebook_likes": 0,
                                    "budget": 0,
                                    "imdb_score": 0,
                                    "opening_gross": 0,
                                    "screens": 0
                                    })
    
    assert response.status_code == 422

    
def test_random_prediction():
    response = client.post('v1/prediction', json = {
                                    "production_budget": 8300681,
                                    "title_year": 1999,
                                    "aspect_ratio": 1.85,
                                    "duration": 97,
                                    "cast_total_facebook_likes": 37907,
                                    "budget": 16000000,
                                    "imdb_score": 7.2,
                                    "opening_gross": 83306801,
                                    "screens": 2271
                                    })
    assert response.status_code == 200
    assert response.json()['worldwide_gross'] != 0