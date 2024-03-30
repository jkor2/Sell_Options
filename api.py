import json
from flask import Flask, jsonify, request
import main as functionality

app = Flask(__name__)

@app.route("/api/get_fund_holdings", methods=["GET"])
def get_fund_holdings():
    '''
    Gets and returns fund holdings in JSON 
    '''

    # Database check and insertion

    fund_holdings = functionality.Main().get_fund_holdings()
    return jsonify(fund_holdings)



@app.route("/api/option_greks", methods=["GET"])
def get_option_greeks():
    '''
    Two arguments (Ticker and Strike Date MMM DD, YYYYY) 
    # Should call and put strikes be held within list instead of objects
    '''

    # Database check and insertion

    greeks = functionality.Main().get_greeks("TSLA", "Apr 12, 2024")
    return jsonify(greeks)



if __name__ == '__main__':
    app.run(port=5000)
    print("App running prot 5000")