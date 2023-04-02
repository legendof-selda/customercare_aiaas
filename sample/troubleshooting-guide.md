
**Troubleshooting Guide**


Yes, the title of this document says it all!! OpManager is a very simple and easy-to-use application and you will simply need to install the application and get started. That still does not rule out the fact that there might be a few issues coming in the way, slowing down your objective of getting your resources monitored by OpManager. This document helps you troubleshoot the common problems that you might encounter when using OpManager.. 

1. Get over initial hiccups
1. Monitoring Configurations
1. Alerting and Notifications 
1. Reporting
##
## **Tips to get over the initial hiccups**

Following are a few tips which may be handy to get over your initial hiccups when using OpManager. For easier navigation, these are further classified as follows:

- Starting Trouble
- Discovery
- Mapping

**Starting Trouble!** 

- Failed to establish connection with Web Server. Gracefully shutting down.
- Error Code 500: Error in applying the OpManager 6.0 license over opmanager 5.6 or the version upgraded from 5.0
- Can't create tables or not all the tables are created properly' error is displayed during OpManager startup.
- Error downloading client files from BE
####
#### **Failed to establish connection with Web Server. Gracefully shutting down**

**Cause 1** 

While starting OpManager as 'root' user in Linux platform, the server goes down with the following message "Failed to establish connection with web server. Gracefully shutting down ..". This is because OpManager starts its Apache Web Server as 'nobody' user and 'nobody' group. The Apache Server may not have read and execute permissions to access the files under <OpManager Home> directory. Hence, the connection to the Apache Server will not be established and the OpManager server will gracefully shut down.

**Solution** 

- Change the value of the parameter Group in httpd.conf file found under <OpManager Home>/apache/conf/backup/ directory.
- Group #-1 to Group nobody
- Provide executable permission to"httpd" file available under <OpManager Home>/apache/bin/ by executing the following command:
- chmod 755 httpd

OpManager server starts successfully after performing the above mentioned steps.

**Cause 2**

If you are using Linux 8.0/9.0 : In Linux 8.0/9.0, a file named libdb.so is not bundled. In earlier versions it was bundled. This file is needed by Apache. Without this, apache does not start in Linux 8.0. This results in the issue you are facin

**Solution**

The file has been bundled with the product and is present in the /lib/backup directory in the latest version of OpManager. Copy it to the /lib directory and restart OpManager.

This solution has worked for those using Fedora and Madrake Linux too.

If you continue to face the problem, then execute the script StartWebSvr (this will be a .bat file in Windows installation and .sh file in Linux installation) in the /apache folder of OpManager installation and send us the output.

If yours is a Debian Linux, then check if libgdbm.so.2 is available under /usr/lib directory. If not, you can install the stable version of libgdmg1. Download this package from the url http://packages.debian.org/stable/libs/libgdbmg1
####
## **Error Code 500: Error in applying the OpManager license**

**Cause**

This error is encountered where there is an incompatibility between the version of application installed, and the version specified in the procured license.

**Solution**

Contact OpManager support with the details of the version installed including the Build number and email the license sent to you. You will be sent a compatible license after verification.
##
## **Can't create tables or not all the tables are created properly' error is displayed during OpManager startup**
**Cause** 

The database tables may be corrupted.

**Solution**

You can repair the corrupt tables. Run the repairdb.bat under \bin directory. After this, run the ReInitializeOpManager.bat script in the same directory. This will remove all the tables created. Restart OpManager. 
## **Error downloading client files from BE**
**Cause**

This error occurs when the database tables are corrupted. The corruption can happen due to improper shutdown of OpManager such as during power outages.

**Solution**

The database must be repaired and OpManager needs a restart. Here are the detailed steps:

1. Stop OpManager Service
1. Open a command prompt and change directory to /opmanager/bin
1. Execute RepairDB.bat/sh. This repairs all the corrupt tables.
1. After it finishes executing, run it once again to ensure all corrupt tables are repaired.
1. Restart OpManager. 
## **Discovery**
- Devices are not discovered
- Devices are identified by IP Address and not host names. 

