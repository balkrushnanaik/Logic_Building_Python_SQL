def nail_biting_suggestions():
    """Provide suggestions and cons about nail biting"""
    
    print("=" * 50)
    print("NAIL BITING - CONS AND SUGGESTIONS")
    print("=" * 50)
    
    cons = [
        "Damaged nail beds and cuticles",
        "Increased risk of infections",
        "Poor oral hygiene and dental issues",
        "Social embarrassment and self-consciousness",
        "Spread of germs and bacteria to mouth",
        "Weakened immune system from infections",
        "Bleeding and pain in fingers",
        "Skin infections around nails",
        "Difficulty typing or using hands",
        "Psychological stress and anxiety"
    ]
    
    suggestions = [
        "Keep nails trimmed short to reduce temptation",
        "Wear gloves or bandages on fingers",
        "Apply bitter-tasting nail polish",
        "Practice stress-relief techniques like meditation",
        "Find alternative habits (fidget toys, gum chewing)",
        "Maintain proper hand hygiene",
        "Identify triggers and avoid them",
        "Use hand creams with pleasant scents",
        "Seek professional help if it's compulsive",
        "Reward yourself for not biting nails"
    ]
    
    print("\n📌 CONS OF NAIL BITING:")
    for i, con in enumerate(cons, 1):
        print(f"   {i}. {con}")
    
    print("\n💡 SUGGESTIONS TO STOP NAIL BITING:")
    for i, suggestion in enumerate(suggestions, 1):
        print(f"   {i}. {suggestion}")
    
    print("\n" + "=" * 50)

if __name__ == "__main__":
    nail_biting_suggestions()
