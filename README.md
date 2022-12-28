# This Just In
A news headline game where players try not to smile

## Rules
1. Separate your group into two teams.
2. Each team will send a representative, known as a "news anchor", to the front of the room.
3. Select "Start Game".
4. In their best TV news voice, the news anchors will alternate reading news headlines.
5. If a news anchor smiles, he/she must sit down and be replaced by the next team member.
6. A news anchor will continue reading headlines until he/she breaks a smile.
7. The team that can read the most headlines with a straight face wins.

## Local Setup (Django)
These instructions assume that you have python3 running on your OS.
1. git clone https://github.com/crunchmasterdeluxe/this_just_in.git
2. This will create a folder in your current directory called `this_just_in`. `cd` (mac)/`dir` (windows) into that folder. (e.g. `cd this_just_in`)
3. Next, install Django. Run `pip3 install Django`. This will give you the basic Django framework and its libraries.
4. To run on your local server, run `python3 manage.py runserver`.
5. If you make any changes to models.py, you must update the database to reflect those changes. You can do so by running `python3 manage.py makemigrations` and then `python3 manage.py migrate`
