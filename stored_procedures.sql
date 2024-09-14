-- the stored procedures for manipulating the database MySQL 
DELIMITER //

DROP PROCEDURE IF EXISTS add_new_user//	

CREATE PROCEDURE add_new_user(
	IN uname VARCHAR(30),
	IN sname VARCHAR(30),
	IN bname VARCHAR(30),
	IN addr VARCHAR(50),
	IN bkg_card_nr VARCHAR(19),
	IN pass VARCHAR(10) )

BEGIN
	INSERT INTO Users(userName, firstName, familyName, email, bankingCardNumber, password) 
		VALUES (uname, sname, bname, addr, bkg_card_nr, pass) ;
END//

DELIMITER ;

DELIMITER $$

DROP PROCEDURE IF EXISTS log_in$$

CREATE PROCEDURE log_in(
	IN uName VARCHAR(30),
	OUT fName VARCHAR(30),
	OUT sName VARCHAR(30),
	OUT emal VARCHAR(30),
	OUT pass VARCHAR(30)
	)

BEGIN

	SELECT firstName, familyName, email, password 
		INTO fName, sName, emal, pass 
		FROM Users 
		WHERE userName = uName;
END$$



DROP PROCEDURE IF EXISTS getAllBooks$$

CREATE PROCEDURE getAllBooks()

BEGIN

	SELECT title, author, genre, price, stock  FROM Books;
END$$



DROP PROCEDURE IF EXISTS isBook$$

CREATE PROCEDURE isBook(IN bName VARCHAR(30), OUT bExist INT)

BEGIN
	SELECT count(*) INTO bExist 
		FROM Books
		WHERE title = bName;

END$$



DROP PROCEDURE IF EXISTS insertBook$$

CREATE PROCEDURE insertBook(
	IN bName VARCHAR(30),
	IN bGenre VARCHAR(30),
	IN bAuthor VARCHAR(30),
	IN bYear VARCHAR(20),
	IN bSock INT,
	IN bPrice DOUBLE
)

BEGIN
	INSERT INTO Books(title, genre, author, published_year, stock, price)
		VALUES (bName, bGenre, bAuthor, bYear, bSock, bPrice);
END$$



DROP FUNCTION IF EXISTS bookScore$$

CREATE FUNCTION bookScore(idBook INT) 
	RETURNS DOUBLE
BEGIN
	DECLARE sumScore INT;
	DECLARE nrReviews INT;
	DECLARE bookGrade DOUBLE DEFAULT 0.0;

	SELECT COUNT(*) INTO nrReviews 
		FROM ReviewedBooks
		WHERE bookId = idBook;

	SELECT IFNULL(SUM(score), 0) INTO sumScore
		FROM ReviewedBooks
		WHERE bookId = idBook;


	IF nrReviews = 0 
	THEN
		SET bookGrade = 0;
	ELSE
		SET bookGrade = sumScore / nrReviews;

	END IF;

	RETURN bookGrade;

END$$



DROP PROCEDURE IF EXISTS getBooksUser$$

CREATE PROCEDURE getBooksUser()

BEGIN

	SELECT title, author, genre,  price, stock, bookScore(bookId) FROM Books;
END$$




DROP PROCEDURE IF EXISTS getUsersBooks$$

CREATE PROCEDURE getUsersBooks(IN uName VARCHAR(30))

BEGIN
	DECLARE idUser INT;
	SELECT userId INTO idUser FROM Users WHERE userName=uName;

	SELECT b.title, b.author, b.genre, bb.quantity, bookScore(b.bookId)
		FROM Books b, BuyedBooks bb
		WHERE b.bookId = bb.bookId
			AND bb.userId = idUser ;
END$$
