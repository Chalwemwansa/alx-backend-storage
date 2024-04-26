-- script creates an index on the first letter of a name in the database
CREATE INDEX idx_name_first ON names(name(1));
