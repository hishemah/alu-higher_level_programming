# SQL - More queries

MySQL users and privileges, table constraints (`NOT NULL`, `DEFAULT`, `UNIQUE`, `PRIMARY KEY`, `FOREIGN KEY`), subqueries and `JOIN`s.

| File | Description |
| ---- | ----------- |
| `0-privileges.sql` | Lists all privileges of the users `user_0d_1` and `user_0d_2` |
| `1-create_user.sql` | Creates `user_0d_1` with all privileges on the server |
| `2-create_read_user.sql` | Creates the database `hbtn_0d_2` and `user_0d_2`, with only `SELECT` on it |
| `3-force_name.sql` | Creates the table `force_name`, whose `name` can't be null |
| `4-never_empty.sql` | Creates the table `id_not_null`, whose `id` defaults to 1 |
| `5-unique_id.sql` | Creates the table `unique_id`, whose `id` defaults to 1 and is unique |
| `6-states.sql` | Creates the database `hbtn_0d_usa` and its table `states` |
| `7-cities.sql` | Creates the table `cities`, with a foreign key to `states` |
| `8-cities_of_california_subquery.sql` | Lists the cities of California with a subquery (no `JOIN`) |
| `9-cities_by_state_join.sql` | Lists all cities with their state name |
| `10-genre_id_by_show.sql` | Lists the shows that have a genre, with each genre id |
| `11-genre_id_all_shows.sql` | Lists all shows with each genre id, or `NULL` |
| `12-no_genre.sql` | Lists the shows without any genre |
| `13-count_shows_by_genre.sql` | Lists each genre with its number of shows |
| `14-my_genres.sql` | Lists all genres of the show Dexter |
| `15-comedy_only.sql` | Lists all Comedy shows |
| `16-shows_by_genre.sql` | Lists all shows with all their genres, or `NULL` |
