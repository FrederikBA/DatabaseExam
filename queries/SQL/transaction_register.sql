BEGIN TRANSACTION;
BEGIN TRY
    DECLARE @member_id VARCHAR(255);
    DECLARE @username VARCHAR(255);
    
    SELECT @member_id = 'testMemberId';
    SELECT @username = 'userTest';
    
    IF NOT EXISTS (SELECT 1 FROM user_login WHERE username = @username)
    BEGIN
        INSERT INTO member (member_id, first_name, last_name, join_date)
        VALUES (@member_id, 'Fiske', 'Laksen', GETDATE());
        
        INSERT INTO user_login (member_id, username, password)
        VALUES (@member_id, @username, '123');
        
        COMMIT;
    END
    ELSE
    BEGIN
        RAISERROR('Username already exists.', 16, 1);
        ROLLBACK TRANSACTION;
    END
END TRY
BEGIN CATCH
    ROLLBACK TRANSACTION;
END CATCH;
