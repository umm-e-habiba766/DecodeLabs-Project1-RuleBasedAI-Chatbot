responses = {

    "hello"        : "Hey there!  I'm DecoBot. How can I help you today?",
    "hi"           : "Hi! Welcome to DecodeLabs. What's on your mind?",
    "hey"          : "Hey! Great to see you. Ask me anything.",


    "who are you"  : "I'm DecoBot  — a rule-based AI built by an intern at DecodeLabs.",
    "what are you" : "I'm a deterministic chatbot. No hallucinations, just hard-coded logic!",

   
    "what is decodelabs" : "DecodeLabs is an AI-focused training lab helping interns build real-world AI skills.",
    "tell me about decodelabs" : "DecodeLabs runs industrial training programs on AI, ML, and software engineering.",


    "help"         : "Sure! You can ask me: who are you, what is AI, tell me a fact, or just say hello.",
    "what can you do" : "I can answer predefined questions. I'm rule-based, so I know what I know!",

    
    "what is ai"   : "AI stands for Artificial Intelligence — teaching machines to simulate human thinking.",
    "what is ml"   : "ML is Machine Learning — a subset of AI where systems learn from data.",
    "what is python": "Python is the #1 language for AI/ML development. You're using it right now!",
    "what is a dictionary" : "A Python dict stores key-value pairs with O(1) lookup — exactly how I work!",


    "tell me a fact": "Fact: The first chatbot, ELIZA, was built in 1966 at MIT. I'm its modern cousin! ",
    "tell me a joke" : "Why do programmers prefer dark mode? Because light attracts bugs! ",
    "how are you"  : "I'm running at 100% uptime — no feelings, pure logic. ",
    "what is your name" : "My name is DecoBot — your rule-based AI companion at DecodeLabs.",

    "bye"          : "Goodbye! Keep building. Type 'exit' to shut me down. ",
    "goodbye"      : "See you next time! Type 'exit' to close the session.",
}

FALLBACK = (
    " I don't understand that yet. Try: 'hello', 'what is AI', "
    "'tell me a joke', or 'help'."
)


EXIT_COMMANDS = {"exit", "quit", "q", "close", "shutdown"}



def sanitize(raw: str) -> str:
    """Phase 1 — Input Sanitization & Normalization.
    Converts any casing and strips whitespace so
    'Hello', 'HELLO', '  hello  ' all become 'hello'.
    """
    return raw.lower().strip()


def get_response(clean_input: str) -> str:
    """Phase 2 — Intent Matching via O(1) Dictionary Lookup.
    Uses .get() for atomic lookup + fallback in one operation.
    """
    return responses.get(clean_input, FALLBACK)



def main():
    print("=" * 55)
    print("   DecoBot   |  DecodeLabs AI Chatbot  |  Batch 2026")
    print("=" * 55)
    print("   Type 'help' to see what I can do.")
    print("   Type 'exit' to shut me down.")
    print("-" * 55)

    while True:

        raw_input  = input("\n  You: ")
        clean_input = sanitize(raw_input)

    
        if clean_input in EXIT_COMMANDS:
            print("\n  DecoBot: Session terminated. Goodbye, Engineer!")
            print("=" * 55)
            break

        if not clean_input:
            print("  DecoBot: (silence detected) Please say something!")
            continue

        reply = get_response(clean_input)
        print(f"\n  DecoBot: {reply}")

if __name__ == "__main__":
    main()
