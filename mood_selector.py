import random

class MoodOutfitSelector:
    """
    A program that suggests outfits based on the user's mood and other contextual factors
    such as the weather. It provides mood-based clothing recommendations to align with or
    boost the user's emotional state.
    """

    def get_user_mood(self):
        """
        Prompt the user to enter their current mood.
        
        Returns:
            str: The mood input by the user (e.g., "happy", "calm", "excited", "sad/melancholy").
        
        Raises:
            ValueError: If the user enters an invalid mood that is not recognized.
        """
        mood = input("How are you feeling today? (happy, calm, excited, sad): ").lower()
        outfit_suggestions = []
        while mood not in outfit_suggestions:
            print("Please enter a mood: happy, calm, excited, or sad.")
            mood = input("How are you feeling today? (happy, calm, excited, sad): ").lower()
        return mood

    def get_weather_context(self):
        """ 
        This gets the weather that the user inputs.

        Returns:
            str: The weather condition input by the user (e.g., "sunny", "rainy", "cold", "hot").
        """

        weather = input("What's the weather like today? (sunny, rainy, cold, hot): ").lower()
        weather_options = ["sunny, partly_cloudy, cloudy, rainy, foggy, storming"]
        while weather not in weather_options:
            print("Please enter a weather condition: sunny, rainy, snow, cold, or hot.")
            weather = input("What's the weather like today? (sunny, rainy, cold, hot): ").lower()
        return weather