**Devices are not discovered**

**Cause**

This can happen if the ping requests to device get timed out.

**Solution**

To resolve this, increase the ping timeout in the file /conf/ping.properties and try again.

**Devices are identified by IP addresses and not by host names**

**Cause** 

If DNS Server address is not set properly in the machine hosting OpManager, the DNS names of the managed devices cannot be obtained from the DNS server.

The other possible reasons could be:

- The DNS Server is not reachable
- The DNS Server is down during discovery.
- The DNS Server does not exist. 

**Solution**

Ensure that the DNS Server is reachable and configure the DNS Server address properly.
## **Mapping**
- Some of my Routers are discovered as Desktops or Servers.
- How are Servers categorized in OpManager? Some servers are classified under desktops!

**Some of my Routers are discovered as Desktops or Servers**

**Cause** 

The devices may not be SNMP enabled or the SNMP agent in the device is not responding to queries from OpManager.

**Solution**

Enable SNMP and rediscover the device. Despite this, if you face issues, troubleshoot as follows:

- Do you see a blue star in the device icon on the maps? This implies that the device responds to SNMP request from OpManager. The device is still not classified properly? Simply edit the category from the device snapshot page.
- If SNMP agent is not running on the router, it will be classified as a server or desktop.You can verify this by the blue star appearing on the top left corner of the device icon for the SNMP-enabled devices. To categorize the device properly, start the SNMP agent in the device. Refer to Configuring SNMP agents in Cisco Devices for details. Rediscover the device with correct SNMP parameters.
- If the SNMP agent is running on the router and you still do not see the blue star in the device icon, then check if the SNMP parameters are properly specified during discovery. If not, rediscover the device with correct SNMP parameters.
- The router is discovered as a server or desktop if the IP Forwarding parameter of the device is set to false. To set the value of this parameter to true 
  - Invoke /opmanager/bin/MibBrowser.bat 
  - Expand RFC1213-MIB.
  - In the ip table, click ipForwarding node.
  - Type 1 in the Set Value box and click Set SNMP variable on the toolbar. 
  - Rediscover the device with correct SNMP parameters.

Similarly, for switches and printers too, enable SNMP in the device and rediscover. 

**How are Servers categorized in OpManager? Some servers are classified under desktops!** 

Following devices are automatically classified under servers based on response to SNMP/telnet request to the devices: 

- Windows 2003 Server
- Windows 2000 Server
- Windows Terminal Server
- Windows NT Server
- Linux Servers
- Solaris Servers

Following devices are classified under desktops:

- Windows 2000 Professional
- Windows XP
- Windows NT Workstation.
- Windows Millinium Home Edition
- Devices not responding to SNMP and Telnet 

If any of the servers are classified under desktops, simply import them into servers. Refer the steps mentioned to check for SNMP.
## **Monitoring Configurations**
- SNMP Monitoring
- Telnet/SSH Monitoring
- WMI Monitoring

**SNMP Monitoring**

Few reasons why SNMP-based monitors may not work are:

- Agent is not enabled on the monitored system.
- OpManager is trying to contact the agent with incorrect credentials, such as a wrong password or wrong port.
- The SNMP service in the monitored system may not be configured to accept SNMP requests from the host where OpManager is installed.
- There is a delay and the queries sent by OpManager to the agents in the monitored devices are getting timed out or the devices are no longer in the network.
- The particular OID (for which the performance monitor is configured) is not implemented in the device.

Following are few common problems encountered and the detailed procedure to troubleshoot:

- Despite SNMP being enabled on the device, the dial graphs for CPU, Memory, and Disk Utilization are not seen.
- Request timed-out error
- Error # Device does not support the required MIB
- Other common SNMP errors encountered

**Despite SNMP being enabled on the device, the dial graphs for CPU, Memory, and Disk Utilization are not seen.**

**Cause**

SNMP may not be enabled, or the SNMP agent is not responding to requests.

**Solution**

Check the SNMP configurations, rediscover the device and re-add the monitors. Troubleshoot as follows:

