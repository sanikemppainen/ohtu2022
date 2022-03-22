*** Settings ***
Resource  resource.robot
Resource  loginresource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Login Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kallekalle
    Set Password  sanasana123
    Set Confirmation  salasana123
    Submit Registeration
    Registeration Should Succeed

Register With Too Short Username And Valid Password
# ...

Register With Valid Username And Too Short Password
# ...

Register With Nonmatching Password And Password Confirmation
# ...

*** Keywords ***
Set Confirmation
    [Arguments]  ${confirmation}
    Input Text  password_confirmation   ${confirmation}


Create User And Go To Login Page
    Create User  kalle  kalle123
    Go To Login Page
    Login Page Should Be Open