# travelplan-basic-py3

A basic [Travel](https://github.com/travel-tools/travel) plan to create Python 3 bags.

Travel plans use [Cookiecutter](https://github.com/cookiecutter/cookiecutter) under the hood. Please, refer to their documentation.

## Usage plan

Let us imagine that we want to create a Python package that looks like this:

```
example/
  commons/
  microservices/
    a/
    b/
travel.yml
```

Then, we would write the following `travel.yml` :

```yaml
commons:
  plan: <plan_repo_URL or plan_folder_abspath>
  config:
    ...

microservices:
  a:
    plan: <plan_repo_URL or plan_folder_abspath>
    config:
      ...

  b:
    plan: <plan_repo_URL or plan_folder_abspath>
    config:
      ...
```

The `config` directive of this Travel plan accepts the following properties:
- `name`, the name of the Py 3 package root folder
- `package`, a map which accepts the following properties:
  - `author`, the name of the package author
  - `author_email`, the email of the package author
  - `description`, a short description of the package
  - `name`, the name of the Py 3 package

If the Py 3 package name is not provided, it is inferred from the root folder (`' '` and `'-'` turn into `'_'`).

Finally, we would run the following commands from the CLI:
```bash
cd <travel.yml_folder_abspath>
travel plan example
```

That's it! Now we would have our three Travel bags: `commons`, `a` and `b`.
