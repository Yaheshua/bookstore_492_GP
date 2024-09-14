--Create the Bookstore applications database foundation
DROP DATABASE IF EXISTS bookStoreDB;
CREATE DATABASE bookStoreDB;
USE bookStoreDB;

DROP TABLE IF EXISTS Books;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Reviews;


CREATE TABLE Books(
	bookId  INT NOT NULL AUTO_INCREMENT,
	title VARCHAR(30) NOT NULL,
	genre VARCHAR(30),
	author VARCHAR(30),
	published_year VARCHAR(20),
	stock INT UNSIGNED,
	price DOUBLE,
	PRIMARY KEY (bookId),
	UNIQUE (title)
);


CREATE TABLE Users(
	userId INT NOT NULL AUTO_INCREMENT,
	userName VARCHAR(30),
	firstName VARCHAR(30),
	familyName VARCHAR(30),
	email VARCHAR(30),
	bankingCardNumber VARCHAR(19) NOT NULL,
	password VARCHAR(10) NOT NULL,
	PRIMARY KEY (userID),
	UNIQUE (userName)
);


CREATE TABLE Reviews(
	reviewId INT NOT NULL AUTO_INCREMENT,
	reviewText VARCHAR(250),
	PRIMARY KEY (reviewId)
);

