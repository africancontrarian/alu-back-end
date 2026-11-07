# alu-back-end

ALU Back-End projects. This repository currently holds the **API** project.

## API (`api/`)

Python scripts that use the [JSONPlaceholder](https://jsonplaceholder.typicode.com)
REST API to read employee data and export it to different data structures.

### Requirements

- Ubuntu 14.04 LTS, `python3` (3.4.3)
- The `requests` module
- Code follows the `PEP 8` style (`pycodestyle`)
- All files are executable and start with `#!/usr/bin/python3`
- Imports are in alphabetical order, dictionary values are read with `get`,
  and nothing runs on import (`if __name__ == "__main__":`)

### Tasks

| # | File | Description |
|---|------|-------------|
| 0 | `api/0-gather_data_from_an_API.py` | Print an employee's TODO list progress |
| 1 | `api/1-export_to_CSV.py` | Export an employee's tasks to `USER_ID.csv` |
| 2 | `api/2-export_to_JSON.py` | Export an employee's tasks to `USER_ID.json` |
| 3 | `api/3-dictionary_of_list_of_dictionaries.py` | Export every employee's tasks to `todo_all_employees.json` |

#### 0. Gather data from an API

```
$ ./api/0-gather_data_from_an_API.py 2
Employee Ervin Howell is done with tasks(8/20):
	 distinctio vitae autem nihil ut molestias quo
	 voluptas quo tenetur perspiciatis explicabo natus
	 ...
```

The first line shows the employee name, the number of completed tasks and
the total number of tasks. Each following line shows the title of a
completed task, indented with one tab and one space.

#### 1. Export to CSV

```
$ ./api/1-export_to_CSV.py 2
$ cat 2.csv
"2","Antonette","False","suscipit repellat esse quibusdam voluptatem incidunt"
"2","Antonette","True","distinctio vitae autem nihil ut molestias quo"
...
```

Format: `"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"`

#### 2. Export to JSON

```
$ ./api/2-export_to_JSON.py 2
$ cat 2.json
{"2": [{"task": "suscipit repellat esse quibusdam voluptatem incidunt", "completed": false, "username": "Antonette"}, ...]}
```

Format: `{"USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ...]}`

#### 3. Dictionary of list of dictionaries

```
$ ./api/3-dictionary_of_list_of_dictionaries.py
$ cat todo_all_employees.json
{"1": [{"username": "Bret", "task": "delectus aut autem", "completed": false}, ...], "2": [...], ...}
```

Format: `{"USER_ID": [{"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ...], ...}`
