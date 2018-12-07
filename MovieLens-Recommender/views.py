from __init__ import app
from flask import jsonify

from ItemRecommend import ItemrecommendModel
from popularRecommed import PopularrecommendModel

def recommend_test(model, user):
    recommend = model.recommend(str(user))
    print("recommend for userid = %s:" % user)
    return recommend

@app.route("/recommend/<int:userid>")
def recommed(userid):
    if userid == 0:
        return jsonify(recommend_test(PopularrecommendModel,userid))
    else:
        return jsonify(recommend_test(ItemrecommendModel,userid))



