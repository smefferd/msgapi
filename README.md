# msgapi

This is a very basic messaging service for demonstration of REST API with Python.
It uses SQLAlchemy for ORM persistence, Flask for the HTTP service and Swagger for 
documentation and ad-hoc testing.
It also makes use of a convenience framework called SAFRS integrating these technologies 
and using reflection on the ORM to present a complete CRUD API without requiring boilerplate code.

The default configuration of the service uses an in-memory sqlite database
so be aware that Users and Messages are not persisted between invocations of the service.
Also by default the `--add-test-data` option is on, 
so there are two existing users Bob and Jane with user ids 1 and 2 respectively.

The assignment requirements that prompted this project can be found [here](assignment.md)


## Usage
The only requirement for the service is Python 3. 
The examples in this readme are for linux platforms, however it should also work on Windows.
Python with windows should usually be run with the `py` command instead of `python3` shown here.

`python3 --version`

To get started make sure Python pip is installed.

`python3 -m ensurepip`

Create and activate a Python virtual environment.
This is not required, however if you have other Python projects
this keeps your environments separate and uncluttered.

````
python3 -m virtualenv .venv && \
source .venv/bin/activate
````

Then install the dependencies with the following command.

`python3 -m pip install -r requirements.txt`

Run the service.

`python3 msgapi.py`

You should see logging similar to the following in the console.
````
/Users/1ce15e/_dev/msgapi_demo/.venv/lib/python3.10/site-packages/flask_sqlalchemy/__init__.py:872: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  warnings.warn(FSADeprecationWarning(
API can be accessed with the url: http://localhost:5000/
 * Serving Flask app 'msgapi' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://localhost:5000/ (Press CTRL+C to quit)
````

Optional parameters can be specified for host, port, etc.

````
python3 msgapi.py --help
usage: msgapi.py [-h] [--host HOST] [--port PORT] [--prefix PREFIX] [--db DB]
                 [--add-test-data TESTDATA]

HTTP API Messaging Service

options:
  -h, --help       show this help message and exit
  --host HOST      hostname of http service
  --port PORT      tcp port for http service
  --prefix PREFIX  api endpoint url prefix for http service
  --db DB          database connection uri
  --add-test-data ADD_TEST_DATA
                   add bob and jane users with existing messages  
````

For example, to start the service on port 8080.

`python3 msgapi.py --port 8080`


## Endpoints
The SAFRS framework provides a full set of CRUD operations on the endpoint entities 
compatible with the OpenAPI specification.
This section in the readme only highlights the endpoints necessary for the basic workflow.
For full documentation and functionality to exercise the API
open the Swagger UI running in the service at the root path.

`http://localhost:5000`

### /users

#### POST
Create a new User.
Usernames must be unique.
Returns a json object with the new user id.
Two users would likely be created before sending a message,
however a single User may send a message to self.
The user ids are used for sender and receiver in the API to create messages.

`POST /user`

````json
{
  "data": {
    "attributes": {
      "name": "Scott",
      "registration_date": "2021-12-14 09:45:00"
    },
    "type": "User"
  }
}
````

### /messages

#### POST
Create a Message from one user to another (or self).
This requires knowing the sender and receiver User.id.

`POST /messages`

````json
{
  "data": {
    "attributes": {
      "sender_id": 2,
      "recipient_id": 1,
      "send_time": "2021-12-14 10:06:00",
      "message": "Hey I just joined the msgapi service!"
    },
    "type": "Message"
  }
}
````

#### GET
Retrieves Messages for a particular User.
Requires the User.id of the recipient and optionally the User.id of the sender.

`GET /messages/?filter=1%2C2&sort=send_time%2Csender_id&page%5Blimit%5D=100`

For the URL parameters (shown separate below), the API service will return all messages
for the recipient from a specific sender.
To get all messages for the recipient from anyone, don't pass the sender_id parameter.
The parameters are shown urlencoded as they should be passed to the API service.

| URLEncoded           | Decoded         | Description |
| -----------          | -----------     | ----------- |
| filter=1%2C2         | filter=1,2      | Recipient Id and optional Sender Id - separated by comma
| page%5Blimit%5D=100  | page[limit]=100 | Number of results to return
| sort=send_time       | sort=send_time  | Sort by send_time


## TO-DO
 - Finish the custom filter method on Message per the requirements by
adding default message sorting, 30 day age limit and pagination.
 - Don't allow empty messages to be created.
 - Include sender name in message response data for convenience.
 - Find out if OpenAPI has a method for specifying a filter condition that
contains an inequality expression such as for dates after a certain time.
 - Determine if the custom filter method is the best way to fully customize responses
or if another url endpoint should be created.
 - Implement better error handling and send application error codes and messages in
response to failed requests.
 - Add integration tests to create users and messages through the api
and test edge cases such as messages without any message text.


## Design Notes
Being most recently familiar with Python and Flask I knew I could
be proficient with those technologies.
I also wanted to check for current best practices and popular frameworks.
Since I've also had some experience with Swagger in a Java Spring environment,
I was aware that it could handle documentation and ad-hoc testing
as well as inform the proper patterns in the application.
An internet search on "python swagger" turned up the SAFRS framework,
I decided to use it as a bootstrap environment for this protoype demo and
since it bundles SQLAlchemy, is an opportunity to get familiarity
with that Python ORM tool.


## References
 - https://github.com/thomaxxl/safrs
 - https://docs.sqlalchemy.org/en/14/tutorial
 - https://www.sqlite.org/index.html
 - https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md
 