The possible reasons for the graphs not appearing are:

- The Resource monitors may not have been associated to this device. Associate the monitors.
- Check if SNMP is enabled properly on this device. If Yes, the Agent may not have responded to the SNMP request. Check if the Agent is responding using the Mib Browser.
- If the device has just been added, wait for the first poll to happen.

Following are the steps to troubleshoot: 

1. In the device snapshot page, scroll down to the monitors list. Click the Edit icon against a monitor. For instance, let us try the CPU Utilization monitor. Click the Test Monitor link in the resulting screen. See if the monitor responds to the test request. If it does, you will see the dial graph.
1. If there is an error message after step#1, it can be because of the snmp request to the cpu variable getting timed-out, or the oid may not be implemented in the MIB.
1. To confirm the reasons mentioned above, invoke the tool MibBrowser.bat present in /bin directory. Load the Host Resource mib and query the oid .1.3.6.1.2.1.25.3.3.1.2 for the device that is not showing the cpu dial.
1. If there is a response for the query in MibBrowser, it implies that the OID is implemented and the dial not appearing can be due to snmp timeout. So, you will need to configure the snmp timeout by including the parameter DATA\_COLLECTION\_SNMP\_TIMEOUT 15 in the file NmsProcessesBE.conf for the process 'PROCESS com.adventnet.nms.poll.Collector'. Look for the following default entry in this file:

PROCESS com.adventnet.nms.poll.Collector

ARGS POLL\_OBJECTS\_IN\_MEMORY 25 POLL\_JDBC true MAX\_OIDS\_IN\_ONE\_POLL 15 AUTHORIZATION true DATA\_COLLECTION\_QUERY\_INTERVAL 120000 PASS\_THRO\_ALL\_POLLING\_OBJECTS true CLEAN\_DATA\_INTERVAL 999999

Include the mentioned additional parameter. Now the changed entry will be as shown below:

PROCESS com.adventnet.nms.poll.Collector

ARGS POLL\_OBJECTS\_IN\_MEMORY 25 POLL\_JDBC true MAX\_OIDS\_IN\_ONE\_POLL 15 AUTHORIZATION true DATA\_COLLECTION\_QUERY\_INTERVAL 120000 PASS\_THRO\_ALL\_POLLING\_OBJECTS true CLEAN\_DATA\_INTERVAL 999999 DATA\_COLLECTION\_SNMP\_TIMEOUT 15

5. On the other hand, if there is no response in the Mib Browser, it implies that the OID is not implemented. The vendor must be requested to implement this variable for you. As an alternative, you can associate a telnet/wmi-based monitor for this device. Delete the existing SNMP-based monitor, Click the Add Monitor link again and select telnet/wmi-based monitors.
## **Request Timed-out**
**Cause**

This error is encountered when the SNMP agent in the monitored device is unable to respond to requests from OpManager within 5 secs

**Solution**

Increase the SNMP timeout in the NMSProcessesBE.conf file as detailed in the above tip.

**Error # Device does not support the required MIB**

**Cause**

This error occurs when you are trying to monitor a variable/MIB that is not implemented in that device

**Solution**

Check the MIBs supported by the device and configure custom monitors for the required variables from the supported mibs.
## **Other SNMP Errors**
Refer to the following document for detailed SNMP troubleshooting tips:

http://www.adventnet.com/products/agenttester/help/mib\_browser/mb\_error\_messages.html
## **Telnet/SSH Monitoring**
Following are few other errors that you might encounter when configuring CLI-based monitors.

- Telnet-based resource monitors not showing data
- Unable to connect: Connection refused:
- Unable to connect: No route to host:
- Unable to connect: Connection timed out:
- Request Timed out to <server name>
- Login Parameter incorrect. Read timed out.
- Exception in getting the command output: Timed out.

**Telnet-based resource monitor is not showing any data**

