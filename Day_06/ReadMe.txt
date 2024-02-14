Day_06 Tasks:

(How we can manage data in django)
Working with Data, Databases & Models.
    . Storing Data in a Presistent way

--------------------------------------------------
What is "Data" and a "DataBase"?
Exploring SQL & MOdels.
Django, Models & Database Quries.
--------------------------------------------------

What is "Data"?

Data :
      . The values we work within our applications such as;
        name,id e-t-c.

      TYPES OF DATA (not official classification)
      I)  Temporary Data  ii) Semi-Persistent Data  
      iii) Persistent Data

      i) Temporary Data:
                        User Input, Selected Blog post e-t-c.
                        .the above is a temporary data becuase
                         it's not important in the future.
                        .That data is used immediately and lost
                         there after.
                        .It's store in Memory (variables)
     ii) Semi-Persistent Data:
                             User Authentication Status.
                             .This Data is stored for a longer
                              time but may be lost 
                              (can be re-created)
                              .
                              . Tore in Browswer, Temporary Files.
     iii) Persistent Data:
                          Blog Posts, Orders, Products e-t-c.
                          .Data is stored forever and must not 
                           be lost.
                           .Store in a Database.


Here we will focused on " Presistent Data ".

--------------------------------------------------
What is DataBase?

DataBase: 
        A database is a structured collection of organized data
        for efficient storage and retrieval.

        TYPES: i) SQL Database   ii) NoSQL Database

        SQL:
            .They Stored Data in tables (Table-based)
            e.g: In a SQL Db Data would be stoed like:

                 col 1    col 1       col 1
                .-----------------------------.
           row1 |  ID  |   NAME     |   AGE   |
           row2 |-----------------------------|
           row3 |  1   |   Nazeem   |   31    |
           row4 |-----------------------------|
           row5 |  2   |   Makaov   |   33    |
                `-----------------------------`
           TYPES
                MySQL, PostgreeSQL, SQLite.
            

        NoSQL:
             .They Stored Data in Documents (Document-based)
              Instead of rows and columns here we have lists

             .---------------------------------. 
             | {id:1, name: "Nazeem", age: 31} |
             | {id:2, name: "Nazeem", age: 35} | 
             `---------------------------------`
             TYPES
                  MongoDB, Cassandra.

These SQL and NoSQL are the philosophies for storing data.
-----------------------
So which one is better?

For many websites it would'nt matter too much it's come out
to personal preferences.
But in some cases choosing between them is must.
like how you want to structure your data.

--------------------------------------------------
Understand SQL



