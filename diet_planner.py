from openai import OpenAI

# Add your API key here
client = OpenAI(api_key="YOUR_API_KEY_HERE")

def get_diet_plan(age, weight, goal):
    prompt = f"""
    Create a simple Indian diet plan.

    Age: {age}
    Weight: {weight} kg
    Goal: {goal}

    Include:
    - Breakfast
    - Lunch
    - Dinner
    - Snacks
    Keep it simple and healthy.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


# ---- User Input ----
age = input("Enter your age: ")
weight = input("Enter your weight (kg): ")
goal = input("Enter your goal (weight loss / gain / maintain): ")

# ---- Generate Plan ----
plan = get_diet_plan(age, weight, goal)

print("\n🥗 Your AI Diet Plan:\n")
print(plan)
