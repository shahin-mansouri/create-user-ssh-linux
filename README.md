# User Traffic Restriction Service

This Django-based service allows administrators to create restricted Ubuntu users who can only utilize the server's traffic resources. It is designed to provide controlled access to server resources, ensuring that users have limited permissions and can only interact with the server's traffic.

## Features

- **Create Restricted Users**: Automatically generate Ubuntu users with limited access.
- **Traffic-Only Access**: Users can only use the server's traffic and have no additional permissions.
- **Admin Dashboard**: Manage users and monitor their activity through a simple Django admin interface.
- **Secure**: Ensures that restricted users cannot perform unauthorized actions on the server.

## Prerequisites

Before setting up the service, ensure you have the following installed:

1. **Python 3.x**: The service is built using Python.
   ```bash
   sudo apt-get install python3
   ```

2. **Django**: The web framework used to build the service.
   ```bash
   pip install django
   ```

3. **Ubuntu Server**: The service is designed to run on Ubuntu.

4. **Superuser Privileges**: You need sudo access to create users and manage the server.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shahin-mansouri/create-user-ssh-linux.git
   cd mysite
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser for the Django admin panel:
   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the admin dashboard at `http://127.0.0.1:8000/admin/` and start managing users.



## Author

This service was developed by **Shahin Mansouri**. For more information, contact **mansouri.math.kntu@gmail.com**.

---

This README provides a comprehensive guide to setting up and using your Django-based service. If you have any questions or suggestions, feel free to reach out!
