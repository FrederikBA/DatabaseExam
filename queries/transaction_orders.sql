BEGIN TRANSACTION;

BEGIN TRY
    INSERT INTO loan (loan_id, movie_id, loan_date, return_date)
    VALUES (1, 'tt0029583', GETDATE(), NULL);
    
    INSERT INTO orders (order_id, loan_id, member_id, total_price)
    VALUES (1, 1, '273d5fbc-9bea-4ce1-b34e-ca11cc9cb85c', 100.0);
    
    COMMIT TRANSACTION;
END TRY
BEGIN CATCH
    ROLLBACK TRANSACTION;
END CATCH;
