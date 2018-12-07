import collections
from operator import itemgetter

import math

from collections import defaultdict

import similarity
import utils


class ItemBasedCF:
    """
    Item-based Collaborative filtering.
    Top-N recommendation.
    """

    def __init__(self, k_sim_movie=20, n_rec_movie=10, use_iuf_similarity=False, save_model=True):
        """
        Init UserBasedCF with n_sim_user and n_rec_movie.
        :return: None
        """
        print("ItemBasedCF start...\n")
        self.k_sim_movie = k_sim_movie
        self.n_rec_movie = n_rec_movie
        self.trainset = None
        self.save_model = save_model
        self.use_iuf_similarity = use_iuf_similarity

    def fit(self, trainset):
        """
        Fit the trainset by calculate movie similarity matrix.
        :param trainset: train dataset
        :return: None
        """
        model_manager = utils.ModelManager()
        try:
            self.movie_sim_mat = model_manager.load_model(
                'movie_sim_mat-iif' if self.use_iuf_similarity else 'movie_sim_mat')
            self.movie_popular = model_manager.load_model('movie_popular')
            self.movie_count = model_manager.load_model('movie_count')
            self.trainset = model_manager.load_model('trainset')
            print('Movie similarity model has saved before.\nLoad model success...\n')
        except OSError:
            print('No model saved before.\nTrain a new model...')
            self.movie_sim_mat, self.movie_popular, self.movie_count = \
                similarity.calculate_item_similarity(trainset=trainset,
                                                     use_iuf_similarity=self.use_iuf_similarity)
            self.trainset = trainset
            print('Train a new model success.')
            if self.save_model:
                model_manager.save_model(self.movie_sim_mat,
                                         'movie_sim_mat-iif' if self.use_iuf_similarity else 'movie_sim_mat')
                model_manager.save_model(self.movie_popular, 'movie_popular')
                model_manager.save_model(self.movie_count, 'movie_count')
                model_manager.save_model(self.trainset, 'trainset')
                print('The new model has saved success.\n')

    def recommend(self, user):
        """
        Find K similar movies and recommend N movies for the user.
        :param user: The user we recommend movies to.
        :return: the N best score movies
        """
        if not self.movie_sim_mat or not self.n_rec_movie or \
                not self.trainset or not self.movie_popular or not self.movie_count:
            raise NotImplementedError('ItemCF has not init or fit method has not called yet.')
        K = self.k_sim_movie
        N = self.n_rec_movie
        predict_score = collections.defaultdict(int)
        if user not in self.trainset:
            print('The user (%s) not in trainset.' % user)
            return
        # print('Recommend movies to user start...')
        watched_movies = self.trainset[user]
        for movie, rating in watched_movies.items():
            for related_movie, similarity_factor in sorted(self.movie_sim_mat[movie].items(),
                                                           key=itemgetter(1), reverse=True)[0:K]:
                if related_movie in watched_movies:
                    continue
                # predict the user's "interest" for each movie
                # the predict_score is sum(similarity_factor * rating)
                predict_score[related_movie] += similarity_factor * rating
        # print('Recommend movies to user success.')
        # return the N best score movies
        return [movie for movie, _ in sorted(predict_score.items(), key=itemgetter(1), reverse=True)[0:N]]

  
    def predict(self, testset):
        """
        Recommend movies to all users in testset.
        :param testset: test dataset
        :return: `dict` : recommend list for each user.
        """
        movies_recommend = defaultdict(list)
        print('Predict scores start...')
        # record the calculate time has spent.
        for i, user in enumerate(testset):
            rec_movies = self.recommend(user)  # type:list
            movies_recommend[user].append(rec_movies)
            # log steps and times.
        print('Predict scores success.')
        return movies_recommend
