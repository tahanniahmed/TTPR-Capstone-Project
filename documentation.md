# TTPR-Capstone-Project
Final project for Cybersecurity Capstone – Brute Force attack detection using Microsoft Azure Virtual Machine, Python and Splunk.

# VM Provisoning
Prerequisites:
  - Cloud platform account (In this project we use Azure)
    - If you are a student you can get a free trial to create VMs
  - Access to virtual network or subnet
  - SSH key pair or credentials for remote access

Step 1:  
log into your Azure account and look up "Virtual Machines" in the search bar and redirect to it.  
<img width="500" height="175" alt="image" src="https://github.com/user-attachments/assets/29bd2386-0e47-40aa-bb93-2fc01569f440" />

Step 2:  
Now it is time to make your VMs. On the virtual machine page click on the create drop down and select "Virtual Machines" to be redirected to the VM specification page.  
<img width="200" height="200" alt="Screenshot 2025-08-05 at 3 22 51 PM" src="https://github.com/user-attachments/assets/c90ce9e7-16ed-4811-9135-a8847c7b53d7" />

Step 3:  
Now it is time to set up the two VMs  
  Step 3.1:  
  First set up the target VM using the following specifications  
  Subscription: Which ever one you have access to  
  Region: Recomended to select the region you are located in
  Image(OS): Windows
  Size: Standard D2s v3 - vCPUs 2, 8 GiB memory
  Administrator account: Set up a 
