BEGIN TRANSACTION;
BEGIN TRY
DECLARE @member_id VARCHAR(255);

SELECT @member_id = 'testMemberId';

INSERT INTO member (member_id, first_name, last_name, join_date)
VALUES (@member_id, 'Fiske', 'Laksen', GETDATE());

INSERT INTO user_login (member_id, username, password)
VALUES (@member_id, 'userTest', '123');
COMMIT;
END TRY
BEGIN CATCH
ROLLBACK TRANSACTION;
END CATCH;
