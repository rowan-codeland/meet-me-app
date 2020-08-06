# Meet Me App
http://rowans-meet-me-app.herokuapp.com/
CRUD Project using MongoDb & Deployed to Heroku
This application is a simple meeting application, users can create, view, edit and delete meetings. Each meeting has a field for the meeting name, description, time & date, and duration.

## UX

This application is built to clearly show and sort meetings based on the closest meeting date at the top and asscending downwards. I decided to seperate out the date object on the front end and display the day, month and day of the week so users can visually sort through the dates with minimal hassle.


## Features
There are 3 core database features (Create, Update, Delete) While creating and updating a meeting a user also uses text input fields, a custom date/time picker and a generic html timepicker for meeting duration. There is also front end form validation
 
### Existing Features
- Custom date and time picker is created with thanks to Tempus Dominus. It allows the user to pick both a date and time and that to be stored in a timestamp format within MongoDB.
- The HTML5 timepicker used for duration saves data as a string to MongoDB
- Input fields are using frontend data validation. This comes off the shelf from Bootstrap 4 forms and breathes interactivity into the form meaning the user will never be lost looking for a missing/ incorrect input.

### Features Left to Implement
- Given more time I would add the following features;
- - Datbase form validation
- - Moduls for confirming deletion of an entry
- - 15 minute time stepping on the duration of a meeting
- - Cap on the meeting duration
- - User login and meetings linked to each user.


## Technologies Used

This webapp uses the following technologies;

- Python
- Javascript
- MongoDB
- Bootstrap 4
- HTML5
- CSS3
- Tempus Dominus

## Testing

1. Create a meeting
    1. Select add meeting button
    2. Fill in form
    3. Click add meeting
    4. Check if meeting is on homepage

2. Delete a meeting
    1. Select trash icon beneath meeting
    2. Check if meeting has been deleted

3. Update a meeting
    1. Select pencil icon beneath meeting
    2. Change fields on edit meeting form
    3. Submit form
    4. Check if meeting has been updated on homepage

4. Form validation
    1. Fill out form leaving one entry blank
    2. Check that form validation is red on that entry and green on remainders
    3. Repeat for all form fields
    4. Submit form with all fields correct format and filled in.


## Deployment

This webapp is hosted using Heroku, deployed directly from the master branch. Every time a new commit is pushed to Heroku the deployed webapp will update.

If you want to run this on your own machine or within your own IDE, type git clone https://github.com/rowan-codeland/meet-me-app.git into your terminal. Please then type "git remote rm origin" to sever ties with the original.

## Credits

### Depmus Dominus
- https://tempusdominus.github.io/bootstrap-4/

