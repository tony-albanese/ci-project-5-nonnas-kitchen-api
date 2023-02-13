### Deploying to Heroku

#### Create PostGres database
The first step is to create a new instance of a PostgreSQL database on ElephantSQL
+ Navigate to ![ElephantSQL](https://www.elephantsql.com/)
+ Login or create an account
+ Go to the Dashboard
+ Click "Create New Instance"
+ Name the database
+ Select Tiny Turtle plan and region
+ Click **Review** button
+ Clicke **Create Instance** button
+ Copy the database URL


#### Create App in Heroku
+ Navigate to ![Heroku]()
+ Login or create an account
+ Click on **Create new app**
+ Give the app a name
+ Click on **Create app**
+ Open Settings Tab
+ Add Config Var for DATABASE_URL and paste the url pointing to the newly created Postgres database from ElephantSQL
