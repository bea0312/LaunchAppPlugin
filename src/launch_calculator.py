from PyPlugin import Action
import subprocess

class LaunchCalculator(Action):
    def on_key_down(self, payload):
        try:
            subprocess.Popen(["gnome-calculator"])
        except Exception as e:
            print(f"Error launching calculator: {e}")

    def get_properties(self):
        return {
            "title": "Launch Calculator",
            "description": "Opens the GNOME calculator when triggered.",
            "icon": "icon.png"
        }