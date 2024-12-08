import random

class MoodOutfitSelector:
    """
    A program that suggests outfits based on the user's mood and other contextual factors
    such as the weather. It provides mood-based clothing recommendations to align with or
    boost the user's emotional state.
    """
    # Mood and weather-based outfit suggestions
    outfit_suggestions = {
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

    def suggest_outfit(self, mood, weather):
        """
        Suggest an outfit based on mood and weather.
        """
        try:
            outfits = self.outfit_suggestions[mood][weather]
            return random.choice(outfits)
        except KeyError:
            return "No outfit suggestions available for this combination."
    
    def main():
        print("Welcome to your personal outfit finder!")
        moods = list(outfit_suggestions.keys())
        weather_conditions = ("sunny", "rainy", "cold", "hot")

        mood = get_user_mood(f"What's your current mood? ({', '.join(moods)}): ", moods)
        weather = get_weather_context(f"What's the weather like? ({', '.join(weather_conditions)}): ", weather_conditions)
        uplift = suggest_outfit("Would you like an outfit to boost your mood? (yes/no): ", ["yes", "no"])

        outfit = suggest_outfit(mood, weather, boost_mood=(boost == "yes"))
        print(f"\nHere's your suggested outfit: {outfit}")

if __name__ == "__main__":
    main()


