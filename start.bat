del signed_student.txt
echo 2> signed_student.txt

start cmd /k py .\classchecker_server.py
start cmd /k py .\classchecker_client.py