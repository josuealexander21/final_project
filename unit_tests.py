import unittest
from unittest.mock import patch
from io import StringIO
from final_outfit_selector import MoodOutfitSelector, Outfit  


class TestMoodOutfitSelector(unittest.TestCase):
    
    def setUp(self):
 
        self.mood_outfit_selector = MoodOutfitSelector()
        
    @patch('builtins.input')
    def test_get_user_mood_valid(self, mock_input):
        # Mock input to simulate the user typing "happy"
        mock_input.return_value = 'happy'
        
        # Simulate the method call
        mood = self.mood_outfit_selector.get_user_mood()
        
        # Test if the returned mood is correct
        self.assertEqual(mood, 'happy')

    @patch('builtins.input')
    def test_get_user_mood_invalid_first_then_valid(self, mock_input):
        # Simulate the user first entering an invalid mood, then a valid one
        mock_input.side_effect = ['angry', 'happy']  # First invalid, then valid
        
        # Simulate the method call
        mood = self.mood_outfit_selector.get_user_mood()
        
        # Test if the returned mood is the valid one
        self.assertEqual(mood, 'happy')

    @patch('builtins.input')
    def test_get_user_mood_invalid(self, mock_input):
        # Simulate the user entering an invalid mood repeatedly
        mock_input.side_effect = ['angry', 'sad', 'happy']  # Invalid moods followed by valid
        
        # Simulate the method call
        mood = self.mood_outfit_selector.get_user_mood()
        
        # Test if the returned mood is the valid one
        self.assertEqual(mood, 'happy')

if __name__ == '__main__':
    unittest.main()
