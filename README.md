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

If you need to stop and reset the database, use the command to set up the database.

## Extra Notes

The program is currently only designed to have tasks that are currently needed on the to do list and will be removed (deleted) when complete.
