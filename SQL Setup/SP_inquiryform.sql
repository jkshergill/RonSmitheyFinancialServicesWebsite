CREATE DEFINER=`root`@`localhost` PROCEDURE `inquiryform`(
	IN p_Topic VARCHAR(150), 
    IN p_Inquiry VARCHAR(100)

)
BEGIN
    INSERT INTO spacepotatoesdb.inquiryform (
        Topic,
        Inquiry, 
        CreateDate,
        Status
    )
    VALUES (
        p_Topic,
        p_Inquiry,
        NOW(),
        0
    );
END