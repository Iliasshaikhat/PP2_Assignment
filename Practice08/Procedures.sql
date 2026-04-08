CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR(100), p_phone VARCHAR(20))
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name) THEN
        UPDATE phonebook 
        SET phone = p_phone 
        WHERE name = p_name;
        RAISE NOTICE 'Contact "%" updated', p_name;
    ELSE
        INSERT INTO phonebook (name, phone) 
        VALUES (p_name, p_phone);
        RAISE NOTICE 'Contact "%" added', p_name;
    END IF;
END;
$$;



CREATE OR REPLACE PROCEDURE insert_many_contacts(
        p_names TEXT[], 
        p_phones TEXT[]
    )
    LANGUAGE plpgsql AS $$
    DECLARE
        i INTEGER;
    BEGIN
        FOR i IN 1..array_length(p_names, 1) LOOP
            IF p_phones[i] ~ '^\\+[0-9]+$' THEN
                CALL upsert_contact(p_names[i], p_phones[i]);
            END IF;
        END LOOP;
    END;
    $$;


CREATE OR REPLACE PROCEDURE delete_contact_by_identifier(p_identifier TEXT)
LANGUAGE plpgsql AS $$
DECLARE
    deleted_count INTEGER;
BEGIN
    DELETE FROM phonebook 
    WHERE name = p_identifier 
       OR phone = p_identifier;

    GET DIAGNOSTICS deleted_count = ROW_COUNT;

    RAISE NOTICE 'Deleted % contact(s)', deleted_count;
END;
$$;