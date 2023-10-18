from main import app
from routers import customer_route, item_route

# register the customer route
app.register_blueprint(customer_route)
# register the item route
app.register_blueprint(item_route)
# run the app
app.run(host='localhost', port=5001, debug=True)
