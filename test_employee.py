from employee import employee_details

def test_employee_details():
    expected_output = (
        "Employee Name: Akkamma\n"
        "Employee ID: 276\n"
        "Department: IT\n"
        "Salary: 55000"
    )
    assert employee_details("Akkamma", "276", "IT", 55000) == expected_output
