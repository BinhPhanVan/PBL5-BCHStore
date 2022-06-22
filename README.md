### This is a website for a laptop store, built on django and to get the project running follow these steps:
1. Clone repositories
    ```
    git init 
    git clone https://github.com/BinhPhanVan/python-bch-store-laptop.git
    ```
2. Open up move into project
    ```
    cd .\python-bch-store-laptop\
    ```
3. Create virtual environment and install library
    ```
    python -m venv venv
    venv/Scripts/activate
    pip install -r requirements.txt
    ```
4. Run project
    ```
    python manage.py runserver
    ```
Note: 
* Since the database is pre-made, you only need to log in with admin rights:
    - username: admin
    - password: password
* Then you implement more website data and functionality

#### You can visit the website after deploying with heroku  
[https://dut-bch-shop.herokuapp.com/](https://dut-bch-shop.herokuapp.com/)
