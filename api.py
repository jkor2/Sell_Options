import json
from flask import Flask, jsonify
from flask import request
import main as functionality

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home_route():
    """
    Returns link to API docs
    Currently will just provide link to repository
    """

    return jsonify({
        "api_docs": "https://github.com/jkor2/Sell_Options"
        })



@app.route("/api/get_fund_holdings", methods=["GET"])
def get_fund_holdings():
    '''
    Returns the fund holdings of SPY and QQQ, returns JSON format
    '''

    # Database check and insertion

    fund_holdings = functionality.Main().get_fund_holdings()
    return jsonify(fund_holdings)



@app.route("/api/option_greeks/", methods=["GET"])
def get_option_greeks():

    """
    Returns option greeks of certain ticker based on date, returns JSON format
    """

    # ?ticker=AAPL&expiration=Apr%2005,%202024          is how arguments are recievied
    ticker = request.args.get('ticker', default='DefaultTicker', type=str)
    expiration = request.args.get('expiration', default='DefaultExpiration', type=str)

    # Database check and insertion

    greeks = functionality.Main().get_greeks(str(ticker).strip().upper(), str(expiration).strip().upper())
    return jsonify(greeks)


@app.route("/api/expiration_dates/", methods=["GET"])
def get_expiration_dates():
    """
    Returns option expiration dates in JSON format
    """


    # ?ticker=AAPL      is how arguments are recievied
    ticker = request.args.get('ticker', default='DefaultTicker', type=str)

    # Database check and insertion

    expiration_dates = functionality.Main().get_exipration_dates(ticker)
    return jsonify(expiration_dates)


@app.route("/api/tresaury_yields", methods=["GET"])
def get_treasury_yields():
    """
    Returns tresaury_yields in JSON format
    """

    yields = functionality.Main().get_yields()

    return jsonify(yields)


if __name__ == '__main__':
    app.run(port=5000)
    print("App running prot 5000")
