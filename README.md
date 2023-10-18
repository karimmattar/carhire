# Car Hire

* data:
  * init.sql, includes sql schema
  * carhire.png, includes schema diagram
* admin:
  * */customer/<ID>*, to retrieve customer by ID
  * */customer/create/*, to create new customer
  * */customer/update/<ID>/*, to update existing customer by ID
  * */customer/delete/<ID>/*, to delete customer by ID
* customer:
  * */customer/login/*, to retrieving customer data with tokens
  * */item/list*, to list all vehicles with categories
  * */item/hire/*,to create new booking

# Run server
* update admin/.env file
* update customer/.env file
* admin server:
  * cd admin 
  * python3 -m venv venv
  * source venv/bin/activate
  * pip install -r requirements.txt
  * python3 server.py
  * *server is running on localhost:5000*
* customer server:
  * cd customer 
  * python3 -m venv venv
  * source venv/bin/activate
  * pip install -r requirements.txt
  * python3 server.py
  * *server is running on localhost:5001*