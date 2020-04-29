import braintree

from flask import Flask
from flask import request





app = Flask(__name__,
            static_url_path='', 
            static_folder='web/static',
            template_folder='web/templates')


          

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id="3q68q4cbb5wyvrhw",
        public_key="zjg2xhg5dyqf9p5q",
        private_key="47f7108885833d85a6fa3b2f4c33a320"
    )
)

#Generate a client token
# client_token = gateway.client_token.generate({
#     "customer_id": a_customer_id
# })


#Send a client token to client
@app.route("/client_token", methods=["GET"])
def client_token():
  return gateway.client_token.generate()

#Receive a payment method nonce from client
@app.route("/checkout", methods=["POST"])
def checkout():
  nonce_from_the_client =  request.form["paymentMethodNonce"]
  amount = request.form["amount"]
  
  # Use payment method nonce here...
  #Create a transaction
  result = gateway.transaction.sale({
      "amount": "10",
      "payment_method_nonce": nonce_from_the_client,      
      "options": {
        "submit_for_settlement": True
      } 
  }) 
  if result.is_success:
    return (result.transaction.id)
  else:
    return (format(result.message))
 
  

@app.route("/refund", methods=["POST"])
def refund():
    transaction = gateway.transaction.find(request.form["transaction_id"])
    result = {}
    if transaction.status in TRANSACTION_SUCCESS_STATUSES:
        result = gateway.refund(transaction)
        result = {
            'header': 'Sweet Success!',
            'icon': 'success',
            'message': 'Your test refund has been successfully processed. See the Braintree API response and try again.'
        }
    else:
        result = {
            'header': 'Transaction Failed',
            'icon': 'fail',
            'message': 'Your test refund has a status of ' + transaction.status + '. See the Braintree API response and try again.'
        }
    

    return(json.dumps(result) )


@app.route('/')
def hello_world():    
    return 'Hey, we have Flask in a Docker container!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')