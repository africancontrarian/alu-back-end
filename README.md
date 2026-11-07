# Python - API

Scripts that gather data from the [JSONPlaceholder](https://jsonplaceholder.typicode.com) REST API.

## Requirements

- Ubuntu 14.04 LTS, `python3` (3.4.3)
- The `requests` module
- Code follows the `PEP 8` style (`pycodestyle`)
- All files are executable and start with `#!/usr/bin/python3`

## Tasks

### 0. Gather data from an API

`0-gather_data_from_an_API.py` takes an employee ID as its only argument
and prints that employee's TODO list progress.

```
$ ./0-gather_data_from_an_API.py 2
Employee Ervin Howell is done with tasks(8/20):
	 distinctio vitae autem nihil ut molestias quo
	 voluptas quo tenetur perspiciatis explicabo natus
	 ...
```

The first line shows the employee name, the number of completed tasks and
the total number of tasks. Each following line shows the title of one
completed task, indented with one tab and one space.