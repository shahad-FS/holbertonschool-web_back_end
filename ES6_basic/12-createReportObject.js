export default function createReportObject(employeesList) {
  return {
    allEmployees: { ...employeesList },
    getNumberOfDepartments(employees) {
      return;
Object.key(employees).length;
    },
  };
}
