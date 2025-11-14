from flet import (
    Page,
    TextField,
    Column,
    Row,
    CrossAxisAlignment,
    MainAxisAlignment,
    FloatingActionButton,
    Icons,
    IconButton,
    Checkbox,
    Colors,
    app,
)
from flet.core.control_event import ControlEvent
from typing import Callable


class Task(Column):
    def __init__(self, task_name: str, task_delete: Callable):
        super().__init__()
        self.task_name: str = task_name
        self.task_delete: Callable = task_delete

        self.display_task: Checkbox = Checkbox(value=False, label=task_name)
        self.edit_name: TextField = TextField(expand=1)

        self.display_view = Row(
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=CrossAxisAlignment.CENTER,
            controls=[
                self.display_task,
                Row(
                    spacing=0,
                    controls=[
                        IconButton(
                            icon=Icons.CREATE_OUTLINED,
                            tooltip="Edit To-Do",
                            on_click=self.edit_clicked,
                        ),
                        IconButton(
                            Icons.DELETE_OUTLINE,
                            tooltip="Delete To-Do",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
        )

        self.edit_view = Row(
            visible=False,
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                IconButton(
                    icon=Icons.DONE_OUTLINE_OUTLINED,
                    icon_color=Colors.GREEN,
                    tooltip="Update To-Do",
                    on_click=self.save_clicked,
                ),
            ],
        )
        self.controls = [self.display_view, self.edit_view]

    def edit_clicked(self, e: ControlEvent):
        self.edit_name.value = str(self.display_task.label)
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e: ControlEvent):
        self.display_task.label = self.edit_name.label
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def delete_clicked(self, e: ControlEvent):
        self.task_delete(self)


class TodoApp(Column):
    def __init__(self):
        super().__init__()
        self.new_task = TextField(
            hint_text="What needs to be done?", expand=True, on_submit=self.add_clicked
        )
        self.tasks = Column()
        self.width = 600

        self.controls = [
            Row(
                controls=[
                    self.new_task,
                    FloatingActionButton(icon=Icons.ADD, on_click=self.add_clicked),
                ],
            ),
            self.tasks,
        ]

    def add_clicked(self, e: ControlEvent):
        if not self.new_task.value:
            return None

        task: Task = Task(self.new_task.value, self.task_delete)
        self.tasks.controls.append(task)
        self.new_task.value = None
        self.update()

    def task_delete(self, task: Task):
        self.tasks.controls.remove(task)
        self.update()


def main(page: Page):
    page.title = "To-Do App"
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.update()

    todo = TodoApp()
    page.add(todo)


app(main)
