import math

ANS = 0          # stores last answer
MODE = "degrees" # angle mode

def calc_expression(expr: str) -> float:
    """Evaluate math or scientific expressions safely."""
    global ANS, MODE
    try:
        # replace shortcuts
        expr = expr.replace("^", "**")
        expr = expr.replace("ANS", str(ANS))
        expr = expr.replace("π", str(math.pi))
        expr = expr.replace("e", str(math.e))

        # allow degree trig by converting before math.*
        if MODE == "degrees":
            expr = expr.replace("sin(", "math.sin(math.radians(")
            expr = expr.replace("cos(", "math.cos(math.radians(")
            expr = expr.replace("tan(", "math.tan(math.radians(")
            expr = expr.replace("asin(", "math.degrees(math.asin(")
            expr = expr.replace("acos(", "math.degrees(math.acos(")
            expr = expr.replace("atan(", "math.degrees(math.atan(")
        else:
            expr = expr.replace("sin(",  "math.sin(")
            expr = expr.replace("cos(", "math.cos(")
            expr = expr.replace("tan(", "math.tan(")
            expr = expr.replace("asin(", "math.asin(")
            expr = expr.replace("acos(", "math.acos(")
            expr = expr.replace("atan(", "math.atan(")

        # other functions
        expr = expr.replace("sqrt(", "math.sqrt(")
        expr = expr.replace("cbrt(", "(**(1/3))(") # handled differently below
        expr = expr.replace("log(", "math.log10(")
        expr = expr.replace("ln(", "math.log(")
        expr = expr.replace("exp(", "math.exp(")
        expr = expr.replace("deg2rad(", "math.radians(")
        expr = expr.replace("rad2deg(", "math.degrees(")

        # evaluate safely
        allowed = {"math": math}
        result = eval(expr, {"__builtins__": None}, allowed)

        ANS = result
        return result

    except ZeroDivisionError:
        return "❌ Error: Division by zero"
    except ValueError:
        return "❌ Error: Math domain error"
    except Exception:
        return "❌ Error: Invalid expression"

def main():
    global MODE
    print("⚛️  Scientific Smart Calculator v2.0")
    print("Type 'exit' to quit, 'mode' to switch between degrees/radians.\n")

    while True:
        print(f"Last ANS = {ANS} | Mode: {MODE}")
        expr = input("Enter expression: ").strip()

        if expr.lower() == "exit":
            print("Goodbye, boss.")
            break

        if expr.lower() == "mode":
            MODE = "radians" if MODE == "degrees" else "degrees"
            print(f"Switched to {MODE} mode.\n")
            continue

        result = calc_expression(expr)
        print(f"➡️  Result: {result}\n")

if __name__ == "__main__":
    main()