- If you have added a Telnet/SSH based Resource monitor, check if the UserName and Password specified are correct. Click the 'Password' link to configure the correct username and password to the device.
- Despite the correct user name and password, if you are still unable to see the dial graphs on Linux/Solaris/AIX/UX devices, try the following steps : 
- Check if the login prompts, password prompts, and the command prompts are correctly specified in the CLI credentials.
- Verify the credentials by opening a remote telnet session to these devices from the machine where OpManager is installed.
- If the login credentials are correct, it is possible that the command used to retrieve the resource data does not execute on the device, or the output is different from the expected standard format. In this case, contact support with your details and you will be assisted with the configuration changes.

**Unable to connect: Connection refused: connect**

The possible reasons for this error could be:

- Telnet is not enabled on the monitored server. Check and enable Telnet.
- The user name and password configured as part of the CLI credential is incorrect. Configure the correct name and try configured.
- It is possible that it is not a Linux/Solaris device. It might have been categorized incorrectly. Check and change the device type.

**Unable to connect: No route to host:**

The above error is encountered when the monitored device is not in the network. Plug the device into the network.

**Unable to connect: Connection timed out:**

The above error too is encountered when the monitored device is not in the network. Plug the device into the network.

**Request Timed out to <server name>**

The Telnet/SSH request sent to the device gets timed out. It is possible that the device is down, or is too busy.

**Login Parameter incorrect. Read timed out**

This error is encountered when either the user name, the password, or the login/password prompts are incorrect. Verify by opening a telnet session to the device from the machine where OpManager is installed and try connecting. 

**Exception in getting the command output: Timed out**

This exception occurs due to the following reasons:

1. The device is not in the network.
1. CLI connection is establised to the device but the device goes out of network at the time of gathering CLI command outputs from it.
## **WMI Monitoring**
Some more WMI monitoring errors with error codes

- WMI-based resource monitors not showing data
- The WMI monitors are not working. Says 'error- access denied'
- 80070005 - Access is denied
- 80041064 - User credentials cannot be used for local connections 
- 800706BA - The RPC server is unavailable 
- 80041010 - Invalid class 
- 80041003 - Access Denied 
- 80040154 - WMI Components are not registered 
- 80080005 - Internal execution failure in the WMI Service 
- 8004106C - WMI is taking up too much memory 
- 8004100E - Invalid namespace 
- 80041017 - Invalid query 

**WMI-based resource monitor is not showing any data**

- If you have added a WMI based Resource monitor, check if the UserName and Password specified are correct. Click the 'Password' link to configure the correct username and password to the device.
- Ensure that you have configured the domain administrator user name and password for WMI Monitors if the device is in a domain. Configure as <domain name>\<admin user name> in the User Name field. If the device is in a workgroup, it is sufficient to configure the device username and password.
- Despite the correct user name and password, if you are still unable to see the dial graphs in Windows devices, try the following steps 
  - Open a command prompt and change directory to /opmanager/conf/application/script
  - Type cscript cpu.vbs <device name> <domain name\admin username> <password> 
    If this command returns a proper output, you should be able to see the dials. If you encounter an error such as Error # Access denied, very the login credentials once again.
  - If the monitored device is Windows XP, try the following option too: 
    - Go to Administrative Tools -->Local Security Policy Select Security Options
    - From the options on the right, select Network access: Sharing and security model for local accounts
    - Right-click and select Properties
    - Change the privilege from Guest to Classic.
    - Remove and re-add the monitors.
    - Check to see if the monitors are up. 

**WMI Monitors are not working. It always says 'error # access denied'**

This error is encountered when the login credentials are incorrect.

Follow the steps below to resolve:

1. Verify if you have provided the domain administrator username and password to connect to the device as mentioned in the above tip. If the device is in a domain the user name should be like "domain name\administrator name".
1. If the login credentials as specified in step 1 are correct, then try associating a WMI based monitor ( preferably, a Free/Used Space in MB/GB graph ) to the Exchange Server using the Resource Monitors -> Add Monitor -> WMI based monitor -> Free/Used Disk Space in MB/GB. You should get the list of drives available in the device.
1. If step #2 does not go through, then try enabling the WMI, RPC services on the Windows system and try the same again.
1. This can also happen if the DCOM settings are not configured properly.

   You can check the exact error for this when you run a vbs script from the command prompt as in
   cmd> cd [OpManagerHome]\conf\application\scripts\
   cmd> cscript cpu.vbs [machinename] [domainname]\[username] [password]
