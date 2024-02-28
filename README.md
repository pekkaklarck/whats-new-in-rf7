# What's new in Robot Framework 7.0

This repository contains examples that I created as part of my [RoboCon Online 2024](https://robocon.io) presentation. You can study the examples here and also run them on your own environment.

Examples are in the following files:

- [tests.robot](tests.robot) contains examples demonstrating the new syntax and enhancements to the library API.
- [Library.py](Library.py) is the library with new features used by the aforementioned tests.
- [Listener.py](Listener.py) is a listener using new features in the listener API.

To run examples demonstrating the new syntax as well as enhancements to the library API, simply run the following command and study the generated log file:

    robot tests.robot

If you want to see enhancements to the listener API in action, you need to take the included listener into use:

    robot --listener Listener.py tests.robot

The listener does modifications that are seen in the log file and also writes some information to the console. To make it easier to read the latter information, you can disable the normal console output:

    robot --quiet --listener Listener.py tests.robot

More information:

- [Robot Framework 7.0 release notes](https://github.com/robotframework/robotframework/blob/master/doc/releasenotes/rf-7.0.rst)
- [More listener examples](https://github.com/robotframework/robotframework/tree/master/atest/testdata/output/listener_interface/body_items_v3)
