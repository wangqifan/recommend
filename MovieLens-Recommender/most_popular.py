import random

import math

from collections import defaultdict
from operator import itemgetter

import similarity
import utils


class MostPopular:
    """
    Recommend via Random Choice.
    Top-N recommendation.
    """

    def __init__(self, n_rec_movie=10, save_model=True):
        """
        Init MostPopular with n_rec_movie.
        :return: None
        """
        print("MostPopular start...\n")
        self.n_rec_movie = n_rec_movie
        self.trainset = None
        self.save_model = save_model

    def fit(self, trainset):
        """
        Fit the trainset via count movies.
        :param trainset: train dataset
        :return: None
        """
        model_manager = utils.ModelManager()
        try:
            self.movie_popular = model_manager.load_model('movie_popular')
            self.movie_count = model_manager.load_model('movie_count')
            self.trainset = model_manager.load_model('trainset')
            self.total_movies = model_manager.load_model('total_movies')
            self.movie_popular_sort = model_manager.load_model('movie_popular_sort')
            print('MostPopular model has saved before.\nLoad model success...\n')
        except OSError:
            print('No model saved before.\nTrain a new model...')
            self.trainset = trainset
            self.movie_popular, self.movie_count = similarity.calculate_movie_popular(trainset)
            self.total_movies = list(self.movie_popular.keys())
            self.movie_popular_sort = sorted(self.movie_popular.items(), key=itemgetter(1), reverse=True)
            print('Train a new model success.')
            if self.save_model:
                model_manager.save_model(self.movie_popular, 'movie_popular')
                model_manager.save_model(self.movie_count, 'movie_count')
                model_manager.save_model(self.total_movies, 'total_movies')
                model_manager.save_model(self.movie_popular_sort, 'movie_popular_sort')
                print('The new model has saved success.\n')

    def recommend(self,user):
        model_manager = utils.ModelManager()
        mostpopularmovie=model_manager.load_model('movie_popular_sort')
        res=[]
        for (movieid,sorce) in mostpopularmovie[:10]:
            res.append(movieid)
        return res
        

       