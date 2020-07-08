# Write your code here
from datetime import datetime, timedelta

from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

TODAY = f"Today {datetime.today().strftime('%d %b')}:"
MAIN_MENU = '''
1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit
'''

Base = declarative_base()


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today())

    def __repr__(self) -> str:
        return f"Task(task: {self.task}, deadline: {self.deadline})"

    def __str__(self):
        return f"{self.task}. {self.deadline.strftime('%d %b')}"


engine = create_engine('sqlite:///todo.db?check_same_thread=False')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def add_task(task: str, deadline=datetime.today()):
    new_task = Task(task=task, deadline=deadline)
    session.add(new_task)
    session.commit()


def get_tasks(offset=None):
    query = session.query(Task).order_by(Task.deadline)
    if offset is not None:
        last_day = datetime.today().date() + timedelta(offset)
        query = query.filter(Task.deadline == last_day)
    return query.all()


def get_missed_tasks():
    return session.query(Task) \
        .filter(Task.deadline < datetime.today().date()) \
        .order_by(Task.deadline).all()


def delete_task(task: Task):
    session.query(Task).filter(Task.id == task.id).delete()
    session.commit()


def print_day(date):
    print(date.strftime('%A %d %b'))


def print_list(tasks):
    if len(tasks) == 0:
        print("Nothing to do!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()


def print_missed(tasks):
    if len(tasks) == 0:
        print("Nothing is missed!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()


while True:
    main_choice = input(MAIN_MENU)
    print()
    if main_choice == '0':
        print("Bye!")
        break
    elif main_choice == '1':
        print(TODAY)
        print_list(get_tasks(0))
    elif main_choice == '2':
        for i in range(0, 7):
            print_day(datetime.today() + timedelta(i))
            print_list(get_tasks(i))
    elif main_choice == '3':
        print("All tasks:")
        print_list(get_tasks())
    elif main_choice == '4':
        print("Missed tasks:")
        print_missed(get_missed_tasks())
    elif main_choice == '5':
        task = input("Enter task\n")
        task_date = datetime.strptime(input("Enter deadline\n"), '%Y-%m-%d')
        add_task(task, task_date)
        print("The task has been added!")
    elif main_choice == '6':
        print("Chose the number of the task you want to delete:")
        tasks = get_tasks()
        print_list(tasks)
        idx = int(input().strip()) - 1
        delete_task(tasks[idx])
        print("The task has been deleted!")
