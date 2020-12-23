/* *****************************************
* CSCI205 - Software Engineering and Design
* Fall 2018
*
* Name: Justin Kahr
* Date: Sep 20, 2018
* Time: 9:32:55 PM
*
* Project: CSCI205
* Package: lab10
* File: HRUtility
* Description: Utility methods useful for the Employee class
*
* ****************************************
 */
package HRDatabase;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;

/**
 *
 * @author jjk033
 */
public final class HRUtility {

    private static SimpleDateFormat empDateFormat = new SimpleDateFormat(
            "yyyy-MM-dd");

    /**
     * Takes an employee and prints out their info
     *
     * @param emp The employee which should be printed out
     */
    public static void displayEmployee(Employee emp) {
        System.out.println(
                emp.getEmpID() + ":\t" + emp.getFirstName() + " " + emp.getLastName() + (emp instanceof Manager ? "\t [MANAGER] " + ((Manager) emp).getDeptName() : ""));
    }

    /**
     * Takes a list of employees and prints out their info using the
     * displayEmployee method
     *
     * @param listOfEmps The employees which should be printed out
     */
    public static void displayEmployees(ArrayList<Employee> listOfEmps) {
        for (Employee emp : listOfEmps) {
            displayEmployee(emp);
        }
        System.out.println();
    }

    /**
     * Takes a manager and prints out their info using the displayEmployee class
     * and prints their employees using the displayEmplyees class
     *
     * @param mgr The manager which should be printed out
     */
    public static void displayManager(Manager mgr) {
        displayEmployee(mgr);
        ArrayList<Employee> empList = mgr.getEmpList();
        System.out.println(
                "Number of Employees: " + empList.size() + "\n----------");
        displayEmployees(empList);
    }

    /**
     * Helper method to parse a date string into a date object. This is really
     * here just to show how to deal with an exception that may be thrown in a
     * method.
     *
     * @param sDate - a date string
     * @return a <code>Date</code> object
     * @throws ParseException if the string cannot be parse correctly.
     */
    public static Date strToDate(String sDate) throws ParseException {
        return empDateFormat.parse(sDate);
    }

    /**
     * Formats the date as a string
     *
     * @param date The date to be formatted
     * @return The formatted string
     */
    public static String dateToStr(Date date) {
        return empDateFormat.format(date);
    }

}
