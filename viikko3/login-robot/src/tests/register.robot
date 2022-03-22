*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Register Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  tiina2  tiinatiina123
    Output Should Contain  New user registered


Register With Already Taken Username And Valid Password
    Input Credentials  tiina  tiina123
    Output Should Contain  User with username tiina already exists

Register With Too Short Username And Valid Password
    Input Credentials  ti  tiina123
    Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Input Credentials  tiina  sa
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  tiina  salasana
    Output Should Contain  Password isn't secure enough


*** Keywords ***
Create User And Input Register Command
    Create User  tiina  tiinatiina123
    Input Register Command
