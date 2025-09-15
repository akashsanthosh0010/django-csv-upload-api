1. Clone the Repo
git clone https://github.com/akashsanthosh0010/django-csv-upload-api.git
2. Move to Project Folder
cd django-csv-upload-api
3. Create Virtual env
python -m venv venv
venv\Scripts\activate - For Windows
4. Run Migrations
python manage.py makemigrations
python manage.py migrate
5. Start the server
python manage.py runserver

API USAGE - POSTMAN

1. Call the api - http://127.0.0.1:8000/users-api/upload-csv/
2. In the body section select form-data then name the file as "file" and select file instead of text and upload the file
3. Select POST Method too
4. And Send the Request
5. Sample Response
{
    "saved_records": 2,
    "rejected_records": 2,
    "errors": [
        {
            "row": 2,
            "error": {
                "age": [
                    "Age must be above 0 and below 120 "
                ]
            }
        },
        {
            "row": 4,
            "error": {
                "email": [
                    "user with this email already exists."
                ]
            }
        }
    ]
}


