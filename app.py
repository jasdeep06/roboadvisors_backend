import numpy as np
import pandas as pd
from flask import request
from utils import get_intersection,get_union
from flask import Flask
from flask import make_response
import json
import pickle
import re
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print(req)
    interests=req.get("interests")
    beliefs=req.get("beliefs")
    sector_dict,industry_dict,ticker2name_dict=pickle.load(open("conclusions/info.p","rb"))
    interests_list=[]
    beliefs_list=[]
    for interest in interests:
        interests_list.append(industry_dict[interest])
    for belief in beliefs:
        beliefs_list.append(sector_dict[belief])

    interest_set=get_union(interests_list)
    belief_set=get_union(beliefs_list)

    final_set=get_intersection([interest_set,belief_set])

    stock_list=[]
    for ticker in final_set:
        stock_list.append(ticker2name_dict[ticker]+"("+ticker+")")



    res = {
        "stocks":stock_list
    }
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r




if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')