1. You can also try configuring the dcom settings as mentioned below:

   From the Run Prompt of your Windows 2k Server, type \"dcomcnfg\" and expand the tree under Component Services -> Computers. Click on the My Computer Icon from the Icon bar and select Default Properties. Check the following:

   Enable Distributed COM on this computer 
   Enable COM Internet Services on this computer 
   Select the Default Impersonation Level as \"Impersonate\". 
   You can also edit the COM Security settings if needed. 
1. If the above 4 steps do not help, try changing the service Log-on details as follows

   Go to Windows Service UI. 
   Open "Properties" dialog of the "ManageEngine OpManager" service 
   Go to "Log On" tab 
   In the "Log on as" option select "This Account" and enter domain name\username and password, which has rights to access WMI data. 
   Save and restart opmanager.

**Note:** This will make the tray icon and splash screen disappear.

The error codes and the resolutions are explained below: 

**80070005 - Access is denied** 

**Cause**

This error occurs when incorrect login credentials are configured.

**Solution**

- If the device is in a domain, ensure to configure the correct domain name, user name, and password. If the device is in a workgroup, it is sufficient to configure only the user name and password. For instance, if the domain name is BigDom, username is admin, in the user name field, type BigDom\admin.
- It is also not necessary to specify the user name and password for devices that have user access from the machine where OpManager is installed. 
- Despite the correct credentials, if you still face issues, troubleshoot further using the following steps: 
  - Check if the user account is valid in the target machine by opening a command prompt and executing the following command:

    net use \\<monitored device name>\ADMIN$ /u:"<Domain Name\User Name>" "<password>"

    If this command throw errors, the provided user account is not valid on the target machine.
  - Check if 'Remote DCOM' is enabled in the monitored workstation. If it is not enabled, enable it as follows:
    - Select Start > Run
    - Type dcomcnfg in the text box and click OK 
    - Select the Default Properties tab 
    - Select the Enable Distributed COM in this machine checkbox 
    - Click OK

To enable DCOM on Windows XP hosts: 

1. Select Start > Run
1. Type dcomcnfg in the text box and click OK
1. Click on Component Services > Computers > My Computer 
1. Right-click and select Properties 
1. Select the Default Properties tab 
1. Select the 'Enable Distributed COM' in this machine checkbox 
1. Click OK

If the above steps do not help, try changing the service Log-on details as follows:

- Go to Windows Service UI.
- Open "Properties" dialog of the "ManageEngine OpManager" service 
- Go to "Log On" tab 
- In the "Log on as" option select "This Account". 
- Configure the user name and password here of the account which has access to the remote machine. Save and restart opmanager. 
- Try the above 3 steps again.

**Note :**You will not find the tray icon and splash screen after you make these changes. 

**80041064 - User credentials cannot be used for local connections**

**Cause**

This error is encountered when you specify the Username and password for monitoring the machine where OpManager is running.

**Solution**

Do not specify Username and password for the localhost. To resolve the issue, remove the configured user name and password from "Passwords" link in the device snapshot page.

**800706BA - The RPC server is unavailable.**

**Cause**

This error is encountered when the RPC and WMI services are not running and if the device is not pingable.

**Solution**

- Check if the device is up and running, and pingable.
- Check the Remote Procedure Call(RPC) and Windows Management Instrumentation(WMI) Services are running 
  - Select Start > Run 
  - Type 'services.msc' in the text box and click OK 
  - In the listed services, see if the status of RPC and WMI services are shown as started.
  - Start the services if it is not started. 
- A firewall might be configured on the remote computer. Such exceptions mostly occur in Windows XP (with SP 2), when the default Windows firewall is enabled. Disable the default Firewall in the Windows XP machine as follows: 
  - Select Start > Run 
  - Type Firewall.cpl and click OK 
  - In the General tab, click Off 
  - Click OK. 
