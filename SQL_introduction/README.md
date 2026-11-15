# SQL - Introduction

First steps with MySQL 8.0: creating and dropping databases and tables, and inserting, selecting, updating and deleting rows, with a few aggregate functions.

| File | Description |
| ---- | ----------- |
| `0-list_databases.sql` | Lists all databases of the MySQL server |
| `1-create_database_if_missing.sql` | Creates the database `hbtn_0c_0` if it is missing |
| `2-remove_database.sql` | Deletes the database `hbtn_0c_0` if it exists |
| `3-list_tables.sql` | Lists all tables of a database |
| `4-first_table.sql` | Creates the table `first_table` (`id INT`, `name VARCHAR(256)`) |
| `5-full_table.sql` | Prints the full description of `first_table` without `DESCRIBE` or `EXPLAIN` |
| `6-list_values.sql` | Lists all rows of `first_table` |
| `7-insert_value.sql` | Inserts the row `89, Best School` into `first_table` |
| `8-count_89.sql` | Counts the records with `id = 89` in `first_table` |
| `9-full_creation.sql` | Creates `second_table` and adds four records |
| `10-top_score.sql` | Lists all records of `second_table` by score, best first |
| `11-best_score.sql` | Lists the records with a score of at least 10 |
| `12-no_cheating.sql` | Sets Bob's score to 10, using his name only |
| `13-change_class.sql` | Removes all records with a score of 5 or less |
| `14-average.sql` | Computes the average score as `average` |
| `15-groups.sql` | Lists the number of records per score, most common first |
| `16-no_link.sql` | Lists the records that have a name, by score, best first |
