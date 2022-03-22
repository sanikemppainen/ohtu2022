*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Submit Credentials
    Click Button  Login

Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}
    
Submit Registration
    Click Button  Register

Login Should Succeed
    Main Page Should Be Open

#confirm?
Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}



