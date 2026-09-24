import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.label import Label


class SimpleAudioUI(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Main layout direction
        self.orientation = "vertical"
        self.padding = 20
        self.spacing = 10

        # 1. Header Label
        self.header = Label(
            text="[b]Audio Processing App[/b]",
            markup=True,
            font_size="20sp",
            size_hint_y=0.1,
        )
        self.add_widget(self.header)

        # 2. File Chooser
        self.file_chooser = FileChooserListView(
            filters=["*.wav"], size_hint_y=0.6
        )
        self.add_widget(self.file_chooser)

        # 3. Status Display Label
        self.status_label = Label(
            text="Select a .wav file to begin",
            font_size="14sp",
            size_hint_y=0.1,
            color=(0.8, 0.8, 0.8, 1),
        )
        self.add_widget(self.status_label)

        # 4. Action Button
        self.process_btn = Button(
            text="Process Selected File",
            size_hint_y=0.15,
            background_color=(0.2, 0.6, 1, 1),
        )
        # Bind button press to event handler
        self.process_btn.bind(on_press=self.on_process_click)
        self.add_widget(self.process_btn)

    def on_process_click(self, instance):
        selected = self.file_chooser.selection
        if selected:
            file_path = selected[0]
            file_name = os.path.basename(file_path)
            self.status_label.text = f"Selected: {file_name}"
            # Insert your backend execution logic or threading here
        else:
            self.status_label.text = "Error: No file selected!"


class MainApp(App):

    def build(self):
        self.title = "Alchemy Audio Engine"
        return SimpleAudioUI()


if __name__ == "__main__":
    MainApp().run()