- If the firewall cannot be disabled, Enable Remote Administration(for administrators) by executing the following command on the remote machine : "netsh firewall set service RemoteAdmin" 
- A firewall might be blocking the WMI traffic. Give access to WMI traffic in the firewall. You will need to open the ports 445,135 in the firewall. 

**80041010 - Invalid class**

**Cause**

This error occurs when the required WMI class is not registered.

**Solution**

- Check whether the desired application is installed.
- To register all the WMI classes for the installed application. Run the below commands: 
  - For Windows 2000 'winmgmt /resyncperf' command from the monitored device. 
  - For Windows XP and 2003 'wmiadap /f' command from the monitored device.

**80041003 - Access Denied**

**Cause**

This error occurs when the user name provided does not have sufficient access privileges to perform the operation.

**Solution**

1. It is possible that this user does not belong to the Administrator group for this host machine.
1. Try moving the user to the Administrator Group of the workstation.
1. Try with an administrator (preferably a Domain Administrator) account. 

**80040154 - WMI Components are not registered**

**Cause**

This error occurs when the WMI is not available in the remote windows workstation. This happens in Windows NT. Such error codes might also occur in higher versions of Windows if the WMI Components are not registered properly.

**Solution**

- Install WMI core in the remote workstation. This can be downloaded from the Microsoft web site. 
- Register the WMI DLL files by executing the following command in the command prompt:
  winmgmt /RegServer
- Install the WMI for Windows NT by downloading the below exe:
  http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=C174CFB1-EF67-471D-9277- 4C2B1014A31E

**80080005 - Internal execution failure in the WMI Service**

**Cause**

This error occurs when there is some internal execution failure in the WMI Service (winmgmt.exe) running in the host machine. The last update of the WMI Repository in that workstation could have failed.

**Solution**

Restart the WMI Service in the remote workstation:

1. Select Start > Run. 
1. Type Services.msc and click OK. 
1. In the Services window that opens, select Windows Management Instrumentation service. 
1. Right-click and select Restart

**8004106C - WMI is taking up too much memory**

**Cause**

This error occurs when WMI is taking up too much memory. This could be caused either by low memory availability or excessive memory consumption by WMI.

**Solution**

- WMI is taking up too much memory.
- This could be caused either by low memory availability or excessive memory consumption by WMI.
- Try restarting or reinstalling the wmi service. 

**8004100E - Invalid namespace**

**Cause**

Invalid namespace Compiler is not a normal error. It is possible that the desired application using the namespace is not installed properly.

**Solution**

- Try re-installing the application or the WMI services alone.
- Contact http://support.opmanager.com with logs. 

**80041017 - Invalid query**

**Cause**

'Query was not syntactically valid' is not a normal error. It is possible that the desired application using the namespace is not installed properly. 

**Solution**

- Try reinstalling the application or the WMI services alone. 
- Contact support with logs.

For any other error codes, refer the MSDN knowledge base. 
## **Alerting and Notification**
- Email notifications are not received
- Error! page is displayed when a profile is selected 
- Modem-based SMS notifications are not working

**Email notifications are not received**

**Cause**

Profile may not be associated to the device, or the mail-server settings may be incorrect

**Solution**

- Check if the notification profile is associated to the device
- Check if the correct criterion is selected in the profile configuration
- Ensure the mail-server settings are configured correctly.

**Error! page is displayed when a profile is selected.**

**Cause**

The profile name may contain special characters or a space

**Solution**

You will not be able to delete the profile from the client in such case. So, follow the steps below:

1. Stop OpManager
1. Open the file /conf/alert.filters
1. Remove the <FILTER>...</FILTER> element containing the profile configuration. 
1. Restart OpManager. 

**Modem-based SMS notifications are not working. The message 'Check the modem settings' alone is seen.**

There are quite a few things that you need to take note of when configuring modem-based sms alerts. Here it goes: 

**Prequisites to configure SMS alerts:**

- Need to have the supported mobile and modem, Sim Card, Serial Cable, and USB Driver.
- Works only on Windows OS

**Required USB Driver:**

