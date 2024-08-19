import unittest
from unittest.mock import patch
import winsound  # Import winsound here
from alarm_clock import alarm_logic

class TestAlarmLogic(unittest.TestCase):

    @patch('winsound.PlaySound')
    @patch('time.sleep', return_value=None)  # Mock sleep to avoid delay during testing
    @patch('datetime.datetime')
    def test_alarm_logic(self, mock_datetime, mock_sleep, mock_play_sound):
        # Set the mock current time
        mock_datetime.now.return_value.strftime.return_value = "00:00:00"

        # Call the alarm logic directly
        alarm_logic("00:00:00", mock_play_sound)

        # Check if the PlaySound function was called with the correct arguments
        mock_play_sound.assert_called_with("sound.wav", winsound.SND_ASYNC)

if __name__ == '__main__':
    unittest.main()
