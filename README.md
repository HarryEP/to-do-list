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

##### Start

To run the application, use `python3 app.py`.

Then go to `http://127.0.0.1:5000/` to see the index screen.

##### Stop

If you need to stop and reset the database, use the command (`psql postgres -f schema.sql`) to set up the database.

##### While the application is active

The application should be very easy to use where you add any tasks you want to add manually at the bottom, accompianed with the priority selected. Every item in the database will appear and be shown on the to do list. You will also be able to sort the list by several ideas, such as creation date, name, whether it is completed and priority.
On each non-complete item, you can do three things: mark as complete, delete the item from the database or edit the item (name and priority).
If an item is complete, it will be coloured green and only have the delete the item from the database option.

## Extra Notes

The program is currently only designed to have tasks that are currently needed on the to do list and will be removed when said task is complete.

## Future Updates

Possible updates include:

- Colour changing to the user's desire
- Different users
- Access online
- Other suggestions (feel free to message me with suggestions if you have any)
- Shopping list feature
- Clear all
