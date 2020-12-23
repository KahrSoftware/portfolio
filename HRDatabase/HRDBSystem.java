/* *****************************************
* CSCI205 - Software Engineering and Design
* Fall 2018
*
* Name: Justin Kahr
* Date: Sep 19, 2018
* Time: 12:20:55 PM
*
* Project: CSCI205
* Package: lab10
* File: HRDBSystem
* Description: A HR Database using the employee class and its subclasses
*
* ****************************************
 */
package HRDatabase;

import java.text.ParseException;
import java.util.ArrayList;

/**
 *
 * @author jjk033
 */
public class HRDBSystem {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws ParseException, ManagerException {

        //Create two managers
        Manager mgr1 = new Manager(0, "Michael", "Scott", 19572847,
                                   HRUtility.strToDate("1995-31-12"),
                                   75000,
                                   "Admin");

        Manager mgr2 = new Manager(1, "Dwight", "Schrute", 18376295,
                                   HRUtility.strToDate("2007-07-07"),
                                   40000, "Engineering");

        //Create a list of employees
        ArrayList<Employee> empList = new ArrayList<Employee>();

        empList.add(new Employee(1, "Jim", "Halpert", 693928567,
                                 HRUtility.strToDate("2004-05-23"), 30000));

        empList.add(new Employee(2, "Andy", "Bernard", 238546738,
                                 HRUtility.strToDate("2012-10-16"), 25000));

        empList.add(new Employee(201, "Stanley", "Hudson", 572947388,
                                 HRUtility.strToDate("1994-03-08"), 35000));

        empList.add(new Employee(4, "Phyllis", "Vance", 322957384,
                                 HRUtility.strToDate("2002-11-30"), 30000));

        empList.add(new Employee(0, "Pam", "Beasly", 840928832,
                                 HRUtility.strToDate("2003-10-02"), 15000));

        empList.add(new Employee(200, "Toby", "Flenderson", 970254275,
                                 HRUtility.strToDate("2003-08-15"), 15000));

        //Assign the employees to managers
        mgr1.addEmployee(empList.get(0));
        mgr1.addEmployee(empList.get(4));
        mgr1.addEmployee(empList.get(5));

        mgr2.addEmployee(empList.get(1));
        mgr2.addEmployee(empList.get(2));
        mgr2.addEmployee(empList.get(3));

        //Display it all
        HRUtility.displayEmployees(empList);

        HRUtility.displayManager(mgr1);
        HRUtility.displayManager(mgr2);

    }

}
