
# Debate Wesbite

A brief description of what this project does and who it's for


## Documentation

[Documentation](https://linktodocumentation)

  This a a django-based website for running debate between 2 people. Users can view the debate and also provide their comments in the comment section.
  Application has ACL based on user roles.
 Application has support Administrator, Moderator, Debater and Guest roles
 Application has only allow registered and logged in users to debate
 Moderators has be responsible for maintaining the debate content, manage an altercation, keeping track of user infractions and banning a volatile user
 Administrators can post a new debate topic, close an old topic, add or delete a user, assign user a particular role, choose the winners of a debate, close a running debate and if required open a closed debate
 Debaters has be able to post their views over a debate, they can challenge another debate over any running debate topic, can choose the debate side (for the motion or against the motion) once per debate topic.
 Debates has be one on one, if the participants changes the same debate topic ost a new debate automatically
 Other debaters can vote up or vote down a debater's point of view
 User profile has be visible to all, and it has carry information regarding, debates participated in, debates won, debates lost, points earned
 A user with good number of points has be chosen as moderator by the site administrator
 Debater can suggest a new debate topic
 Debaters should be searchable
 Debate List should be searchable
## Authors

- [@kingdragon46](https://www.github.com/kingdragon46)

  
## Run Locally

Clone the project

```bash
  git clone https://github.com/kingdragon46/debate-django
```

Go to the project directory

```bash
  cd debate
```

Install dependencies

```bash
  source venv/Scripts/activate

  pip install -r requirements.txt

  python manage.py makemigrations

  python manage.py migrate
  
  python manage.py createsuperuser
```

Start the server

```bash
  python manage.py runserver
```

  