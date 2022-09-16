# MainAssignment
Ticketing system using python+django+docker


1) pre-requisit: docker-desktop, ubuntu18.04
2) clone into local system
3) run docker-compose up
4) go to http://localhost:800/api/resiter to resiter using user,pass,email
5) go to http://localhost:800/api/login  with username and password which will generate access token
6) using vscode thunder client make post request on http://localhost:800/apiticketrequest url to access rest of features by updating bearer token and body
7) updated input for different request in input_json.txt file
8) check all request logs in event_log table