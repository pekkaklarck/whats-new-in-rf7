*** Settings ***
Library         Library.py
Test Tags       common    tags

*** Test Cases ***
VAR syntax
    VAR    ${name}    Robot Framework
    VAR    ${longer}    aldjf la jslajsdf lksadlkf jalsj
    ...    alsdk jlsakdjflsakdj
    ...    lasdjflasdjf
    VAR    ${multiline}
    ...    first line
    ...    second line
    ...    last line
    ...    separator=\n
    VAR    @{list}    first item    second item
    ...    last item
    Log Many    ${name}    ${longer}    ${multiline}
    ...    ${list}

    VAR    ${SUITE LEVEL}    value    scope=SUITE
    Log    ${SUITE LEVEL}

VAR continued
    Log    ${SUITE LEVEL}

-tag syntax
    [Tags]    -common    own
    No Operation

Return setting deprecation
    ${value} =    Return something
    Should Be Equal    ${value}    something

Mixed arguments with library keywords
    Number of horses should be    1
    Number of horses should be    count=7
    Number of dogs should be    4

Literal conversion
    Turn    left
    Turn    RIGHT
    Turn    around


*** Keywords ***
Return something
    RETURN    something
