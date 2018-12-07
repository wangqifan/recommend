import time
import pickle

import os
import shutil



class ModelManager:
    """
    Model manager is designed to load and save all models.
    No matter what dataset name.
    """
    # This dataset_name belongs to the whole class.
    # So it should be init for only once.
    path_name = ''

    @classmethod
    def __init__(cls, dataset_name=None, test_size=0.3):
        """
        cls.dataset_name should only init for only once.
        :param dataset_name:
        """
        if not cls.path_name:
            cls.path_name = "model/" + dataset_name + '-testsize' + str(test_size)

    def save_model(self, model, save_name: str):
        """
        Save model to model/ dir.
        :param model: source model
        :param save_name: model saved name.
        :return: None
        """
        if 'pkl' not in save_name:
            save_name += '.pkl'
        if not os.path.exists('model'):
            os.mkdir('model')
        pickle.dump(model, open(self.path_name + "-%s" % save_name, "wb"))

    def load_model(self, model_name: str):
        """
        Load model from model/ dir via model name.
        :param model_name:
        :return: loaded model
        """
        if 'pkl' not in model_name:
            model_name += '.pkl'
        if not os.path.exists(self.path_name + "-%s" % model_name):
            raise OSError('There is no model named %s in model/ dir' % model_name)
        return pickle.load(open(self.path_name + "-%s" % model_name, "rb"))

    @staticmethod
    def clean_workspace(clean=False):
        """
        Clean the whole workspace.
        All File in model/ dir will be removed.
        :param clean: Boolean. Clean workspace or not.
        :return: None
        """
        if clean and os.path.exists('model'):
            shutil.rmtree('model')
