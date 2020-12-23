## HR Database
This project is the result of an object oriented design lab from school. The program is a HR Database system written in Java. There is also a UML diagram describing the class setup.

`HRDBSystem.java` contains the main method, which serves as a sort of test script, adding example employees and managers. The class `Employee.java` defines an employee of the company using the system, and `Manager.java` inherits from the employee class while also adding functionality for relating employees as directly under a manager. Finally, `HRUtility.java` contains functions which allow interaction with employees and `ManagerException.java` defines an exception used when an employee and manager are incorrectly assumed to be related.

To compile and run the project:

- Ensure you have java installed.
- From outside the `HRDatabase` directory run the command:
- `	javac HRDatabase/*.java`.
- Run `java HRDatabase/HRDBSystem`.