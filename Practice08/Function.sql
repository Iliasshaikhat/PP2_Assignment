CREATE OR REPLACE FUNCTION get_contacts_by_pattern(p_pattern TEXT)
RETURNS TABLE (id INTEGER, name VARCHAR(100), phone VARCHAR(20)) AS $$
BEGIN
    RETURN QUERY 
    SELECT c.id, c.name, c.phone 
    FROM phonebook c
    WHERE c.name ILIKE '%' || p_pattern || '%'
       OR c.phone ILIKE '%' || p_pattern || '%';
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_contacts_paginated(
    p_limit INTEGER DEFAULT 5, 
    p_offset INTEGER DEFAULT 0
)
RETURNS TABLE (id INTEGER, name VARCHAR(100), phone VARCHAR(20)) AS $$
BEGIN
    RETURN QUERY 
    SELECT c.id, c.name, c.phone 
    FROM phonebook c
    ORDER BY c.name
    LIMIT p_limit 
    OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;