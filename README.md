
## Setup

### Prerequisites

- [Python](https://www.python.org/) installed
- Redis installed

### Installation

1. Navigate to the project directory:

    ```bash
    cd your-repository
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Linux:

        ```bash
        source venv/bin/activate
        ```

    - On Windows (Command Prompt):

        ```bash
        .\venv\Scripts\activate
        ```

        On Windows (PowerShell):

        ```bash
        .\venv\Scripts\Activate.ps1
        ```

4. Install project dependencies:

    ```bash
    pip install -r requirements.txt
    ```
5. Set PRODUCTION = False in settings.py

6. Apply migrations:

    ```bash
    python manage.py migrate
    ```

7. Create a superuser (optional):

    ```bash
    python manage.py createsuperuser
    ```

### Usage

1. Run the development server:

    ```bash
    python manage.py runserver
    ```

    The project will be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

2. Access the admin panel:

    - Create an admin user if not done during setup.
    - Visit [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and log in.
    - For Setup open ai configuration
    - Visit [http://127.0.0.1:8000/admin/chatai/siteconfig/](http://127.0.0.1:8000/admin/chatai/siteconfig/).

