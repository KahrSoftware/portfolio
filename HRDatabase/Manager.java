/* *****************************************
* CSCI205 - Software Engineering and Design
* Fall 2018
*
* Name: Justin Kahr
* Date: Sep 19, 2018
* Time: 12:09:05 PM
*
* Project: CSCI205
* Package: lab10
* File: Manager
* Description: A subclass of employee who is in charge of a department
*
* ****************************************
 */
package HRDatabase;

import java.util.ArrayList;
import java.util.Date;

/**
 *
 * @author jjk033
 */

public class Manager extends Employee {

    private DeptType dept;
    private ArrayList<Employee> empList = new ArrayList<Employee>();

    public Manager(int empID, String firstName, String lastName, int ssNum,
                   Date hireDate, double salary, String deptName) {
        super(empID, firstName, lastName, ssNum, hireDate, salary);
        setDeptName(deptName);
    }

    public Manager(int empID, String firstName, String lastName, int ssNum,
                   Date hireDate, double salary, String deptName,
                   ArrayList<Employee> empList) {
        super(empID, firstName, lastName, ssNum, hireDate, salary);
        setDeptName(deptName);
        this.empList = empList;
    }

    /**
     * An collection of the various types of managers
     */
    private enum DeptType {
        ENGINEERING, HR, ADMIN, STAFF, OTHER;
    }

    /**
     * Get the value of deptName
     *
     * @return the value of deptName
     */
    public String getDeptName() {
        return dept.name();
    }

    /**
     * Set the value of deptName
     *
     * @param deptName new value of deptName
     *
     */
    public void setDeptName(String deptName) {
        try {
            this.dept = DeptType.valueOf(deptName.toUpperCase());
        } catch (IllegalArgumentException e) {
            System.out.println("ERROR: UNKNOWN MANAGER TYPE");
        }
    }

    /**
     * Adds a new employee to the manager
     *
     * @param emp The employee to be added
     * @throws ManagerException
     */
    public void addEmployee(Employee emp) throws ManagerException {
        if (empList.contains(emp)) {
            throw new ManagerException(
                    "ERROR: EMPLOYEE IS ALREADY MANAGED BY THIS MANAGER");
        }
        empList.add(emp);
    }

    public ArrayList<Employee> getEmpList() {
        return empList;
    }

    /**
     * Removes and employee from the manager
     *
     * @param emp The employee to be removed
     * @throws ManagerException
     */
    public void removeEmployee(Employee emp) throws ManagerException {
        if (!empList.contains(emp)) {
            throw new ManagerException(
                    "ERROR: EMPLOYEE IS NOT MANAGED BY THIS MANAGER");
        }
        empList.remove(emp);
    }

    @Override
    public String toString() {
        return super.toString() + ", Manager{" + "deptName=" + this.getDeptName() + '}';
    }

}
