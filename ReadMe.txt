FEATURES OF THE WEB APP:

Users can :

	1. View a list all music track details. 
	2. Add music track with details like Title, Genres, Rating.
	3. Add genre with its name. 
	5. Edit specific track title, genre and rating.
	5. Can search track based on track or genres name.
	
 

################  Installation ##############

1. Make a Virtual Environment.
2. Clone the repository with git clone https://github.com/Amanbg/Music-Web-App.git

3. Run pip install -r requirements.txt
4. Go to the directory Music-Web-App/Musictracks/ 
		a) Run python manage.py makemigrations
		b) Run python manage.py migrate
		c) Run mysql -u root -p
			i) enter password : root
			ii) create database musictrack;
		d) Run python manage.py loaddata Musictracks/fixtures/trackdata.json
		e) Run python manage.py runserver
		f) In the Browser's address bar, type "localhost:8000/tracks"


5. To modify or add data through Django admin , We need to create a SuperUser as:
	a) Run python manage.py createsuperuser
	b) follow instructions
	c) In the Browser window, type "localhost:8000\admin"
	d) login with the username and password you created.


