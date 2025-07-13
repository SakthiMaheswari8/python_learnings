'''tryblock
try:
    a=[1,2,3]
    print(int(a))
    print(b)
except NameError:
  print("name error")
except ValueError:
  print("value error")
except TypeError:
  print("type error")
else:
  print("Nothing went wrong")
finally:
    print("thank you")'''
    
    
def calculate_power_custom(base, exponent):
        if exponent < 0:
            # Handle negative exponents (e.g., return 1 / base**abs(exponent))
            return 1 / (base ** abs(exponent))
        elif exponent == 0:
            return 1
        else:
            result = 1
            for _ in range(exponent):
                result *= base
            return result

    # Example usage:
result = calculate_power_custom(1, 4)  # 3 raised to the power of 4
print(result)
