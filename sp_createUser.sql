USE BucketList;
DROP TABLE IF EXISTS tbl_user;

CREATE TABLE tbl_user (
  user_id BIGINT UNIQUE AUTO_INCREMENT,
  user_name VARCHAR(45) DEFAULT NULL,
  user_username VARCHAR(45) DEFAULT NULL,
  user_password VARCHAR(255) DEFAULT NULL,
  PRIMARY KEY (user_id));

DROP PROCEDURE IF EXISTS sp_createUser;

DELIMITER $$
CREATE DEFINER='root'@'localhost' PROCEDURE sp_createUser(
    IN p_name VARCHAR(20),
    IN p_username VARCHAR(20),
    IN p_password VARCHAR(255)
)
BEGIN
    if ( select exists (select 1 from tbl_user where user_username = p_username) ) THEN

        select 'Username Exists !!';

    ELSE

        insert into tbl_user (
            user_name,
            user_username,
            user_password
        )
        values
        (
            p_name,
            p_username,
            p_password
        );

    END IF;
END$$
DELIMITER ;
