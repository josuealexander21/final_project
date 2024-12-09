import random

class MoodOutfitSelector:
    """
    A program that suggests outfits based on the user's mood and other contextual factors
    such as the weather. It provides mood-based clothing recommendations to align with
    or boost the user's emotional state.
    """

    def __init__(self):
        
        self.outfit_suggestions = {
            "happy": {
                "sunny": ["bright sundress", "colorful t-shirt and shorts", "light linen outfit"],
                "rainy": ["yellow raincoat", "jeans and waterproof boots", "cute umbrella accessory"],
                "cold": ["cheerful sweater", "wool scarf and beanie", "layered outfit with boots"],
                "hot": ["flowy summer dress", "tank top and shorts", "light pastel blouse"]
            },
            "calm": {
                "sunny": ["light blue shirt", "comfortable jeans", "soft cardigan"],
                "rainy": ["cozy hoodie", "rainproof jacket", "soft scarf"],
                "cold": ["oversized sweater", "corduroy pants", "knit beanie"],
                "hot": ["cotton jumpsuit", "linen trousers and top", "simple tank top"]
            }
        }

    def get_user_mood(self):

        """
        Gets the user to enter their current mood.
        
        Returns:
            str: The mood input by the user (e.g., "happy", "calm").
        
        Raises:
            ValueError: If the user enters an invalid mood that is not recognized.
        """
        moods = list(self.outfit_suggestions.keys())
        mood = input(f"How are you feeling today? ({', '.join(moods)}): ").lower()
        while mood not in moods:
            print(f"Please enter a valid mood: {', '.join(moods)}.")
            mood = input(f"How are you feeling today? ({', '.join(moods)}): ").lower()
        return mood

    def get_weather_context(self):

        """ 
        Gets the user to enter the current weather condition.

        Returns:
            str: The weather condition input by the user (e.g., "sunny", "rainy").
        """
        weather_conditions = ["sunny", "rainy", "cold", "hot"]
        weather = input(f"What's the weather like today? ({', '.join(weather_conditions)}): ").lower()
        while weather not in weather_conditions:
            print(f"Please enter a valid weather condition: {', '.join(weather_conditions)}.")
            weather = input(f"What's the weather like today? ({', '.join(weather_conditions)}): ").lower()
        return weather

    def suggest_outfit(self, mood, weather, uplift):

        """
        Suggests an outfit based on mood and weather. Includes the option to boost the users mood.

        Args:
            mood (str): The user's mood.
            weather (str): The current weather condition.
            uplift (str): "yes" to boost the mood, "no" to stay aligned with the mood.

        Returns:
            str: A randomly selected outfit suggestion.
        """
        if uplift == "yes":
            mood = "happy"  # Boost mood by suggesting a 'happy' outfit

        try:
            outfits = self.outfit_suggestions[mood][weather]
            return random.choice(outfits)
        except KeyError:
            return "No outfit suggestions available for this combination."


def main():

    print("Welcome to your personal outfit finder!")
    selector = MoodOutfitSelector()

    # this gets user inputs
    mood = selector.get_user_mood()
    weather = selector.get_weather_context()
    uplift = input("Would you like an outfit to boost your mood? (yes/no): ").lower()

    # this will uggest outfit
    outfit = selector.suggest_outfit(mood, weather, uplift)
    print(f"\nHere's your suggested outfit: {outfit}")


if __name__ == "__main__":
    main()