The modem and the mobile vendors provide the required modem/mobile drivers. For instance, you can get the driver for Nokia from the following link:

http://www.nokia.com/A4144937

**Required Cables :**

This depends on your mobile phone model. For Nokia 62xx/63xx, you need DLR-3P cable. Newer Nokia models use DKU-9 USB cable. In such case you need to download the driver from Nokia's website, which creates a virtual communication port. Other brands have their own cables, usually USB ones. GSM Modems have a serial port and so you will need a standard serial cable. 

**Identifying the port at which the modem/mobile is connected:**

1. Go to My Computer->Control Panel->System->Hardware->Device Manager- >ports.
1. Here you will find the port to which the Modem\Mobile is connected. 
1. If it is not available, then 
1. Go to My Computer->Control Panel->System->Hardware->Device Manager->Modems.

After the system system detects the port to which the Modem\Mobile is connected, connect it to OpManager as follows: 

1. Start OpManager.
1. Go to Admin->SMS Server Settings.
1. Type the port number to which the modem/mobile is connected in the SMS Server Settings page. 
1. If the Mobile\Modem is connected to the specified port, the Mobile\Modem details are shown.
1. Configure an SMS alert from Admin->Notification Profiles->SMS Alert->Modem based SMS and associate to the devices.

OpManager is ready to send the SMS notifications whenever an alarm is generated.

**System detects the port to which the modem/mobile is connected but OpManager fails to detect it:**

- Ensure that the mobile or modem is supported in OpManager. 
- Ensure that the correct port number is correct and is of the format - COM5 or com5. 
- Also check for the validity of the SIM.
## **Reporting**
- Top N Reports shows No Data Available
- All Servers Disk Usage Report shows No Data Available
- Top N Volumes having Low/More Disk Space report shows No Data Available
- Junk Characters in Interface Reports
- NA in All Servers Disk Usage Report
- Applications Reports show No Data Available

**Top N Reports shows No Data Available**

To view the CPU utilization, Memory Utilization, Disk Utilization, Interface Traffic, Interface Utilization and Interface Errors reports, you need to have SNMP installed in the managed devices. Reports list only the SNMP-enabled devices. For non-SNMP servers, data can be collected using CLI (for Unix-based servers), and WMI (for Windows devices).

OpManager requires a minimum of 1 hour to plot the collected data. Try accessing the reports after 1 hour from server startup.

**All Servers Disk Usage Report shows No Data Available**

To view the All Server Disk Usage report, you must assign the Free Disk Space and Used Disk Space monitors to the managed devices. Assign both the Used Disk Space and Free Disk Space monitors to the devices and wait for two polling intervals and then view the report again.

**Top N Volumes having Low/More Disk Space report shows No Data Available**

To view the partition-wise reports, you must assign the Free Disk Space and Used Disk Space graphs to the managed devices. Refer to Assigning a Graph Profile to a Device for details.

Assign both the Used Disk Space and Free Disk Space graphs to the devices, wait for two polling intervals and then view the report again.

**Junk characters in Interface Reports**

In Chinese or Japanese version of OpManager, if the SNMP agents sends data as Unicode characters, OpManager might not be able to translate it properly and hence display the values as junk. 

To display this properly, you need to specify the encode type of your agent in the Device Settings dialog. In the device snapshot page, select Device Properties link under Configure tab. Enter the encode type in the Encoding Box and click Save.

**"NA" in All Servers Disk Usage Report**

You will see NA in All Servers Disk Usage report if you have not assigned both the Used Disk Space and Free Disk Space graph profiles to the managed devices. 

Assign both the Used Disk Space and Free Disk Space graphs to the devices, wait for two polling intervals and then view the report again.

**Service Reports show No Data Available**

The TCP Services reports such as HTTP Servers by Response Time, SMTP Servers by Response Time, and others can produce results only if the service is running in at least one of the managed devices. Otherwise, the report shows No Data Available.

**Knowledgebase**

For further tips to troubleshoot or find resolutions, dig into our online knowledgebase or write to us at our Support Portal.
8

