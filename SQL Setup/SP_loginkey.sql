CREATE DEFINER=`root`@`localhost` PROCEDURE `loginkey`(
    IN p_ID INT, 
    IN p_FirstName VARCHAR(20),
    IN p_LastName VARCHAR(20),
    IN p_Email VARCHAR(40),
    IN p_Pass VARCHAR(20)
)
BEGIN
    INSERT INTO spacepotatoesdb.loginkey (
        ID,
        FirstName,
        LastName,
		Email,
        Pass,
        CreateDate
    )
    VALUES (
        p_ID,
        p_FirstName,
        p_LastName,
		p_Email,
        p_Pass,
        NOW()
    );
END