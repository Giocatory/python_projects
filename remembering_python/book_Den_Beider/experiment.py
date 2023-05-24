match t := input():
    case "Flask" | "Django" | "Fast-API":
        print(f"Python({t}),Backend-dev")
    case "Angular" | "React" | "Vue":
        print(f"JavaScript/TypeScript({t}),Frontend-dev")
    case "Flutter" | "React Native":
        print(f"JavaScript({t}),Cross-Mobile-dev")
    case "Pandas" | "skit-learn" | "keras":
        print(f"Python({t}),Data-Scientist")
    case _:
        print("модель еще не обучена")