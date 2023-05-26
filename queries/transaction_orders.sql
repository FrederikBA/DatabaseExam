BEGIN TRANSACTION;

DECLARE @order_id VARCHAR(255);
DECLARE @loan_id VARCHAR(255);

INSERT INTO orders (order_id, member_id, total_price)
VALUES ('12345', '79b727f3-dfe5-423c-acd3-f8a84135d392', 100.00);

SELECT @order_id = '12345';

INSERT INTO loan (loan_id, order_id, movie_id, loan_date, return_date)
VALUES ('loan123', @order_id, 'tt0029583', GETDATE(), NULL);

SELECT @loan_id = 'loan123';

IF @@ROWCOUNT = 1
BEGIN
    COMMIT;
END
ELSE
BEGIN
    ROLLBACK;
END;
