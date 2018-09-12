

We request that you write a Python exploit that will automate the attack technique you picked. (You may decide to write the exploit in powershell/bash)

--> It  will execute  ping cmd and get ping result .
    permission : user
    process command line parameters and get the result.

1. Your exploit should clearly define attack preconditions 
 --> ([Operating System = "Linux", Software Installed = ""])

2. Your exploit should clearly define attack action (Execution of the attack)
 --> attack action : execution 

3. Your exploit should clearly define postconditions (This will act as a validation check if your exploit was either successfully/failed)
 --> python demo.py

4. Your exploit should finally contain a comprehensive clean-up method which will remove any files, directories and reset configurations changed/added by the attack action


Your exploit should be easy to set up, and should run on either Linux or Mac OS X. It should not require any non open-source software. The exploit will be tested in a virtual machine lab based on the clearly defined preconditions.

There are many ways that this exploit could be built; we ask that you build it in a way that showcases one of your strengths. If you you enjoy documentation, do something interesting with defining the preconditions. If you like object-oriented design, feel free to dive deeper into the model of this problem. We're happy to tweak the requirements slightly if it helps you show off one of your strengths.

## Bonus Points
Using orchestration software (Salt, Ansible, Puppet, Chef, and/or deployment scripts) to provision attack target machine state (meeting attack preconditions)

Once you're done, please submit a paragraph or two in your `README` about what you are particularly proud of in your implementation, and why.

## Evaluation
Evaluation of your submission will be based on the following criteria. 

1. Did your exploit fulfill the basic requirements?
2. Did you document the method for setting up and running your exploit?
3. Did you follow the instructions for submission?
4. Does your exploit work


