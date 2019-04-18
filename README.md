# AWSRemoteCommandRun

## Setting up virtual environment

1) Installing virtual environmnet
    		py -m pip install --user virtualenv

2) creating virtual environment
        	py -m virtualenv env

3) Activating Virtual environment
           .\env\Scripts\activate


## SSM configuration agents

1) install this in windows server
            https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/windows_amd64/AmazonSSMAgentSetup.exe
2) in windows server powershell run this command 
            Restart-Service AmazonSSMAgent
    or go to the installed path run the exe. 
