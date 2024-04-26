-- script creates a trigger that decreases the quantity of an item whenever a new order is added
CREATE TRIGGER dec_item AFTER INSERT ON orders
	FOR EACH ROW
		UPDATE items SET quantity = quantity - NEW.number
			WHERE name LIKE NEW.item_name;
