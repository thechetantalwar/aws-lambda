## Instructions
* Create a Lmabda Function with Runtime "Python"
* Then paste the code which we do have in getInstances.py file in the IDE which is there on Lambda Page
* Now if you try executing your fucntion, it will fail with message stating "Unauthorized Operation"
* You can provide permissions, either by creating a new role with required permissions added or you can edit the existing one as well.
* Let's edit the existing only.
* Go to configuration -> Permissions -> Click on the Role name, it will take you to the IAM role page
* Click on Attach Policies
* Filter the policies out for "AmazonEC2ReadOnlyAccess", and select it
* Click on Attach Policy
* Now you have provied the needed permissions to the role, now your lambda function can execute.
* Go to lambda function page, and execute it, this time you will witness it returing the Instance Ids.
