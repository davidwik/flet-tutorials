from flet import (
    OutlinedButton,
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
    Tabs,
    Tab,
    Text,
    TextThemeStyle,
    Control,
)
from flet.core.control_event import ControlEvent
from typing import Callable


class Task(Column, Control):
    def __init__(self, task_name: str, task_change: Callable, task_delete: Callable):
        super().__init__()
        self.completed: bool = False
        self.task_name: str = task_name
        self.task_delete: Callable = task_delete
        self.task_status_change: Callable = task_change

        self.display_task: Checkbox = Checkbox(
            value=False, label=task_name, on_change=self.status_changed
        )
        self.edit_name: TextField = TextField(expand=1, on_submit=self.save_clicked)

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

    def edit_clicked(self, _: ControlEvent):
        self.edit_name.value = str(self.display_task.label)
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, _: ControlEvent):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def delete_clicked(self, _: ControlEvent):
        self.task_delete(self)

    def status_changed(self, e: ControlEvent):
        self.completed = bool(self.display_task.value)
        self.task_status_change(e)


class TodoApp(Column):
    def __init__(self):
        super().__init__()
        self.new_task = TextField(
            hint_text="What needs to be done?", expand=True, on_submit=self.add_clicked
        )

        self.filter = Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[Tab(text="all"), Tab(text="active"), Tab(text="completed")],
        )

        self.items_left = Text("0 active item(s) left")

        self.tasks = Column()
        self.width = 600

        self.controls = [
            Row([Text(value="Todos", theme_style=TextThemeStyle.HEADLINE_MEDIUM)]),
            Row(
                controls=[
                    self.new_task,
                    FloatingActionButton(icon=Icons.ADD, on_click=self.add_clicked),
                ],
            ),
            Column(
                spacing=25,
                controls=[
                    self.filter,
                    self.tasks,
                    Row(
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=CrossAxisAlignment.CENTER,
                        controls=[
                            self.items_left,
                            OutlinedButton(
                                text="Clear completed", on_click=self.clear_clicked
                            ),
                        ],
                    ),
                ],
            ),
        ]

    def before_update(self):
        status = self.filter.tabs[self.filter.selected_index].text
        tasks: list[Task] = self.tasks.controls  # type: ignore
        count = 0
        for task in tasks:
            task.visible = (
                status == "all"
                or (status == "active" and task.completed is False)
                or (status == "completed" and task.completed)
            )
            if not task.completed:
                count += 1

        self.items_left.value = f"{count} active item(s) left."

    def tabs_changed(self, _: ControlEvent):
        self.update()

    def task_status_change(self, _: ControlEvent):
        self.update()

    def clear_clicked(self, _: ControlEvent):
        tasks: list[Task] = self.tasks.controls  # type: ignore
        for task in tasks:
            if task.completed:
                self.task_delete(task)

    def add_clicked(self, _: ControlEvent):
        if not self.new_task.value:
            return None

        task: Task = Task(
            self.new_task.value, self.task_status_change, self.task_delete
        )
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
