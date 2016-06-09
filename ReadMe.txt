FEATURES OF THE WEB APP:

Users can :

	1. View a list all music track details. 
	2. Add music track with details like Title, Genres, Rating.
	3. Add genre with its name. 
	5. Edit specific track title, genre and rating.
	5. Can search track based on track or genres name.
	
 

INSTALLATION

1. Make a Virtual Environment.
2. Clone the repository with git clone https://github.com/Amanbg/Music-Web-App.git
3. Go to the directory Music-Web-App/Musictracks/ 
4. Run sudo apt-get install libmysqlclient-dev python-dev
5. Run pip install -r requirements/requirements.txt
6. Run mysql -u root -p
	i) enter password : root
	ii) create database musictrack;
7. Run python manage.py makemigrations
8. Run python manage.py migrate
9. Run python manage.py loaddata Musictracks/fixtures/trackdata.json
10. Run python manage.py runserver
11. In the Browser's address bar, type "localhost:8000/tracks"

12. To modify or add data through Django admin , We need to create a SuperUser as:
	a) Run python manage.py createsuperuser
	b) follow instructions
	c) In the Browser window, type "localhost:8000\admin"
	d) login with the username and password you created.


