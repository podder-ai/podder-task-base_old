all: isort yapf flake8 mypy pytest

isort:
	isort -y -rc podder_task_base

yapf:
	yapf -i -r --exclude 'podder_task_base/task_initializer/templates/**/*.py' podder_task_base

flake8:
	flake8 podder_task_base

mypy:
	mypy podder_task_base

test:
	PYTHONPATH=. pytest
