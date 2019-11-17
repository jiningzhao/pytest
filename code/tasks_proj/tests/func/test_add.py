"""
Placeholder test file.

We'll add a bunch of tests here in later versions.
"""
import pytest
import tasks
from tasks import Task

def test_add_returns_valid_id():
    """Placeholder test."""
    new_task = Task
    task_id = tasks.add(new_task)
    assert isinstance(task_id,int)

@pytest.mark.smoke
def test_add_task_has_id_set():

    new_task = Task('sit in chair',owner='me',done=True)
    task_id = tasks.add(new_task)

    task_from_db = tasks.get(task_id)

    assert task_from_db.id == task_id

@pytest.fixture(autouse=True)
def initialied_tasks_db(tmpdir):

    tasks.start_tasks_db(str(tmpdir),'tiny')

    yield # this is where the testing happens

    tasks.stop_tasks_db()