# dmg-task

Pre Reqs:
- ``firefox 77 `` - (Test are developed to run in headless mode)
- ``python 3.6+`` 

How to Run:
- ``git clone https://github.com/mraeeschachar/dmg-task.git`` - (Clone this repo)
- ``cd dmg-task`` - (Go to project root folder in terminal)
- ``pip3 install -r requirements.txt`` - (Install requirements)

To Run Functional tests:
- ``nosetests -v tests/`` - (All tests would run in headless mode)

To Run API tests:
- ``nosetests -v api_tests/`` 

To Run Locust tests: 
- ``locust -f locust_tests/locustfile.py`` - (Server would start)
- ``http://127.0.0.1:8089/`` - (Open this url to see web interface)
- ``Add Number of total users to simulate``
- ``Add Hatch rate``
- ``Add "https://dog.ceo/api" in Host field``
- ``Click Start swarming`` - (Now you can view live the performance on this web interface)