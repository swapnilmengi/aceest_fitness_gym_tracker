import pytest
import ACEest_Fitness
import tkinter as tk

def test_app_creation():
    root = tk.Tk()
    app = ACEest_Fitness.FitnessTrackerApp(root)
    assert app.workouts == []
    root.destroy()

