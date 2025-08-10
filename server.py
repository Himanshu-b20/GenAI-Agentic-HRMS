from typing import Dict
from email.message import EmailMessage
from emails import EmailSender
from mcp.server.fastmcp import FastMCP
from utils import seed_services
from hrms import *
import os
from dotenv import load_dotenv

_ = load_dotenv()

mcp = FastMCP('hrms-mcp-server')
email_sender = EmailSender(
        smtp_server="smtp.gmail.com",
        port=587,
        username=os.getenv("EMAIL"),
        password=os.getenv("EMAIl_PWD"),
        use_tls=True
    )

employee_manager = EmployeeManager()
leave_manager = LeaveManager()
meeting_manager = MeetingManager()
ticket_manager = TicketManager()

seed_services(employee_manager, leave_manager, meeting_manager, ticket_manager)

@mcp.tool()
def add_employee(name:str, email:str, manager_id:str) -> str :
    """
    Add a new employee to HRMS system
    Args:
        name: employee name
        email: employee email id
        manager_id: manager Id (optional)

    Returns: Confirmation message

    """
    emp = EmployeeCreate(name=name, email=email, manager_id=manager_id, emp_id=employee_manager.get_next_emp_id())
    employee_manager.add_employee(emp)
    return f'Employee {name} added successfully!'

@mcp.tool()
def get_employee_details(name:str)->Dict[str, str]:
    """
    Get employee details by name.
    Args:
        name: Name of employee

    Returns: employee Id and manager Id

    """
    emp_list = employee_manager.search_employee_by_name(name)
    if len(emp_list) == 0:
        raise ValueError(f'No employee found with name: {name}')
    return employee_manager.get_employee_details(emp_list[0])

@mcp.tool()
def get_employee_details_by_id(emp_id:str)->Dict[str, str]:
    """
    Get employee details by Employee id.
    Args:
        emp_id: Name of employee

    Returns: Details of employee

    """
    return employee_manager.get_employee_details(emp_id=emp_id)

@mcp.tool()
def send_email(to_email_id: List[str], subject: str, body: str):
    """
    Send email to multiple employee
    Args:
        to_email_id: List of employee email ids
        subject: email subject
        body: email body

    Returns: Confirmation msg

    """
    email_sender.send_email(
        subject=subject,
        body=body,
        to_emails=to_email_id,
        from_email=email_sender.username
    )
    return "Email sent Successfully!"

@mcp.tool()
def create_ticket(emp_id:str, item:str, reason:str) -> str:
    """
    Create ticket for equipments
    Args:
        emp_id: Employee Id
        item: Item name for which ticket need to be created
        reason: Reason to create ticket

    Returns: Confirmation message

    """
    create_tkt = TicketCreate(
        emp_id=emp_id,
        item=item,
        reason=reason
    )
    return ticket_manager.create_ticket(create_tkt)

@mcp.tool()
def schedule_meeting(emp_id: str, meeting_date: datetime ,topic: str):
    """
    Schedule introductory meeting
    Args:
        emp_id: Employee id
        meeting_date: Meeting date
        topic: Meeting reason

    Returns: Confirmation message

    """
    details = MeetingCreate(
        emp_id=emp_id,
        meeting_dt=meeting_date,
        topic=topic
    )
    return meeting_manager.schedule_meeting(details)

@mcp.tool()
def apply_leave(emp_id: str, leave_date: List[date]):
    """
    Apply for leaves for an employee
    Args:
        emp_id: Employee Id
        leave_date: Leave dates list

    Returns: Confirmation message

    """
    leave_details  = LeaveApplyRequest(
        emp_id=emp_id,
        leave_dates=leave_date
    )
    return leave_manager.apply_leave(leave_details)

@mcp.tool()
def get_leave_balance(emp_id: str):
    """
    Get the balance of the leaves for an employee
    Args:
        emp_id: Employee Id

    Returns: Confirmation message

    """
    return leave_manager.get_leave_balance(emp_id)

@mcp.prompt("on_boarding_employee")
def onboarding_new_employee(employee_name: str, manager_name:str):
    return f"""
        On-boarding new employee with following details:
        - Employee name :{employee_name},
        - Manager name : {manager_name}
        
        Steps to follow-
        - Add the employee to HRMS system
        - Send the welcome email to employee with login credentials. Format (employee_name@abcz.com)
        - Notify the manager about the new employee's onboarding. 
        - Raise the ticket for laptop, Id card and other necessary equipments.
        - Schedule a introductory meeting with the new employee and manager
"""

@mcp.prompt("employee_leave_management")
def leave_management(employee_id :str, leave_date:str):
    return f"""
    Apply for leave of an employee with following details:
    Employee Id : {employee_id}
    Leaves Date : {leave_date}
    
    After applying the leaves also get the leave balance and employee name for that particular employee and show the summary in table format.
"""

if __name__ == '__main__':
    mcp.run(transport='stdio')