 -- Delete the table if it already exists 
DROP TABLE IF EXISTS Ideas;

 -- Create the schema 
CREATE TABLE Ideas(
					idea_ID int not null primary key auto_increment,
					name varchar(50) not null,
					description  varchar(10000) not null,
					category varchar(50) not null
				  );



