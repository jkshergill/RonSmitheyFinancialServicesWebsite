CREATE DEFINER=`root`@`localhost` PROCEDURE `bookappointment`(
    IN p_Username VARCHAR(45),
    IN p_Email VARCHAR(45),
	IN p_Phone INT, 
    IN p_Date DateTime,
    IN p_Reason VARCHAR(45)
)
BEGIN
    INSERT INTO spacepotatoesdb.bookappointment (
        Username, 
        Email, 
        Phone,
        Date, 
        Reason
    )
    VALUES (
        p_Username,
        p_Email,
        p_Phone,
        NOW(),
        p_Reason
    );
END