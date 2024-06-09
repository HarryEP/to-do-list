# Basic To Do List

This is a basic to do list app that incorporates flask, postgresql, html and various other sources.

## First Set-Up

Run `pip3 install -r "requirements.txt"`

In a postgresql database, run `psql postgres -f schema.sql` to set up the database whenever you need. This will also refresh the database.

To connect to said database, create an `.env` file with:

- DB_USER=######
- DB_NAME=######
- DB_HOST=######
- DB_PASS=######

for the username, database name, host and password respectfully.

## Running The Application

To run the application, use `python3 app.py`.

Then go to `http://127.0.0.1:5000/` to see the index screen.

If you need to stop and reset the database, use the command (`psql postgres -f schema.sql`) to set up the database.

The application should be very easy to use where you implement any tasks you need manually and will keep them until you remove them from the database (clicking task complete will do this).

## Extra Notes

The program is currently only designed to have tasks that are currently needed on the to do list and will be removed when said task is complete.

## Future Updates

Possible updates include:

- Colour changing to the user's desire
- Showing a completed task database
- Different users
- Access online
- Other suggestions (feel free to message me with suggestions if you have any)
