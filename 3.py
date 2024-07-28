import subprocess
from twilio.rest import Client

def run_script_background(script_path):
    subprocess.Popen(['python', script_path])

sms_script_path = 'C:\\Users\\ASUS\\ProjectTesting\\PythonMLProjects\\MyProject\\sms.py'
call_script_path = 'C:\\Users\\ASUS\\ProjectTesting\\PythonMLProjects\\MyProject\\call.py'
whatsapp_script_path = 'C:\\Users\\ASUS\\ProjectTesting\\PythonMLProjects\\MyProject\\whatsapp.py'

run_script_background(sms_script_path)
run_script_background(call_script_path)
run_script_background(whatsapp_script_path)
