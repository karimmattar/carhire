from routers import customer_route
from main import app

# register the customer route
app.register_blueprint(customer_route)
app.run(host='localhost', port=5000, debug=True)
