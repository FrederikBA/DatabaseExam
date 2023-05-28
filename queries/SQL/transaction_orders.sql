BEGIN TRANSACTION;
BEGIN TRY
DECLARE @order_id VARCHAR(255);

INSERT INTO orders(order_id, member_id, total_price) 
VALUES ('12345', '5682ffa8-172d-4b57-9c50-f2a39aa36243', 100.00);

SET @order_id = '12345';

INSERT INTO loan(loan_id, order_id, movie_id, loan_date, return_date)
VALUES ('loan123', @order_id, 'tt0029583', GETDATE(), GETDATE());

COMMIT TRANSACTION;
END TRY
BEGIN CATCH
ROLLBACK TRANSACTION;
END CATCH;
