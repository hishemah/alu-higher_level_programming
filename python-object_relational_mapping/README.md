# Python - Object-relational mapping

Connecting Python to MySQL, first with the `MySQLdb` module (raw SQL, including the difference between a query built with `format` and a safe parameterized query), then with the SQLAlchemy ORM (models, sessions, queries, inserts, updates, deletes and relationships).

Every script takes the MySQL username, password and database name as arguments and connects to `localhost:3306`.

| File | Description |
| ---- | ----------- |
| `0-select_states.py` | Lists all states (MySQLdb) |
| `1-filter_states.py` | Lists the states whose name starts with `N` |
| `2-my_filter_states.py` | Lists the states matching an argument (query built with `format`) |
| `3-my_safe_filter_states.py` | Same, safe from SQL injection |
| `4-cities_by_state.py` | Lists all cities with their state |
| `5-filter_cities.py` | Lists the cities of a state, on one line |
| `model_state.py` | SQLAlchemy `Base` and `State` model (table `states`) |
| `6-model_state.py` | Creates the `states` table from the model |
| `7-model_state_fetch_all.py` | Lists all `State` objects |
| `8-model_state_fetch_first.py` | Prints the first `State` object, or `Nothing` |
| `9-model_state_filter_a.py` | Lists the `State` objects containing the letter `a` |
| `10-model_state_my_get.py` | Prints the id of the state given as argument, or `Not found` |
| `11-model_state_insert.py` | Adds the state `Louisiana` |
| `12-model_state_update_id_2.py` | Renames the state with id 2 to `New Mexico` |
| `13-model_state_delete_a.py` | Deletes the states containing the letter `a` |
| `model_city.py` | `City` model (table `cities`) |
| `14-model_city_fetch_by_state.py` | Lists all cities as `<state>: (<id>) <city>` |
| `relationship_state.py`, `relationship_city.py` | `State` and `City` models with a relationship |
| `100-relationship_states_cities.py` | Creates California with the city San Francisco |
| `101-relationship_states_cities_list.py` | Lists all states with their cities |
| `102-relationship_cities_states_list.py` | Lists all cities with their state |
