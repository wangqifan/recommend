import utils
from most_popular import MostPopular
from dataset import DataSet



def run_model(model_name, dataset_name, test_size=0.3, clean=False):
    print('*' * 70)
    print('\tThis is %s model trained on %s with test_size = %.2f' % (model_name, dataset_name, test_size))
    print('*' * 70 + '\n')
    model_manager = utils.ModelManager(dataset_name, test_size)
    try:
        trainset = model_manager.load_model('trainset')
    except OSError:
        ratings = DataSet.load_dataset(name=dataset_name)
        trainset= DataSet.train_split(ratings)
        model_manager.save_model(trainset, 'trainset')
    '''Do you want to clean workspace and retrain model again?'''
    '''if you want to change test_size or retrain model, please set clean_workspace True'''
    model_manager.clean_workspace(clean)
    model = MostPopular()
    model.fit(trainset)
    return model


dataset_name = 'ml-100k'
model_type = 'MostPopular'
test_size = 0.1
PopularrecommendModel= run_model(model_type, dataset_name, test_size, False)