from fastapi import FastAPI, Path
from pydantic import BaseModel


app = FastAPI()
movies = {}


class Movie(BaseModel):
    title: str
    director: str
    release_year: int
    rating: float


@app.get('/movies')
async def get_all_movies():
    return movies


@app.post('/movies')
async def add_new_movie(movie: Movie):
    movies[max(movies.keys())+1 if movies != {} else 1] = {'title': movie.title, 'director': movie.director,
                                                           'release_year': movie.release_year, 'rating': movie.rating}
    return {'status': 'success'}


@app.get('/movies/{id}')
async def get_one_movie(id: int = Path(ge=1)):
    return movies[id]


@app.delete('/movies/{id}')
async def delete_movie(id: int = Path(ge=1)):
    del movies[id]
    return {'status': 'success'}
