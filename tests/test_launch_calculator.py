import unittest
from src.launch_calculator import LaunchCalculator
from unittest.mock import patch, MagicMock

class TestLaunchCalculator(unittest.TestCase):
    @patch('subprocess.Popen')
    def test_on_key_down_success(self, mock_popen):
        calculator = LaunchCalculator()
        calculator.on_key_down(None)
        mock_popen.assert_called_once_with(["gnome-calculator"])

    @patch('subprocess.Popen', side_effect=Exception("Error"))
    def test_on_key_down_failure(self, mock_popen):
        calculator = LaunchCalculator()
        with patch('builtins.print') as mock_print:
            calculator.on_key_down(None)
            mock_print.assert_called_once_with("Greška pri pokretanju kalkulatora: Error")

    def test_get_properties(self):
        calculator = LaunchCalculator()
        properties = calculator.get_properties()
        self.assertEqual(properties['title'], "Pokreni Kalkulator")
        self.assertEqual(properties['description'], "Otvara GNOME kalkulator kad se pritisne.")
        self.assertEqual(properties['icon'], "icon.png")

if __name__ == '__main__':
    unittest.main()